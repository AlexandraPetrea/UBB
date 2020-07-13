#include "repo.h"
#include "ui.h"

int main()
{
	MaterialRepo * repo = createRepo();

	OperationStack* undo_stack = create_operation_stack();
	OperationStack* redo_stack = create_operation_stack();

	Controller * ctrl = create_allocate_controller(repo);


	UI * ui = create_allocate_UI(ctrl);

	startUI(ui);
	destroyUI(ui);

	return 0;
}