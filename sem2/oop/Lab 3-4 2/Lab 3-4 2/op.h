#pragma once
#include <stdio.h>
#include <stdlib.h>

//#include "material.h"
#include "d.h"

typedef struct
{
	Material* material;

	char* type;
}Operation;

Operation* create_operation(Material* material, char* type);
// Creates an operation
void destroy_operation(Operation* op);
// Frees the memory for an operation
Operation* operation_copy(Operation* op);
// Returns a copy of an operation
char* get_operation_type(Operation* op);
// Returns a char containing the type of an operation
Material* get_operation_material(Operation* op);
// Returns the estate in an operation

// --------------------------------------------------

typedef struct
{
	Operation* operations[100];
	int length;
}OperationStack;

OperationStack* create_operation_stack();
// Creates an operation stack
void destroy_operation_stack(OperationStack* stack);
// Destroys an operation stack
void push(OperationStack* stack, Operation* op);
// Pushes an operation onto the stack
Operation* pop(OperationStack* stack);
// Pops an operation from the stack (and returns it)

void test_operation_stack();


