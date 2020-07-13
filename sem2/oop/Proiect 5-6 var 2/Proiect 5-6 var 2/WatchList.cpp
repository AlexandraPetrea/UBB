#include "WatchList.h"


WatchList::WatchList()
{
	this->current = 0;
}

void WatchList::add(const Film& film)
{
	this->films.add(film);
}

void WatchList::Delete(int pos)
{
	this->films.Delete(pos);
}

Film WatchList::getCurrentFilm()
{
	if (this->current == this->films.getSize())
		this->current = 0;
	return this->films[this->current];
}

int WatchList::play()
{
	if (this->films.getSize() == 0)
		return 0;
	this->current = 0;
	Film currentFilm = this->getCurrentFilm();
	currentFilm.play();
	return 1;
}

int WatchList::next()
{
	if (this->films.getSize() == 0)
		return 0;
	this->current++;
	Film currentFilm = this->getCurrentFilm();
	currentFilm.play();
	return 1;
}
int WatchList::next1()
{
	if (this->films.getSize() == 0)
		return 0;
	this->current++;
	Film currentFilm = this->getCurrentFilm();
	return 1;
}

bool WatchList::isEmpty()
{
	return this->films.getSize() == 0;
}

int WatchList::size()
{
	return this->films.getSize();
}