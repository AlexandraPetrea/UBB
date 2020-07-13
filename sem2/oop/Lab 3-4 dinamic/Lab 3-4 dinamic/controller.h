#pragma once
#include <stdio.h>
#include <stdlib.h>
#include "repository.h"

typedef struct {

	MaterialRepository * repo;
	OperationStack * undo_stack;
	OperationStack * redo_stack;
}MaterialController;


