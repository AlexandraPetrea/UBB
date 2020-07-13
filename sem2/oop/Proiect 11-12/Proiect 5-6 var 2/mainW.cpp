#include "mainW.h"
#include <QtWidgets>

MainWindow::MainWindow(QWidget *parent)
{
	QPushButton *train_button = new QPushButton(this);
	train_button->setText(tr("something"));
	train_button->move(600, 600);
	train_button->show();
}