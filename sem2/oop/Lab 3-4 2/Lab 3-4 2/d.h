#ifndef DynamicArray_h
#define DynamicArray_h

#include <stdio.h>

#include "material.h"

typedef Material* TElement;

typedef struct {
	int length;
	int capacity;
	TElement* elems;
} DynamicArray;

DynamicArray* allocate_array(int capacity);

void deallocate_array(DynamicArray* darray);

void add_to_array(DynamicArray* darray, TElement t);
void grow_capacity(DynamicArray* darray);
int search_by_address(DynamicArray* darray, char* address);
int get_length(DynamicArray* darray);
void delete_from_array(DynamicArray* darray, int pos);
void update_array(DynamicArray* darray, int pos, TElement t);


#endif /* DynamicArray_h */