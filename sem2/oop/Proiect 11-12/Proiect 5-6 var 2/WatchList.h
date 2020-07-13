#pragma once
//#include "DynamicVector.h"
#include <vector>
#include "Film.h"

class WatchList
{
protected:
	//DynamicVector<Film> films;
	std::vector<Film> films;
	int current;

public:
	WatchList();

	// Adds a film to the watchlist.
	void add(const Film& film);
	void Delete(int pos);

	// Returns the film that is currently playing.
	Film getCurrentFilm();

	// Starts the watchlist - plays the first trailer.
	int play();

	// Plays the next trailer in the watchlist.
	int next();
	int next1();

	// Checks if the watchlist is empty.
	bool isEmpty();
	int size();
};