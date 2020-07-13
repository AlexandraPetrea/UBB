#pragma once
#include<vector>
#include <algorithm>
#include "repository.h"
#include "Controller.h"
#include "Film.h"
#include <QtWidgets/qmainwindow.h>
#include <QtWidgets/qlistwidget.h>
#include <QtWidgets/qboxlayout.h>
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/qformlayout.h>
#include <QtWidgets/qlabel.h>
#include <QtWidgets/qpushbutton.h>
#include <QtWidgets/qradiobutton.h>
#include <QtWidgets/qmessagebox.h>
#include <QtWidgets/qbuttongroup.h>

using namespace std;

class GUI :public QWidget
{
	Q_OBJECT

public:
	GUI(Controller& c, QWidget* parent = 0);
	~GUI();
private:
	QListWidget * repoList;
	QLineEdit* titleEdit;
	QLineEdit* presenterEdit;
	QLineEdit* likesEdit;
	QLineEdit* durationEdit;
	QLineEdit* linkEdit;
	QLineEdit* viewsEdit;
	QPushButton* addButton;
	QPushButton* deleteButton;
	QPushButton* moveOneTutorialButton;
	QPushButton* moveAllTutorialsButton;
	QListWidget * watchList;

	Controller& ctrl;
	vector<Tutorial> elemsRepo;
	void initGUI();
	void populateRepo();
	void populateWatchList();
	int getRepoIndex();
	private slots:
	void addNewTutorial();
	void deleteTutorial();
	void moveTutorialToWatchlist();
	void moveAllTutorials();
	void connectSignalsAndSlots();
};
