#ifndef ADOPTIONLIST_H
#define ADOPTIONLIST_H

#include "film.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>

class WatchList {
protected:
	std::vector <Film> watchList;
public:
	WatchList();

	std::vector <Film> getWatchList();
	void add(const Film& f);
};

#endif // ADOPTIONLIST_H