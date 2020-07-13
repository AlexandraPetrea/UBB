#include "repo.h"

MaterialRepo* createRepo() 
{
	MaterialRepo* v = (MaterialRepo*)malloc(sizeof(MaterialRepo));
	v->materials = allocate_array(20);

	return v;
}

void destroy_repository(MaterialRepo* repo)
{
	deallocate_array(repo->materials);
	free(repo);
}

int add_repository(MaterialRepo* repo, TElement t)
{
	//if (repo->materials->length == 0)
		//add_to_array(repo->materials, t);
	if (search_by_name(repo->materials, t) == -1)
		//repo->estates->elems[length] = t;
	{
		add_to_array(repo->materials, t);
		return 1; //succes
	}

	else
		return 0; //era deja gasit
}
	
	
int get_repo_length(MaterialRepo * repo)
{
	return get_length(repo->materials);

}

Material* delete_repository(MaterialRepo * repo, char * name)
{
	int pos = search_by_name(repo->materials, name);
	if (pos == -1)
		return NULL;
	Material* new_material = copy_material(repo->materials->elems[pos]);
	delete_from_array(repo->materials, pos);
	return new_material;
}

Material* update_repository(MaterialRepo* repo, TElement t)
{
	int pos = search_by_name(repo->materials, t->name);
	if (pos < 0 || pos >= repo->materials->length)
		return NULL;
	Material* new_material = copy_material(repo->materials->elems[pos]);
	update_array(repo->materials, pos, t);
	return new_material;
}
