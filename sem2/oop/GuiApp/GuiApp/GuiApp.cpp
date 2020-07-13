#include "GuiApp.h"
#include <vector>
#include "Film.h"
//#include "Utils.h"
#include <QMessageBox>
#include "RepositoryException.h"

WatchlistQt::WatchlistQt(Controller& c, QWidget *parent) : ctrl{ c }, QWidget{ parent }
{
	this->initGUI();
	this->currentFilmInRepoList = this->ctrl.getAllFilms();
	this->populateRepoList();
	//connectSignalsAndSlots();
}

WatchlistQt::~WatchlistQt()
{

}

void WatchlistQt::initGUI()
{
	//General layout of the window
	QHBoxLayout* layout = new QHBoxLayout{ this };

	// Prepare left side components - vertical layout with: 
	// - list
	// - form layout with the song data
	// - grid layout with buttons: add, delete, update, filter
	QWidget* leftWidget = new QWidget{};
	QVBoxLayout* leftSide = new QVBoxLayout{ leftWidget };

	// list
	this->repoList = new QListWidget{};
	// set the selection model
	this->repoList->setSelectionMode(QAbstractItemView::SingleSelection);

	// song data
	QWidget* filmDataWidget = new QWidget{};
	QFormLayout* formLayout = new QFormLayout{ filmDataWidget };
	this->titleEdit = new QLineEdit{};
	this->genreEdit = new QLineEdit{};
	this->yearEdit = new QLineEdit{};
	this->likesEdit = new QLineEdit{};
	this->durationEdit = new QLineEdit{};
	this->trailerEdit = new QLineEdit{};
	formLayout->addRow("&Title:", titleEdit);
	formLayout->addRow("&Genre:", genreEdit);
    formLayout->addRow("&Year:", yearEdit);
	formLayout->addRow("&Likes:", likesEdit);
	formLayout->addRow("&Trailer:", trailerEdit);
	formLayout->addRow("&Duration:", durationEdit);

	// buttons
	QWidget* buttonsWidget = new QWidget{};
	QGridLayout* gridLayout = new QGridLayout{ buttonsWidget };
	this->addButton = new QPushButton("Add");
	this->deleteButton = new QPushButton("Delete");
	this->updateButton = new QPushButton("Update");
	this->filterButton = new QPushButton("Filter");

	gridLayout->addWidget(addButton, 0, 0);
	gridLayout->addWidget(deleteButton, 0, 1);
	gridLayout->addWidget(updateButton, 0, 2);
	gridLayout->addWidget(filterButton, 0, 3);

	// add everything to the left layout
	leftSide->addWidget(new QLabel{ "All movies" });
	leftSide->addWidget(repoList);
	leftSide->addWidget(filmDataWidget);
	leftSide->addWidget(buttonsWidget);

	// middle component: just two button - to add the songs from the reposiotory to the playlist
	QWidget* middleWidget = new QWidget{};
	QVBoxLayout* vLayoutMiddle = new QVBoxLayout{ middleWidget };
	this->moveOneFilmButton = new QPushButton{ ">> Move one film" };
	this->moveAllFilmsButton = new QPushButton{ ">> Move all films" };
	QWidget* upperPart = new QWidget{};
	QWidget* lowerPart = new QWidget{};
	QVBoxLayout* vLayoutUpperPart = new QVBoxLayout{ upperPart };
	vLayoutUpperPart->addWidget(this->moveOneFilmButton);
	vLayoutUpperPart->addWidget(this->moveAllFilmsButton);
	vLayoutMiddle->addWidget(upperPart);
	vLayoutMiddle->addWidget(lowerPart);

	// right component: the playlist
	QWidget* rightWidget = new QWidget{};
	QVBoxLayout* rightSide = new QVBoxLayout{ rightWidget };

	// playlist
	watchList = new QListWidget{};

	// two buttons
	QWidget* watchlistButtonsWidget = new QWidget{};
	QHBoxLayout* watchlistButtonsLayout = new QHBoxLayout{ watchlistButtonsWidget };
	watchlistButtonsLayout->addWidget(new QPushButton{ "&Play" });
	watchlistButtonsLayout->addWidget(new QPushButton{ "&Next" });

	// add everything to the right layout
	rightSide->addWidget(new QLabel{ "Watchlist" });
	rightSide->addWidget(watchList);
	rightSide->addWidget(watchlistButtonsWidget);

	// add the three layouts to the main layout
	layout->addWidget(leftWidget);
	layout->addWidget(middleWidget);
	layout->addWidget(rightWidget);

	// connect the signals and slots
	this->connectSignalsAndSlots();
}

void WatchlistQt::connectSignalsAndSlots()
{
	// add a connection: function listItemChanged() will be called when an item in the list is selected
	QObject::connect(this->repoList, SIGNAL(itemSelectionChanged()), this, SLOT(listItemChanged()));

	// add button connections
	QObject::connect(this->addButton, SIGNAL(clicked()), this, SLOT(addFilm()));
	QObject::connect(this->deleteButton, SIGNAL(clicked()), this, SLOT(deleteFilm()));
	QObject::connect(this->updateButton, SIGNAL(clicked()), this, SLOT(updateFilm()));
	QObject::connect(this->filterButton, SIGNAL(clicked()), this, SLOT(filterRepoFilms()));

	QObject::connect(this->moveOneFilmButton, SIGNAL(clicked()), this, SLOT(moveFilmToWatchlist()));
	QObject::connect(this->moveAllFilmsButton, SIGNAL(clicked()), this, SLOT(moveAllFilms()));
}

