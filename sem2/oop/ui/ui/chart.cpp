#include "chart.h"
#include "ui_chart.h"
#include "util.h"
#include <QMessageBox>

chart::chart(Controller ctrl, QWidget *parent) :
	QDialog(parent),
	ui(new Ui::chart)
{
	ui->setupUi(this);

	this->ctrl = ctrl;

}
chart::~chart()
{
	delete ui;
}