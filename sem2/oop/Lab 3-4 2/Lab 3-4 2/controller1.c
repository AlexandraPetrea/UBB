#include "controller.h"

Controller* create_allocate_controller(MaterialRepo* repo, OperationStack* undo_stack, OperationStack* redo_stack)
{
	Controller* ctrl = (Controller*)malloc(sizeof(Controller));
	//ctrl->repo = (EstateRepository*)malloc(sizeof(EstateRepository));
	ctrl->repo = repo;
	ctrl->undo_stack = undo_stack;
	ctrl->redo_stack = redo_stack;

	return ctrl;

}

void destroy_controller(Controller* ctrl)
{
	destroy_repository(ctrl->repo);
	free(ctrl);
}

int add_controller(Controller* ctrl, char* name, char* supplier, int quantity, char* expiration)
{
	int result;
	Material* material = createMaterial(name, supplier, quantity, expiration);
	result = add_repository(ctrl->repo, material);
	if (result == 1) {
		Operation* op = create_operation(material, "add");
		push(ctrl->undo_stack, op);
		destroy_operation(op);
		destroy_operation_stack(ctrl->redo_stack);
		ctrl->redo_stack = create_operation_stack();
	}
	return result;

}

MaterialRepo * get_repo(Controller * ctrl)
{
	return ctrl->repo;
}

int delete_controller(Controller * ctrl, char * name)
{
	Material* result = delete_repository(ctrl->repo, name);
	if (result != NULL) {
		Operation* op = create_operation(result, "del");
		push(ctrl->undo_stack, op);
		destroy_operation(op);
		destroy_operation_stack(ctrl->redo_stack);
		ctrl->redo_stack = create_operation_stack();
		return 1;
	}
	return 0;

}

int update_controller(Controller * ctrl, char * name, char * supplier, int quantity, char * expiration)
{
	Material* new_material = createMaterial(name,supplier, quantity, expiration);
	Material* result = update_repository(ctrl->repo, new_material);
	if (result != NULL) {
		Operation* op = create_operation(result, "update");
		push(ctrl->undo_stack, op);
		destroy_operation(op);
		destroy_operation_stack(ctrl->redo_stack);
		ctrl->redo_stack = create_operation_stack();

		return 1;
	}
	return 0;
}

MaterialRepo * filter_by_keyword(Controller * ctrl, char key[])
{
	MaterialRepo* repo = createRepo();
	int i;
	for (i = 0; i < ctrl->repo->materials->length; i++)
		if (strstr(get_name(ctrl->repo->materials->elems[i]), key) != NULL)
			add_repository(repo, ctrl->repo->materials->elems[i]);

	return repo;
}

MaterialRepo* sort_repository(Controller* ctrl, MaterialRepo* repository)
{
	int i, j;
	Material* aux;
	for (i = 0; i < repository->materials->length - 1; i++)
	{
		for (j = i + 1; j < repository->materials->length; j++)
		{
			if (repository->materials->elems[i] > repository->materials->elems[j])
			{
				aux = repository->materials->elems[j];
				repository->materials->elems[j] = repository->materials->elems[i];
				repository->materials->elems[i] = aux;
			}
		}
	}
	return repository;
}
/*
EstateRepository* sort_repository_l(EstateController* ctrl, EstateRepository* repository)
{
	int i, j;
	Estate* aux;
	for (i = 0; i < repository->estates->length - 1; i++)
	{
		for (j = i + 1; j < repository->estates->length; j++)
		{
			if (get_price(repository->estates->elems[i]) > get_price(repository->estates->elems[j]))
			{
				aux = repository->estates->elems[j];
				repository->estates->elems[j] = repository->estates->elems[i];
				repository->estates->elems[i] = aux;
			}
		}
	}
	return repository;
}
*/
MaterialRepo * filter_by_name(Controller * ctrl, char * key)
{
	MaterialRepo* repo = createRepo();
	int i;
	for (i = 0; i < ctrl->repo->materials->length; i++)
		if (strstr(get_name(ctrl->repo->materials->elems[i]), key) != NULL)
			add_repository(repo, ctrl->repo->materials->elems[i]);


	return repo;
}

