#include"film.h"
#include <Windows.h>
#include <shellapi.h>
#include <vector>
#include <string>
#include <sstream>
using namespace std;


Film::Film() : title(""), genre(""), year(0), likes(0), trailer(""), duration(0) {}

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

Film Film::fromString(string obj) {
	vector <string> aux;
	aux.push_back("");
	for (int i = 0; i < obj.size(); ++i) {
		if (obj[i] == ',')
			aux.push_back("");
		else
			aux.back() += obj[i];
	}
	return Film(aux[0], aux[1], stoi(aux[2]), stoi(aux[3]), aux[4], stoi(aux[5]));
}


ostream & operator <<(ostream & os, Film & f)
{
	//os << f;
	os << f.getTitle() << "," << f.getGenre() << "," << f.getYear() << "," << f.getLikes() << "," << f.getTrailer() << "," << f.getDuration() << "\n";
	return os;
}

vector<string> tokenize(const string& str, char delimiter)
{
	vector<string> result;
	stringstream ss(str);
	string(token);
	while (getline(ss, token, delimiter))
		result.push_back(token);
	return result;
}
istream & operator >> (istream & is, Film & f)
{
	string line;
	getline(is, line);

	vector<string> tokens = tokenize(line, ',');
	if (tokens.size() != 6)
		//cout << tokens[0];
		return is;

	f.title = tokens[0];
	f.genre = tokens[1];
	f.year = stoi(tokens[2]);
	f.likes = stoi(tokens[3]);
	f.trailer = tokens[4];
	f.duration = stoi(tokens[5]);
	return is;
}

std::string Film::convert() {
	std::ostringstream output;

	output << "Title " << this->title;
	output << "\nGenre: " << this->genre;
	output << "\nYear: " << this->year;
	output << "\nLikes: " << this->likes;
	output << "\nTrailer: " << this->trailer;
	output << "\nDuration: " << this->duration << "\n";

	return output.str();
}

bool Film::operator==(const Film& anotherFilm) {
	return this->getGenre() == anotherFilm.genre && this->getTitle() == anotherFilm.title;
}