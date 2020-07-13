#include "WatchList.h"

#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;

class WatchListFile : public WatchList {
public:
	virtual void writeToFile() = 0;
	virtual void openFile() = 0;
};