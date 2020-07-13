#include "Test.h"
#include "Film.h"
#include "Repository.h"
#include "Controller.h"
#include <iostream>
#include <cassert>
#include <string>
#include <fstream>

using namespace std;
/*
void Test::test_film() {
	Film* f = new Film("A", "romance", 2010, 10, "www.no",10);
	assert(f->getTitle()== "A");
	assert(f->getGenre() == "romance");
	assert(f->getYear() == 2010);
	assert(f->getLikes() == 10);
	assert(f->getTrailer() == "www.no");
	assert(f->getDuration() == 10);
	vector<Film> v;
	Film f1("A", "romance", 1, 1, "www.d", 20);
	v = v;
	assert((f1 < 15) == 0);
	assert((f1 < 25) == 1);

	v.push_back(f1);
	//v = v + f1;
	
	assert(v.size() == 1);
	assert(v[0].getTitle() == "A");
	assert(v[0].getGenre() == "romance");
	assert(v[0].getLikes() == 1);

	Film f2("B", "SF", 2, 2, "www.a",20);
//	v = f2 + v;
	v.push_back(f2);
	assert(v.size() == 2);
	assert(v[1].getTitle() == "B");
	assert(v[1].getGenre() == "SF");
	assert(v[1].getTrailer() == "www.a");
	/*
	for (int i = 1; i <= 10; i++)
		v = v + f2;
	assert(v.getSize() == 12);
	*/
