#include "Film.h"
#include <Windows.h>
#include <shellapi.h>


Film::Film() : title(""), genre(""), year(0), likes(0), trailer(""), duration(0){}

Film::Film(const std::string& title, const std::string& genre, const int year, const int likes, const std::string& trailer, const int duration)
{
	this->title = title;
	this->genre = genre;
	this->year = year;
	this->likes = likes;
	this->trailer = trailer;
	this->duration = duration;
}


void Film::play()
{
	ShellExecuteA(NULL, NULL, "chrome.exe", this->getTrailer().c_str(), NULL, SW_SHOWMAXIMIZED);
}