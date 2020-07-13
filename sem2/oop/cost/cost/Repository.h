#pragma once

#include "Bill.h"
#include <vector>
#include"Utils.h"

class Repository
{
	std::vector<Bill> bills;

public:
	Repository();
	~Repository();

	void readFile();
	std::vector<Bill> getBillsRepo() const { return this->bills; }
};
