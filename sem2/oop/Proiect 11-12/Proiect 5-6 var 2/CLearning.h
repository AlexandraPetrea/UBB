#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_CLearning.h"

class CLearning : public QMainWindow
{
	Q_OBJECT

public:
	CLearning(QWidget *parent = 0);
	~CLearning();

private:
	Ui::CLearningClass ui;
};
