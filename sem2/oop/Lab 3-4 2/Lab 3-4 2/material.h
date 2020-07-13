#pragma once

typedef struct {
	char* name;
	char* supplier;
	int quantity;
	char* expiration;
}Material;

Material* createMaterial(char* name, char* supplier, int quantity, char* expiration);

void destroyMaterial(Material * m);

Material* copy_material(Material* material);

char* get_type(Material* material);

char* get_address(Material* material);

double get_surface(Material* material);

double get_price(Material* material);

void toString(Material* material, char str[]);

Material* copy_material(Material* material);