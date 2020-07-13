#include "HTMLWatchList.h"
#include <fstream>
#include <Windows.h>
#include "RepositoryException.h"

using namespace std;

void HTMLWatchList::writeToFile()
{
	ofstream f(this->filename);
	if (!f.is_open())
		throw FileException("The file could not be opened!");
	f << "<!DOCTYPE html><html><body background ='a.jpg'><head><title>WatchList</title><h1> <center> WatchList </center> </h1> </head><body><table border=1><tr>";

	f << "<tr>" << "<td>" << "Title" << "</td>" << "<td>" << "Genre" << "<td>" << "Year" << "</td>" << "</td>" << "<td>" << "Likes" << "</td>" << "<td> " << "Youtube link" << "</td>" << "<td>" << "Duration" << "</td>" << "</tr>";
	for (auto d : this->films)
	{
		f << "<center>" << "<tr> "<< "<td>"<< d.getTitle() << "</td>" << "<td>" << d.getGenre() <<  "<td>" << d.getYear() << "</td>" << "</td>"<< "<td>" << d.getLikes() << "</td>" << "<td><a href =" << d.getTrailer() << ">Link</a></td>" << "<td>" << d.getDuration() << "</td>" << "</tr>" << "</center>";
	}
	f << "</table></body></html>";
	f.close();
}

void HTMLWatchList::displayWatchList() const
{
	string aux = "\"" + this->filename + "\""; // if the path contains spaces, we must put it inside quotations
	ShellExecuteA(NULL, NULL, "chrome.exe", aux.c_str(), NULL, SW_SHOWMAXIMIZED);
}