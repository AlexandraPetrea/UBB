#include "Repository.h"
#include <string>
#include <fstream>
#include "RepositoryException.h"

using namespace std;

Repository::Repository(const std::string& fileName)
{
	this->fileName = fileName;
	this->loadFromFile();
}
void Repository::addFilm(const Film& f)
{
	int pos = this->findByTitle(f.getTitle());
	if (pos != -1)
		throw DuplicateFilmException();
	else {
		this->films.push_back(f);
		this->saveToFile();
	}
}

void Repository::deleteFilm(const std::string& title)
{
	int pos = findByTitle(title);
	if (pos == -1)
		throw InFilmException();
	else {
		this->films.erase(films.begin() + pos);
		this->saveToFile();
	}
	
}

void Repository::updateFilm(const Film&f)
{
	string title;
	title = f.getTitle();
	int pos = findByTitle(title);
	//this->films.update(pos, f);

	for (int i = 0; i < this->films.size(); i++)
	{
		Film f1 = films[i];
		if (f1.getTitle() == title)
			films[i] = f;
	}
	
	this->saveToFile();
}


Film Repository::findByTitleAndGenre(const std::string& title, const std::string& genre)
{
	//Film* filmsInDynamicVector = this->films.getAllElems();
	//if (filmsInDynamicVector != NULL)
		//return Film{};

	auto it = std::find_if(this->films.begin(), this->films.end(), [title, genre](Film f)
	{return f.getTitle() == title && f.getGenre() == genre; });
	if (it == this->films.end())
		return Film{};
	else return *it;

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
	/*
	for (int i = 0; i < this->films.size(); i++)
	{
		Film f = films[i];
		if (f.getTitle() == title)
			return i;
	}
	*/

	return -1;
}

void Repository::saveToFile() {
	ofstream fout(this->fileName.c_str());

	if (!fout.is_open())
		throw FileException("The file could not be open!");
	/*
	for (int i = 0; i < this->films.size(); ++i) {
		Film f = this->films[i];
		fout << f.getTitle() + "," +
			f.getGenre() + "," +
			to_string(f.getYear())+ "," +
			to_string(f.getLikes()) + "," +
			f.getTrailer() + "," + to_string(f.getDuration()) << '\n';
	}
	*/

	for (auto film : this->films)
	{
		fout << film;
	}

}

void Repository::loadFromFile() {

	ifstream fi(this->fileName);

	if (!fi.is_open())
		throw FileException("The file could not be open!");
	/*
	string line;
	while (getline(fi, line) && line != "") {
		Film aux = Film::fromString(line);
		this->addFilm(aux);
	}

	*/
	Film f;
	while (fi >> f)
		this->films.push_back(f);

	fi.close();
}