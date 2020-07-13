#pragma once
#include "FileWatchList.h"

#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

class HTMLWatchList: public FileWatchList {
public:
	void writeToFile() override;
	void displayWatchList() const override;
};