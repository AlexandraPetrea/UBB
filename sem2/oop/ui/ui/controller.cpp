#include "controller.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

Controller::Controller() {}

std::string Controller::addFilm(const std::string& title, const std::string& genre, const int year, const int likes, const std::string& trailer, const int duration) {

	//if (title == "" || genre == "" || year == 0 || likes == 0 || trailer == "" || duration == 0) {
		//return "> All fields must be filled!";
	//}
	//else if (year != 0) {
	Film f = Film{title, genre, year, likes, trailer, duration};
		this->validator.validate(f);
		this->repo.addFilm(f);
		return "> Film successfully added!";
	//}
	//else {
		//return "> Invalid !";
	//}

}

std::vector <Film> Controller::getFilmList() {
	return this->repo.getFilms();
}

std::string Controller::getFilms() {
	std::vector <Film> filmList = this->repo.getFilms();
	std::string allFilms;

	for (int i = 0; i < filmList.size(); i++)
		allFilms += std::to_string(i + 1) + ". " + filmList[i].getTitle() + " | " + filmList[i].getGenre() + " | Year:  " + std::to_string(filmList[i].getYear()) + " | Likes:  " + std::to_string(filmList[i].getLikes()) + " | Duration: " + std::to_string(filmList[i].getDuration()) + " minutes \n";

	return allFilms;
}

std::string Controller::removeFilm(const std::string &film_id) {
	
		this->repo.removeFilm(film_id);
		return "> Film successfully removed!";

}

std::string Controller::updateFilm(const std::string& film_id, const std::string& title, const std::string& genre, const int year, const int likes, const std::string& trailer, const int duration)
{
	std::vector <Film> filmList = this->repo.getFilms();

		this->repo.updateFilm(film_id, Film{title, genre, year, likes, trailer, duration});
		return "> Film successfully updated!";


}

std::string Controller::filter(const int duration) {
	std::vector <Film> filmList = this->repo.getFilms();
	std::string allFilms;

	int k = 0;

	for (int i = 0; i < filmList.size(); i++)
		if (filmList[i].getDuration() <= duration)
			allFilms += std::to_string(++k) + ". " + filmList[i].getTitle() + " | " + filmList[i].getGenre() + " | " + std::to_string(filmList[i].getYear()) + " \n";

	if (allFilms == "")
		allFilms = "No results!";

	return allFilms;
}

std::string Controller::addToWatchList(const Film& f) {
	this->al.add(f);
	return "Added to WatchList!";
}

std::vector <Film> Controller::getWatchList() {
	return this->al.getWatchList();
}