#include "Repository.h"
#include <string>

using namespace std;

void Repository::addFilm(const Film& f)
{
	this->films.add(f);
}

void Repository::deleteFilm(const std::string& title)
{
	int pos = findByTitle(title);
	this->films.Delete(pos);
}

void Repository::updateFilm(const Film&f)
{
	string title;
	title = f.getTitle();
	int pos = findByTitle(title);
	this->films.update(pos, f);
}


Film Repository::findByTitleAndGenre(const std::string& title, const std::string& genre)
{
	Film* filmsInDynamicVector = this->films.getAllElems();
	if (filmsInDynamicVector != NULL)
		//return Film{};

	for (int i = 0; i < this->films.getSize(); i++)
	{
		Film f = filmsInDynamicVector[i];
		if (f.getGenre() == genre && f.getTitle() == title)
			return f;}

	return Film{};
}

int Repository::findByTitle(const std::string& title)
{
	Film* filmsInDynamicVector = this->films.getAllElems();
	if (filmsInDynamicVector != NULL)
		//return -1;

	for (int i = 0; i < this->films.getSize(); i++)
	{
		Film f = filmsInDynamicVector[i];
		if (f.getTitle() == title)
			return i;
	}

	return -1;
}

