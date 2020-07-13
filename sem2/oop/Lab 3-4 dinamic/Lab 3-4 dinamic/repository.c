#include "repository.h"

MaterialRepository * create_allocate_repository()
{
	MaterialRepository * repo = (MaterialRepository*)malloc(sizeof(MaterialRepository));
	repo->material = allocate_array(20);
	return repo;
}
