#pragma once
#include <iostream>
#include <vector>

#include "film.h"

class Repository {
protected:
	std::vector <Film> films;
	std::string filename;

public:
	Repository();

	void addFilm(const Film& f);
	void removeFilm(const std::string& film_id);
	void updateFilm(const std::string& film_id, const Film& f);
	std::vector <Film> getFilms();
	int findByTitle(const std::string& title);

private:
	void readFromFile();
	void writeToFile();
};

