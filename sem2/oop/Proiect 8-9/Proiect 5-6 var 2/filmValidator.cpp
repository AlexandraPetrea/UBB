#include "FilmValidator.h"

using namespace std;

FilmException::FilmException(std::vector<std::string> _errors) : errors{ _errors }
{
}

std::vector<std::string> FilmException::getErrors() const
{
	return this->errors;
}

void FilmValidator::validate(const Film& f)
{
	vector<string> errors;
	string aux = f.getGenre();
	bool ok = false;
	if (aux == "romance" or aux == "action" or aux == "SF" or aux == "drama" or aux == "comedy" or aux == "history")
		ok = true;
	if(ok == false)
		errors.push_back("The only valid genre are romance, action, SF, drama, comedy or history.\n");
	if (!isupper(f.getTitle()[0]))
		errors.push_back(string("The title of the film must start with a capital letter!\n"));
	if (f.getYear() == 0)
		errors.push_back(string("The year cannot be 0!\n"));

	if(f.getLikes() != int(f.getLikes()))
		errors.push_back(string("This must be an integer!\n"));

	// search for "www" or "http" at the beginning of the trailer string
	
	
	int posWww = f.getTrailer().find("www");
	int posHttp = f.getTrailer().find("http");
	if (posWww != 0 && posHttp != 0)
		errors.push_back("The youtube source must start with one of the following strings: \"www\" or \"http\" \n");
	
	if (errors.size() > 0)
		throw FilmException(errors);
}