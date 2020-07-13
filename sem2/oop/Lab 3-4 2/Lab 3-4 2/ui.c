#include "ui.h"
#include <stdio.h>
#include <stdlib.h>

UI* create_allocate_UI(Controller * c)
{
	UI* ui = (UI*)malloc(sizeof(UI));
	ui->ctrl = c;

	return ui;
}

void destroyUI(UI * ui)
{
	destroy_controller(ui->ctrl);

	free(ui);
}

void printMenu()
{
	printf("1. Add a material to repo\n");
	printf("2. Delete a material\n");
	printf("3. Update a material\n");
	printf("4. List all the materials\n");
	printf("5. Filter by a given string and past their expiration date\n");
	printf("6. Filter by supplier, in short quantity and ascending by quantities\n");
	printf("7. Undo\n");
	printf("8. Redo\n");
	printf("\n");
}

int readCommand(const char* s)
{	
	char aux[16];
	int res = 0;
	int r = 0;
	printf(s);
	scanf("%s", aux);
	r = sscanf(aux, "%d", &res);

	return res;
}

void addMaterialUI(UI* ui)
{
	char name[50], supplier[50], expiration[12];
	int quantity = 0;

	printf("Please enter the name:\n");
	scanf("%49s", name);
	printf("Please enter the supplier:\n");
	scanf("%49s", supplier);
	printf("Please enter the quantity:\n");
	scanf("%d", &quantity);
	printf("Please enter the expiration date:\n");
	scanf("%11s", expiration);
	
	return add_controller(ui->ctrl, name, supplier, quantity, expiration);
}

void deleteMaterialUI(UI* ui)
{
	char name[100];
	printf("> Give name: ");
	scanf("%s", name);
	int result = delete_controller(ui->ctrl, name);
	if (result == 0)
		printf("> DELETE FAILED\n");
}
void print_materials(UI* ui)
{
	MaterialRepo* repo = get_repo(ui->ctrl);
	int length = get_repo_length(repo);
	if (length == 0)
	{
		printf("> NO MATERIALS\n");

	}
	else
	{
		char str[900];
		for (int i = 0; i < length; i++)
		{
			toString(repo->materials->elems[i], str);
			printf("%s\n", str);
		}
	}
}
void update_UI(UI* ui)
{
	char name[100], new_supplier[100], new_expiration[14];
	int new_quantity;
	printf("> Please insert a name: ");
	scanf("%s", name);
	printf("> NEW SUPPLIER: ");
	scanf("%s", new_supplier);
	printf("> NEW EXPIRATION DATE: ");
	scanf("%s", new_expiration);
	new_quantity = readCommand("> NEW QUANTITY: ");
	//printf("%s %s %d %s", name, new_supplier, new_quantity, new_expiration);

	int result = update_controller(ui->ctrl, name, new_supplier, new_quantity, new_expiration);
	if (result == 0)
	{
		printf("> The name is invalid or it does not exist. Please try again. UPDATE FAILED!\n");

	}

}

void filter_by_string(UI* ui)
{
	char str[30], s[170];
	printf("> Search for: ");
	scanf("%s", str);
	if (strcmp(str, "null") == 0)
		print_materials(ui);
	else
	{
		int i;
		MaterialRepo* repo = filter_by_keyword(ui->ctrl, str);
		if (get_repo_length(repo) == 0)
			printf("> Sorry! No items matching te requested keyword.\n");
		else
		{
			//repo = sort_repository(ui->ctrl, repo);
			repo = dataToInt(ui->ctrl, repo);
			for (i = 0; i < repo->materials->length; i++)
			{
				toString(repo->materials->elems[i], s);
				printf("%s\n", s);
			}
		}
	}
}

void filter_s(UI* ui)
{
	char supplier[40], s[100];
	printf("> SUPPLIER: ");
	scanf("%s", supplier);
	int min_sf = readCommand("> Give min_quantity: ");
	MaterialRepo* repo = filter_by_name(ui->ctrl, supplier);
	repo = filter_by_quantity(ui->ctrl, min_sf, repo);
	//repo = sort_repository_a(ui->ctrl, repo);
	if (get_repo_length(repo) == 0)
		printf("> NO ITEMS MATCHING\n");
	else {
		for (int i = 0; i < repo->materials->length; i++) {
			toString(repo->materials->elems[i], s);
			printf("%s\n", s);
		}
	}
}

void startUI(UI* ui)
{
	//addMaterial(ui->ctrl, "a", "b", 1, "2");
	add_controller(ui->ctrl,"faina", "AAA", 12, "12/02/2018/");
	add_controller(ui->ctrl, "ciocolata", "Cioco", 6, "10/04/2019/");
	add_controller(ui->ctrl, "vanilie", "Van", 10, "10/04/2017/");
	add_controller(ui->ctrl, "visine", "RomArt", 1200, "10/03/2018/");
	add_controller(ui->ctrl, "drojdie", "Buc", 132, "8/02/2016/");
	add_controller(ui->ctrl, "rom", "Van", 8, "8/02/2019/");
	while (1) {
		printMenu();
		int op = readCommand("Please enter the command:\n");
		//system("pause");
		if (op == 1)
		{
			addMaterialUI(ui);
			printf("Succesful added!");
			op = 2;
		}
		else
		if (op == 2)
		{
			deleteMaterialUI(ui);
		}
		else
			if (op == 3)
				update_UI(ui);
		else
			if (op == 4)
			{
				print_materials(ui);
			}
		else
			if (op == 5)
			{
				filter_by_string(ui);

			}
		else
			if (op == 6)
			{
				filter_s(ui);
			}
		else
			if (op == 7)
			{
			//	int res = undo(ui->ctrl);
				//if (res == 0)
					//printf("> Cannot undo more!\n");
				break;
			}
		else
			if (op == 8)
			{
				//printf("DA");
			//	dataToInt(ui->ctrl, ui->ctrl->repo);
				//printf("Rez is %d\n", res);
			}

			else
			{
				int aux = search_by_name(ui->ctrl->repo->materials, "faina");
				printf("%d", aux);
				
			}


	}
}