#pragma once
#include <stdio.h>
#include <stdlib.h>
#include "controller.h"

typedef struct
{
	Controller* ctrl;
} UI;

UI* create_allocate_UI(Controller* c);
void destroyUI(UI* ui);

void startUI(UI* ui);