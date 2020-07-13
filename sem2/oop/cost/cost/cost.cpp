#include "cost.h"
#include <qboxlayout.h>
#include <algorithm>
#include "qformlayout.h"
#include "qcolor.h"
#include"qfont.h"

cost::cost(Controller &c, QWidget *parent)
	: cont{ c }, QWidget(parent)
{
	ui.setupUi(this);
	this->currentBillsInRepo = this->cont.getListCont();
	this->initGUI();
}

cost::~cost ()
{
}

void cost::initGUI() {

	std::sort(this->currentBillsInRepo.begin(), this->currentBillsInRepo.end());
	for (auto b : this->currentBillsInRepo)
	{
		QString itemInList = QString::fromStdString(b.getDescription() + "- " + std::to_string(b.getPriority()));
		QListWidgetItem *item = new QListWidgetItem(itemInList);
		QFont font;
		font.setBold(true);
		if (b.getPriority() == 1)
			//item->Text(font.bold = true);
			//item->setBackgroundColor(QColor("red"));	
			//item->QFont::bold(true);
			//item->(QFont font(item->font)).setBold(true);
			//item->setFont(QFont("bold"));
			//item->setFont(QFont("bold"));
		//item->setFont(QFont::Bold);
		item->setFont(font);
			
		ui.repoList->addItem(item);
	}
}


void cost::on_pushButton_2_clicked()
{
	std::string priority = ui.lineEdit->text().toStdString();
	int sum = 0;
	sum = cont.calculateDuration(priority);

	ui.label_3->setText(QString::number(sum));
}
