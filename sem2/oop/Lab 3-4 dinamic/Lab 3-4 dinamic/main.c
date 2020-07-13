#include "ui.c"
#include "UI.h"

int main()
{

	MaterialRepository * repo = create_allocate_repository();
	
	OperationStack* undo_stack = create_operation_stack();
	OperationStack* redo_stack = create_operation_stack();

	MaterialController* controller = create_allocate_controller(repo, undo_stack, redo_stack);

	UI * ui = create_allocate_UI(controller);

	run(ui);
	
	destroy(ui);

}