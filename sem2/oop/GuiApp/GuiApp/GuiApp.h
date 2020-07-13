#pragma once
#include <QtWidgets/QMainWindow>
#include "ui_GuiApp.h"
#include "Controller.h"
#include <QListWidget>
#include <QFormLayout>
#include <QLineEdit>
#include <QPushButton>
#include <QLabel>

class WatchlistQt : public QWidget //public QMainWindow
{
	Q_OBJECT

public:
	WatchlistQt(Controller& c, QWidget *parent = 0);
	~WatchlistQt();

private:
	Controller & ctrl;
	std::vector<Film> currentFilmInRepoList;

	QListWidget* repoList;
	QLineEdit* titleEdit;
	QLineEdit* genreEdit;
	QLineEdit* durationEdit;
	QLineEdit* trailerEdit;
	QLineEdit* yearEdit;
	QLineEdit* likesEdit;
	QPushButton* addButton;
	QPushButton* deleteButton;
	QPushButton* updateButton;
	QPushButton* filterButton;
	QPushButton* moveOneFilmButton;
	QPushButton* moveAllFilmsButton;

	QListWidget* watchList;

	void initGUI();
	void populateRepoList();

	void connectSignalsAndSlots();

	void populateWatchlist();
	int getRepoListSelectedIndex();

	private slots:
	// When an item in the list is clicked, the text boxes get filled with the item's information
	void listItemChanged();
	
	void addFilm();
	void deleteFilm();
	void updateFilm();
	// filters the elements in the list, by the artist written in the artist edit box
	void filterRepoFilms();

	void moveFilmToWatchlist();
	void moveAllFilms();
	
	
};
