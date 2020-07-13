#ifndef LMDB_UTIL_H
#define LMDB_UTIL_H

#include <string>
#include <vector>
#include "film.h"

using namespace std;

/*
Function that simulates strip and split by commas.
*/
string* splitString(string temp);

/*
Compare function between two movie entity genres.
*/
bool genreBool(Film a, Film b);

/*
Function that gets a list of movies and returns a sorted one by genre.
*/
vector<Film> sortByGenre(vector<Film> items);

#endif //LMDB_UTIL_H