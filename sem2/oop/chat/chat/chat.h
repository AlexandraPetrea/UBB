#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_chat.h"

class chat : public QMainWindow
{
	Q_OBJECT

public:
	chat(QWidget *parent = Q_NULLPTR);

private:
	Ui::chatClass ui;
};
