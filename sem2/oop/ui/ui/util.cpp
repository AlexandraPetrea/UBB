#include "util.h"
#include <sstream>
#include<algorithm>

using namespace std;

bool genreBool(Film a, Film b) { return a.getGenre() > b.getGenre(); }

vector<Film> sortByGenre(vector<Film> items)
{
	sort(items.begin(), items.end(), genreBool);
	return items;
}