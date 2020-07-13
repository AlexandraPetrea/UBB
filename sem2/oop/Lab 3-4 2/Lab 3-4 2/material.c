#include "material.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

Material* createMaterial(char* name, char* supplier, int quantity, char* expiration)
{
	Material* m = (Material*)malloc(sizeof(Material));
	m->name = (char*)malloc(sizeof(char)*(strlen(name) + 1));
	strcpy(m->name, name);
	m->supplier = (char*)malloc(sizeof(char)*(strlen(supplier) + 1));
	strcpy(m->supplier, supplier);
	
	m->quantity = quantity;

	m->expiration = (char*)malloc(sizeof(char)*(strlen(expiration) + 1));
	strcpy(m->expiration, expiration);

	return m;
}


void destroyMaterial(Material * m)
{
	free(m->name);
	free(m->supplier);
	free(m->expiration);
	free(m);
}
Material* copy_material(Material * material)
{
	Material* new_material = createMaterial(material->name, material->supplier, material->quantity, material->expiration);
	return new_material;
}


char* get_name(Material* m)
{
	return m->name;
}

char* getSupplier(Material* m)
{
	return m->supplier;
}

char* getExpiration(Material* m)
{
	return m->expiration;
}
int getQuantity(Material* m)
{
	return m->quantity;
}

void toString(Material* m, char str[])
{
	sprintf(str, "%s %s %d %s.", m->name, m->supplier, m->quantity, m->expiration);
}