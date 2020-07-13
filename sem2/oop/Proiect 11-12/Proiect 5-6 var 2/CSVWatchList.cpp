#include "CSV.h"
#include <fstream>
#include <Windows.h>
#include "RepositoryException.h"

using namespace std;

void CSVWatchList::writeToFile()
{
	ofstream f(this->filename);

	if (!f.is_open())
		throw FileException("The file could not be opened!");

	for (auto d : this->films)
		f << d;

	f.close();
}

void CSVWatchList::displayWatchList() const
{
	string aux = "\"" + this->filename + "\""; // if the path contains spaces, we must put it inside quotations
	ShellExecuteA(NULL, NULL, "notepad.exe", aux.c_str(), NULL, SW_SHOWMAXIMIZED);
}