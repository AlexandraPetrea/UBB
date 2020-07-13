#include "cost.h"
#include"Repository.h"
#include"Controller.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
	QApplication a(argc, argv);
	Repository r;
	Controller c{ r };
	cost w{ c };
	w.show();
	return a.exec();
}
