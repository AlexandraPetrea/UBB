#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>
#include "repository.h"
#include"repositoryexception.h"


Repository::Repository() {
	this->filename = "a.txt";
	this->readFromFile();
}

void Repository::addFilm(const Film&f) {
	int pos = this->findByTitle(f.getTitle());
	if (pos != -1)
	{
		throw DuplicateFilmException();
	}
	this->films.push_back(f);
	this->writeToFile();
}

void Repository::removeFilm(const std::string &film_id) {
	
	if (atoi(film_id.c_str()) >= 1 && atoi(film_id.c_str()) <= films.size())
	{
		this->films.erase(this->films.begin() + atoi(film_id.c_str()) - 1);
		this->writeToFile();
	}
	else 
		throw InFilmException();
}

void Repository::updateFilm(const std::string &film_id, const Film &f) {
	this->films[atoi(film_id.c_str()) - 1] = f;
	this->writeToFile();
}

std::vector <Film> Repository::getFilms() {
	return this->films;
}

void Repository::readFromFile()
{
	std::ifstream fi;
	fi.open("a.txt");
	std::string breed, name, photograph;
	int age;

	Film f;
	while (fi >> f)
		this->films.push_back(f);

	fi.close();
}

void Repository::writeToFile()
{
	std::ofstream fo;
	fo.open("a.txt");

	for (auto d : this->films)
		fo << d;
	fo.close();
}

int Repository::findByTitle(const std::string& title)
{
	int i = 0;
	for (auto film : this->films)
	{
		if (film.getTitle() == title)
			return i;
		else
			i = i + 1;
	}

	return -1;
}