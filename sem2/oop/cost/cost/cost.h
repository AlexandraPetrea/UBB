#pragma once

#include <QtWidgets/QMainWindow>
#include "Controller.h"
#include <qwidget.h>
#include <qlistwidget.h>
#include <qlineedit.h>
#include <qpushbutton.h>
#include <qlabel.h>
#include "ui_cost.h"

class cost : public QWidget
{
	Q_OBJECT

public:
	cost(Controller &c, QWidget *parent = 0);
	~cost();

	private slots:
	void on_pushButton_2_clicked();
private:
	Controller & cont;
	std::vector<Bill> currentBillsInRepo;
	Ui::cost ui;
	void initGUI();

	
};


