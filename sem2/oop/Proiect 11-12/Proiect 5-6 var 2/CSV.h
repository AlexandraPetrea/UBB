#pragma once
#include "FileWatchList.h"
#include <string>

class CSVWatchList : public FileWatchList
{
public:
	/*
	Writes the AdoptionList to file.
	Throws: FileException - if it cannot write.
	*/
	void writeToFile() override;

	/*
	Displays the AdoptionList using Microsoft Excel.
	*/
	void displayWatchList() const override;
};
