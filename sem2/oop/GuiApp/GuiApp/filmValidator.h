#pragma once
#include <string>
#include "Film.h"
#include <vector>

class FilmException
{
private:
	std::vector<std::string> errors;

public:
	FilmException(std::vector<std::string> _errors);
	std::vector<std::string> getErrors() const;
};

class FilmValidator
{
public:
	FilmValidator() {}
	static void validate(const Film& f);
};