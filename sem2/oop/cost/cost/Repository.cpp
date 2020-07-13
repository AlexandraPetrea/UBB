#include "Repository.h"
#include <fstream>

Repository::Repository()
{
	this->readFile();
}


Repository::~Repository()
{
}

void Repository::readFile()
{
	std::ifstream file("Repo.txt");
	if (!file.is_open())
		throw (std::exception("Error opening file!"));

	Bill b{};
	while (file >> b)
	{
		this->bills.push_back(b);
	}
	file.close();
}
