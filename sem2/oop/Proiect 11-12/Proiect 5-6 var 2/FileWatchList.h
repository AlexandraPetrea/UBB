#pragma once
#include "WatchList.h"

class FileWatchList : public WatchList
{
protected:
	std::string filename;
public:
	FileWatchList();
	virtual ~FileWatchList() {}

	void setFileName(const std::string& filename);
	virtual void writeToFile() = 0;
	virtual void displayWatchList() const = 0;
};