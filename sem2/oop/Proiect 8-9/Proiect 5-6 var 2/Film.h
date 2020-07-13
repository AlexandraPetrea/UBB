#pragma once
#include <iostream>
class Film
{
public:
	std::string title;
	std::string genre;
	int year;
	int likes;
	std::string trailer;
	int duration;

public:
	// default constructor for a Film
	Film();

	// constructor with parameters
	Film(const std::string& title, const std::string& genre, const int year, const int likes, const std::string& trailer, const int duration);

	std::string getTitle() const 
		{ return title; }
	// return the title of a film
	std::string getGenre() const 
		{ return genre; }
	// return the genre of a film
	int getYear() const 
		{ return year; }
	// return the year of a film
	int getLikes() const 
		{ return likes; }
	int getDuration() const
		{ return duration;	}
	// return the no of likes of a film
	std::string getTrailer() const
		{ return trailer; }
	// return the trailer of a film

	std::string setTitle(const std::string& title1)
	{	// set a new title for a film
		this->title = title1;
		return title;
	}

	std::string setGenre(const std::string& genre1)
	{	// set a new genre for a film
		this->genre = genre1;
		return genre;
	}
	
	bool operator<(int dur)
	{
		if (duration < dur)
			return true;
		return false;
	}
	

	void play();
	static Film fromString(std::string obj);

	friend std::istream& operator>>(std::istream& is, Film& d);
	friend std::ostream& operator<<(std::ostream& os, const Film& d);
};

