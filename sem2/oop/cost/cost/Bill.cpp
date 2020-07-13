#include "Bill.h"
#include "Utils.h"
#include <vector>

Bill::Bill()
{
}

Bill::Bill(const std::string & description, const int & duration, const int & priority)
	:description{ description }, duration{ duration }, priority{ priority }
{
}


Bill::~Bill()
{
}

bool Bill::operator<(const Bill & b)
{
	return this->priority < b.priority;
}

Bill & Bill::operator=(const Bill & b)
{
	if (this == &b)
		return *this;
	this->description = b.description;
	this->duration = b.duration;
	this->priority = b.priority;
	return *this;
}
std::istream &operator>>(std::istream & is, Bill & b)
{
	std::string line;
	getline(is, line);

	std::vector<std::string> tokens = tokenize(line, '|');
	if (tokens.size() != 3)
		return is;

	b.setDescription(tokens[0]);
	b.setDuration(std::stoi(tokens[1]));
	b.setPriority(std::stoi(tokens[2]));

	return is;

}