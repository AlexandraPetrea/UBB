#pragma once
#include "repo.h"
#include "op.h"

typedef struct 
{
	MaterialRepo* repo;
	OperationStack* undo_stack;
	OperationStack* redo_stack;
}Controller;

Controller* create_allocate_controller(MaterialRepo* r);
void destroyController(Controller* c);
int undo(Controller* ctrl);
int redo(Controller* ctrl);