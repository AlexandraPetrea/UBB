#include "Controller.h"
#include <algorithm>
#include <vector>
#include <iterator>
#include <string>

using namespace std;
int Controller::addFilmToRepo(const std::string& title, const std::string& genre, int year, int likes, const std::string& trailer, int duration)
{
	Film f{ title, genre, year, likes, trailer, duration};
	int pos = this->repo.findByTitle(title);
	if (pos == -1)
	{
		this->repo.addFilm(f);
		return 1;
	}
	return -1;
}
int Controller::deleteFilm(const std::string& title)
{
	int pos = this->repo.findByTitle(title);
	if (pos != -1)
	{
		this->repo.deleteFilm(title);
		return 1;
	}
	return pos;
}

void Controller::updateFilmController(const std::string& title, const std::string& genre, int year, int likes, const std::string& trailer, int duration)
{
	Film f{ title, genre, year, likes, trailer, duration};
	this->repo.updateFilm(f);
}

void Controller::addFilmToWatchlist(const Film& film)
{
	int aux = watchList.size();
	if(aux == 0)
		this->watchList.add(film);
	else {
		bool ok = true;
		while (aux != 0)
		{
			Film f = watchList.getCurrentFilm();
			if (f.getTitle() == film.getTitle())
				ok = false;
			watchList.next1();
			aux = aux - 1;
		}
		if (ok == true)
			this->watchList.add(film);
		else
			return;
	}
	
} 
void Controller::deleteFilmToWatchlist(int pos)
{
	this->watchList.Delete(pos);
}
void Controller::startWatchlist()
{
	this->watchList.play();
}

void Controller::nextFilmWatchlist()
{
	this->watchList.next();
}

void Controller::nextFilmWatchlist1()
{
	this->watchList.next1();
}

void Controller::addFilmByGenreToWatchlist(const std::string& genre)
{
	// get all the films from the repository
	DynamicVector<Film> films = this->repo.getFilms();
	
	for (int i = 0; i < films.getSize(); i++)
	{
	Film f = films[i];
	if (f.getGenre() == genre)
	this->watchList.add(f);
	}
}