void WatchlistQt::populateRepoList()
{
	// clear the list, if there are elements in it
	//if (this->repoList->count() > 0)
		//this->repoList->clear();
	this->repoList->clear();

	for (auto s : this->currentFilmInRepoList)
	{
		QString itemInList = QString::fromStdString(s.getTitle() + " - " + s.getGenre());
		this->repoList->addItem(itemInList);
	}

	// set the selection on the first item in the list
	//if (this->currentFilmInRepoList.size() > 0)
		//this->repoList->setCurrentRow(0);
}

void WatchlistQt::populateWatchlist()
{
	// clear the list, if there are elements in it
	if (this->watchList->count() > 0)
		this->watchList->clear();

	for (auto s : this->ctrl.getAllFilms())
	{
		QString itemInList = QString::fromStdString(s.getTitle() + " - " + s.getGenre());
		this->watchList->addItem(itemInList);
	}
}


int WatchlistQt::getRepoListSelectedIndex()
{
	if (this->repoList->count() == 0)
		return -1;

	// get selected index
	QModelIndexList index = this->repoList->selectionModel()->selectedIndexes();
	if (index.size() == 0)
	{
		this->titleEdit->clear();
		this->genreEdit->clear();
		this->durationEdit->clear();
		this->yearEdit->clear();
		this->likesEdit->clear();
		this->trailerEdit->clear();
		return -1;
	}

	int idx = index.at(0).row();
	return idx;
}

void WatchlistQt::listItemChanged()
{
	int idx = this->getRepoListSelectedIndex();
	if (idx == -1)
		return;

	std::vector<Film> films = this->currentFilmInRepoList;

	// get the song at the selected index
	if (idx > films.size())
		return;

	Film f = films[idx];

	this->titleEdit->setText(QString::fromStdString(f.getTitle()));
	this->genreEdit->setText(QString::fromStdString(f.getGenre()));
	this->yearEdit->setText(QString::number(f.getYear()));
    this->likesEdit->setText(QString::number(f.getLikes()));
	this->trailerEdit->setText(QString::fromStdString(f.getTrailer()));
	this->durationEdit->setText(QString::number(f.getDuration()));
}

void WatchlistQt::addFilm()
{
	std::string title = this->titleEdit->text().toStdString();
	std::string genre = this->genreEdit->text().toStdString();
	int year = this->yearEdit->text().toInt();
	int likes = this->likesEdit->text().toInt();
	int duration = this->durationEdit->text().toInt();
	
	if (duration == 0)
	{
		QMessageBox messageBox;
		messageBox.critical(0, "Error", "The duration must be different from 0! ");
		return;
	}

	std::string trailer= this->trailerEdit->text().toStdString();

	try
	{
		this->ctrl.addFilmToRepo(title, genre, year, 1998, trailer, duration);
		// refresh the list
		this->currentFilmInRepoList = this->ctrl.getAllFilms();
		this->populateRepoList();
	}
	catch (FilmException& e)
	{
		QMessageBox messageBox;
		messageBox.critical(0, "Error", "Eroare");
	}
	catch (DuplicateFilmException& e2)
	{
		QMessageBox messageBox;
		messageBox.critical(0, "Error", e2.what());
	}
}

void WatchlistQt::deleteFilm()
{
	std::string title = this->titleEdit->text().toStdString();
	
	try
	{
		this->ctrl.deleteFilm(title);
		// refresh the list
		this->currentFilmInRepoList = this->ctrl.getAllFilms();
		this->populateRepoList();
	}
	
	catch (InFilmException& er)
	{
		QMessageBox messageBox;
		messageBox.critical(0, "Error", er.what());
	}
	
}

void WatchlistQt::filterRepoFilms()
{
	std::string duration = this->durationEdit->text().toStdString();
	if (duration == "")
	{
		this->currentFilmInRepoList = this->ctrl.getAllFilms();
		this->populateRepoList();
		return;
	}

	this->currentFilmInRepoList = this->ctrl.filterByDuration(stoi(duration));
	this->populateRepoList();
}
void WatchlistQt::updateFilm()
{
	std::string title = this->titleEdit->text().toStdString();
	std::string genre = this->genreEdit->text().toStdString();
	int year = this->yearEdit->text().toInt();
	int likes = this->likesEdit->text().toInt();
	int duration = this->durationEdit->text().toInt();
	std::string trailer = this->trailerEdit->text().toStdString();

	this->ctrl.updateFilmController(title, genre, year, likes,trailer, duration);
	this->currentFilmInRepoList = this->ctrl.getAllFilms();
	this->populateRepoList();

}

void WatchlistQt::moveFilmToWatchlist()
{
	int idx = this->getRepoListSelectedIndex();
	if (idx == -1 || idx >= this->currentFilmInRepoList.size())
		return;

	const Film& f = this->currentFilmInRepoList[idx];
	this->ctrl.addFilmToWatchlist(f);
	this->populateWatchlist();
}

void WatchlistQt::moveAllFilms()
{
	for (auto f : this->currentFilmInRepoList)
	{
		this->ctrl.addFilmToWatchlist(f);
	}
	this->populateWatchlist();
}
