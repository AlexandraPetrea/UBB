#ifndef CHART_H
#define CHART_H

#include <QDialog>
#include "controller.h"
#include <cstring>

namespace Ui {
	class chart;
}

class chart : public QDialog
{
	Q_OBJECT

public:
	explicit chart(Controller ctrl, QWidget *parent = 0);
	~chart();

private:
	Ui::chart *ui;
	Controller ctrl;
	std::vector<std::string> genres;
};

#endif // CHART_H