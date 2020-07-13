#pragma once
#include "FileWatchList.h"
#include <string>

class CSVWatchList : public FileWatchList
{
public:
	void writeToFile() override;
	void displayWatchList() const override;
};
