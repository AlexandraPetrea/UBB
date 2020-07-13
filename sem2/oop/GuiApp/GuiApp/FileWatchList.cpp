#include "FileWatchList.h"

FileWatchList::FileWatchList() :WatchList{}, filename{ "" }
{
}

void FileWatchList::setFileName(const std::string& filename)
{
	this->filename = filename;
}