#pragma once
#include "Film.h"
#include <vector>
#include <iterator>
#include <algorithm>

class Repository
{
private:
	std::vector<Film> films;
	std::string fileName;

public:
	/*
	Default constructor
	Initializes an object of type repository
	*/
	Repository() {}

	Repository(const std::string& fileName);
	void addFilm(const Film& f);
	/*
	Adds a film to the repository
	In: f - Film
	Out: the film is added to the repository
	*/

	void deleteFilm(const std::string& title);
	/*
	Deletes a film, by title
	In: title- string
	Output: the film is deleted
	*/

	void updateFilm(const Film&f);
	/*
	Updates a film
	In: f - Film
	Out: the film is updated with the new attributes
	*/
	Film findByTitleAndGenre(const std::string& title, const std::string& genre);
	/*
	Finds a film, by title and genre
	In: title, genre - string
	Out: the film that was found, or an "empty" film (all fields empty, year and likes are 0), if nothing was found.
	*/

	int findByTitle(const std::string& title);
	/*
	Finds a film, by title
	In: title, genre - string
	Out: the position in the repo if the film was found, or -1 if nothing was found.
	*/
	std::vector<Film> getFilms() const 
	{ return films; }
	//return all the films 
private:
	void saveToFile();
	void loadFromFile();

};