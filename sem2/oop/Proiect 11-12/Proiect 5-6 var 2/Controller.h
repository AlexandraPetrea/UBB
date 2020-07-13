#pragma once
#include "Repository.h"
#include "WatchList.h"
#include "filmValidator.h"
#include "FileWatchList.h"
class Controller
{
private:
	Repository repo;
	//WatchList watchList;
	FilmValidator validator;
	FileWatchList* watchList;

public:
	//Controller(const Repository& r) : repo{ r } {}
	//Controller();
	Controller(const Repository& r, FileWatchList* a, FilmValidator v) : repo{ r }, watchList{ a }, validator{ v } {}

	Repository getRepo() const 
	{ return repo; }
	WatchList* getWatchlist() const 
	{ return watchList; }

	int addFilmToRepo(const std::string& title, const std::string& genre, int year, int likes, const std::string& trailer, int duration);
	/*
	Adds a given film to the repo
	In: the attributes of a film - title, genre, year, likes, trailer
	Out: the film is added
	*/
	//void addSongToWatchlist(const Film & film);
	int deleteFilm(const std::string& title);
	/*
	Deletes a film given by title from repo
	In: the title of the film
	Out: the film is deleted
	*/
	void updateFilmController(const std::string& title, const std::string& genre, int year, int likes, const std::string& trailer, int duration);
	/*
	Updates a film from repo 
	In: the attributes of the new film 
	Out: the film is added*/

	void addFilmToWatchlist(const Film& film);
	void addFilmByGenreToWatchlist(const std::string& genre);
	void startWatchlist();
	void nextFilmWatchlist();
	void nextFilmWatchlist1();
	void deleteFilmToWatchlist(const int pos);
	void openWatchList() const;
	void saveWatchList(const std::string& filename);

};

