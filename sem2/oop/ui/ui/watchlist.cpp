#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>

#include "watchlist.h"

WatchList::WatchList() {}

std::vector <Film> WatchList::getWatchList() {
	return this->watchList;
}

void WatchList::add(const Film& f) {
	this->watchList.push_back(f);
}