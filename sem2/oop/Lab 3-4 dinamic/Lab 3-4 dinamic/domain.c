#include "domain.h"

Material * create_material(char * name, char * supplier, int quantity, char * expiration)
{
	Material * material = (Material*)malloc(sizeof(Material));
	material->name = (char*)malloc(sizeof(char)*strlen(name) + 1);

	material->supplier = (char*)malloc(sizeof(char)*strlen(supplier) + 1);

	material->expiration = (char*)malloc(sizeof(char)*strlen(expiration) + 1);
	
	strcpy(material->name, name);
	strcpy(material->supplier, supplier);
	strcpy(material->expiration, expiration);

	material->quantity = quantity;

	return material;
}

void destroy_material(Material * material)
{
	free(material->name);
	free(material->supplier);
	free(material->expiration);
	free(material);
}