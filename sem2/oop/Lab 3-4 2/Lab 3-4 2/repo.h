#pragma once
//#include "material.h"
#include "d.h"

#include <stdio.h>
#include <stdlib.h>


typedef struct {
	DynamicArray* materials;
}MaterialRepo;

MaterialRepo* createRepo();

/*
destroy_repository desrroys a repository by deallocating the memory already allocated
*/
void destroy_repository(MaterialRepo* repo);

int add_repository(MaterialRepo* repo, TElement t);
int get_repo_length(MaterialRepo* repo);

Material* delete_repository(MaterialRepo* repo, char* address);
Material* update_repository(MaterialRepo* repo, TElement t);
