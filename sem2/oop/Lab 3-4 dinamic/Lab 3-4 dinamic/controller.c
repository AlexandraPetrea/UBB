#include "controller.h"

MaterialController* create_allocate_controller(MaterialRepository* repo, OperationStack* undo_stack, OperationStack* redo_stack)
{
	MaterialController* ctrl = (MaterialController*)malloc(sizeof(MaterialController));
	//ctrl->repo = (EstateRepository*)malloc(sizeof(EstateRepository));
	ctrl->repo = repo;
	ctrl->undo_stack = undo_stack;
	ctrl->redo_stack = redo_stack;

	return ctrl;

}

void destroy_controller(MaterialController * ctrl)
{
	destroy_repository(ctrl->repo);
	free(ctrl);
}