#pragma once
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct {
	char* name;
	char* supplier;
	char* expiration;
	int quantity;
}Material;

Material * create_material(char * material, char * supplier, int quantity, char * expiration)