/*
	for (int i = 1; i <= 10; i++)
		v.push_back(f2);
	assert(v.size() == 12);


	delete(f);
	
}
*/
/*

void Test::test_repository() {
	
	Repository repo = {"a.txt"};

	vector<Film> v;
	vector <Film> AUX;
	AUX = repo.getFilms();

	Film* doi = AUX.data();
//	assert(doi.getTitle() == "");
	assert(repo.findByTitle("A") == -1);
	assert(repo.findByTitle("Home") == -1);
	
	Film film = repo.findByTitleAndGenre("Home", "romance");
	assert(film.getTitle() == "");
	assert(film.getTrailer() == "");
	assert(film.getYear() == 0);
	assert(film.getLikes() == 0);
	assert(film.getGenre() == "");
	
	//Film f1{ "Home again", "romance", 2017, 211118, "https://www.youtube.com/watch?v=y-oFOgFB2uM&t",10 };
	//Film f2{ "Everybody loves somebody", "romance", 2017, 20000, "https://www.youtube.com/watch?v=CQ6p9YQ4PuI",10 };
	

	//repo.addFilm(f1);
	v = repo.getFilms();
	//assert(v.size() == 2); 
	//repo.addFilm(f2);
	v = repo.getFilms();
	//assert(v.size() == 3);
	Film* films= v.data();
	assert(films[0].getTitle() == "Home again");
	assert(films[1].getTitle() == "Everybody loves somebody");

	int aux = repo.findByTitle("Home again");
	assert(aux == 0);
	aux = repo.findByTitle("Everybody loves somebody");
	assert(aux == 1);

	Film aici = repo.findByTitleAndGenre("Home again", "romance");
	assert(aici.getTitle() == "Home again");
	assert(aici.getYear() == 2017);

	repo.deleteFilm("Home again");
	v = repo.getFilms();
	films = v.data();
	assert(v.size() == 1);
	assert(films[0].getTitle() == "Everybody loves somebody");
	Film f3("Everybody loves somebody", "action", 2018, 10, "www.a",10);
	repo.updateFilm(f3);
	v = repo.getFilms();
	films = v.data();

	assert(films[0].getGenre() == "action");
	assert(films[0].getLikes() == 10);
	assert(films[0].getYear() == 2018);
	assert(films[0].getTrailer() == "www.a");

	//for(int i = 1; i <= 10; i++)
		//repo.addFilm(f1);
	//v = repo.getFilms();
	//assert(v.size() == 11);


	
}

void Test::test_controller() {
	
	Repository repo{};
	WatchList watchlist{};
	Controller ctrl{ repo };

	vector<Film> v = ctrl.getRepo().getFilms();

	assert(v.size() == 0);
	assert(ctrl.deleteFilm("Home again") != 1);

	ctrl.addFilmToRepo("Home again", "romance", 2017, 211118, "https://www.youtube.com/watch?v=y-oFOgFB2uM&t",10);
	ctrl.addFilmToRepo("Everybody loves somebody", "romance", 2017, 20000, "https://www.youtube.com/watch?v=CQ6p9YQ4PuI",10);

	v = ctrl.getRepo().getFilms();
	Film* films = v.data();
	
	assert(ctrl.addFilmToRepo("Home again", "romance", 2017, 211118, "https://www.youtube.com/watch?v=y-oFOgFB2uM&t",10) == -1);
	assert(v.size() == 2);
	assert(films[0].getTitle() == "Home again");
	assert(films[0].getLikes() == 211118);

	assert(ctrl.addFilmToRepo("A", "romance", 1, 1, "www.a",1) == 1);
	assert(films[1].getGenre() == "romance");
	assert(films[1].getTrailer() == "https://www.youtube.com/watch?v=CQ6p9YQ4PuI");

	ctrl.deleteFilm("Home again");
	v = ctrl.getRepo().getFilms();
	films = v.data();

	ctrl.addFilmToRepo("A", "romance", 2000, 120, "www.no",10);
	assert(films[0].getTitle() == "Everybody loves somebody");

	ctrl.updateFilmController("Everybody loves somebody", "r", 2, 2, "www.no",10);
	v = ctrl.getRepo().getFilms();
	films = v.data();
	assert(films[0].getGenre() == "r");
	assert(films[1].getGenre() == "romance");
	assert(films[1].getTitle() == "A");
	ctrl.deleteFilm("A");

	v = ctrl.getRepo().getFilms();
	films = v.data();
	assert(films[0].getTitle() == "Everybody loves somebody");

	//Test for controller watchList
	Film f1{ "Home again", "romance", 2017, 211118, "https://www.youtube.com/watch?v=y-oFOgFB2uM&t",10 };
	Film f2{ "Everybody loves somebody", "romance", 2017, 20000, "https://www.youtube.com/watch?v=CQ6p9YQ4PuI",10 };
	assert(ctrl.getWatchlist().play() == 0);
	assert(ctrl.getWatchlist().next1() == 0);
	assert(ctrl.getWatchlist().next() == 0);
	
	assert(ctrl.getWatchlist().isEmpty() == 1);
	ctrl.addFilmToWatchlist(f1);
	ctrl.addFilmToWatchlist(f1);
	
	assert(ctrl.getWatchlist().size() == 1);
	assert(ctrl.getWatchlist().getCurrentFilm().getTitle() == "Home again");
	//ctrl.startWatchlist();
	ctrl.addFilmToWatchlist(f2);
	ctrl.nextFilmWatchlist1();
	assert(ctrl.getWatchlist().getCurrentFilm().getTitle() == "Everybody loves somebody");
	
	//ctrl.nextFilmWatchlist();
	//assert(ctrl.getWatchlist().getCurrentFilm().getTitle() == "Home again");
	//ctrl.getWatchlist().play();

	ctrl.deleteFilmToWatchlist(1);
	assert(ctrl.getWatchlist().size() == 1);
	ctrl.deleteFilmToWatchlist(1);
	assert(ctrl.getWatchlist().size() == 0);
	ctrl.addFilmByGenreToWatchlist("r");
	assert(ctrl.getWatchlist().size() == 1);
	
//	ctrl.saveToFile("a.txt");
	ifstream fi("a.txt");
	string line;
	getline(fi, line);
	Film aux = Film::fromString(line);
	ctrl.addFilmToRepo(aux.getTitle(), aux.getGenre(), aux.getYear(), aux.getLikes(), aux.getTrailer(), aux.getDuration());

	v = ctrl.getRepo().getFilms();
	films = v.data();

	assert(films[0].getTitle() == "Everybody loves somebody");
	
}
*/

void Test::test_everything() {
	//this->test_film();
//	this->test_repository();
	//this->test_controller();
}