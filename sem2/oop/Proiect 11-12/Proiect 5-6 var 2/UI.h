#pragma once
#include <sstream>
#include "Controller.h"

class UI
{
private:
	Controller ctrl;

public:
	UI(const Controller& c) : ctrl(c) {}

	void run();

private:
	static void printMenu();
	//print the available modes
	static void printRepositoryMenu();
	//print the available commands for the administrator
	static void printWatchListMenu();
	//print the available commands for the user
	void addFilmToRepoUI();
		// adds a film using controller
	void deleteFilmUI();
		// deletes a film using controller
	void updateFilmUI();
		// updates a film using controller
	void addFilmByGenre();
	void displayFilm();
	void addFilmToWatchlist();
		//creates a watchlist 
	void displayAllFilmsRepoUI();
		//displays all the films from repo
	void deleteFilmWatchList();
	void filterByDuration();
	void listMovies();
	void displayWatchListToFile();
};