MaterialRepo* filter_by_quantity(Controller* ctrl, double min_surface, MaterialRepo* repo)
{
	MaterialRepo* new_repo = createRepo();
	int i;
	for (i = 0; i < repo->materials->length; i++)
	{
		if (min_surface <= getQuantity(repo->materials->elems[i]))
			add_repository(new_repo, repo->materials->elems[i]);
	}
	return new_repo;
}


int undo(Controller * ctrl)
{
	if (ctrl->undo_stack->length == 0)
		return 0;
	Operation* op = pop(ctrl->undo_stack);
	Operation* redo_op = operation_copy(op);
	if (strcmp(get_operation_type(redo_op), "add") == 0)
		redo_op->type = "del";
	else if (strcmp(get_operation_type(redo_op), "del") == 0)
		redo_op->type = "add";

	if (strcmp(get_operation_type(op), "add") == 0) {
		Material * material= copy_material(get_operation_material(op));
		delete_repository(ctrl->repo, get_name(material));
	}
	else if (strcmp(get_operation_type(op), "del") == 0) {
		Material * material = copy_material(get_operation_material(op));
		add_repository(ctrl->repo, material);
	}
	else if (strcmp(get_operation_type(op), "update") == 0) {
		Material * material= copy_material(get_operation_material(op));
		redo_op->material = copy_material(update_repository(ctrl->repo, material));
	}
	push(ctrl->redo_stack, redo_op);
	destroy_operation(redo_op);
	destroy_operation(op);
	return 1;
}

int redo(Controller * ctrl)
{
	if (ctrl->redo_stack->length == 0)
		return 0;
	Operation* op = pop(ctrl->redo_stack);
	Operation* undo_op = operation_copy(op);
	if (strcmp(get_operation_type(undo_op), "add") == 0)
		undo_op->type = "del";
	else if (strcmp(get_operation_type(undo_op), "del") == 0)
		undo_op->type = "add";
	if (strcmp(get_operation_type(op), "add") == 0) {
		Material * material = copy_material(get_operation_material(op));
		delete_repository(ctrl->repo, get_name(material));
	}
	else if (strcmp(get_operation_type(op), "del") == 0) {
		Material* material = copy_material(get_operation_material(op));
		add_repository(ctrl->repo, material);
	}
	else if (strcmp(get_operation_type(op), "update") == 0) {
		Material * material = copy_material(get_operation_material(op));
		undo_op->material = copy_material(update_repository(ctrl->repo, material));
	}
	push(ctrl->undo_stack, undo_op);
	destroy_operation(undo_op);
	destroy_operation(op);

	return 1;
}

MaterialRepo* dataToInt(Controller* ctrl, MaterialRepo* repository)
{
	MaterialRepo* repo = createRepo();
	char data[14];
	for (int i = 0; i < repository->materials->length; i++)
	{
		int res = 0;
		//	printf("%s \n", getExpiration(repository->materials->elems[i]));
		char * data = getExpiration(repository->materials->elems[i]);
		//printf("%s \n", data);
		char *p;
		char * day1;
		char *year1;
		char * month1;
		p = strtok(data, "/");
		day1 = p;
		p = strtok(NULL, "/");
		month1 = p;
		p = strtok(NULL, "/");
		year1 = p;
		//printf("ziua luna an %s %s %s \n", day1, month1, year1);

		time_t timer;
		struct tm* tm_info;
		char day[3];
		char month[3];
		char year[5];
		time(&timer);
		tm_info = localtime(&timer);
		strftime(day, 3, "%d", tm_info);
		strftime(month, 3, "%m", tm_info);
		strftime(year, 5, "%Y", tm_info);
		//printf("%s %s %s \n", day, month, year);

		int aux = strcmp(year, year1);
		//printf("year %d\n", aux);

		int aux1 = strcmp(month, month1);
		//printf("month %d\n", aux1);
		int aux2 = strcmp(day, day1);
		//printf("day %d\n", aux2);
		if (aux == 0 && aux1 == 0 && aux2 == 0)
			res = 0;
		if (aux == 0 && aux1 == 0)
			if (aux2 == -1)
				res = 1;
			else res = -1;
			if (aux == 0)
				if (aux1 == -1)
					res = 1;
				else res = -1;

				if (aux == -1)
					res = 1;
				else
					if (aux == 1)
						res = -1;
				//printf("Res pentru data asta %d %s \n", res, repository->materials->elems[i]->name);
				if (res == -1)
					add_repository(repo, repository->materials->elems[i]);
	}
	return repo;

}