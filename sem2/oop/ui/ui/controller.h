#ifndef CONTROLLER_H
#define CONTROLLER_H

#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>

#include "repository.h"
#include "watchlist.h"
#include"filmValidator.h"

class Controller {
protected:
	Repository repo;
	FilmValidator validator;
	WatchList al;

public:
	Controller();

	std::string addFilm(const std::string& title, const std::string& genre, const int year, const int likes, const std::string& trailer, const int duration);
	std::string removeFilm(const std::string& film_id);
	std::string updateFilm(const std::string& film_id, const std::string& title, const std::string& genre, const int year, const int likes, const std::string& trailer, const int duration);

	std::string addToWatchList(const Film& f);
	std::string filter(const int duration);

	std::string getFilms();
	std::vector <Film> getFilmList();
	std::vector <Film> getWatchList();
};

#endif // CONTROLLER_H