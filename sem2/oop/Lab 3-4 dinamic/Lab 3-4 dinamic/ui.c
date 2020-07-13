#include "ui.h"
#include <stdio.h>
#include <stdlib.h>

UI * create_allocate_UI(MaterialController * controller)
{
	UI * ui = (UI*)malloc(sizeof(UI));
	ui->controller = controller;
	return ui;
}

void destroy(UI * ui)
{
	destroy_controller(ui->controller);
	free(ui);

}

void run(UI * ui)
{
	while (1)
		printf("%s", "aici");
}