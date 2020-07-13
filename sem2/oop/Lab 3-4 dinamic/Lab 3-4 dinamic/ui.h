#pragma once
#include "controller.h"

typedef struct {
	MaterialController* controller;
}UI;

UI* create_allocate_UI(MaterialController * controller);
void destroy(UI* ui);
void run(UI * ui);
