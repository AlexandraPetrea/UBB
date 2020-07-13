#pragma once

#include "Repository.h"

class Controller
{
	Repository repo;
public:
	Controller();
	Controller(Repository &r);
	~Controller();

	std::vector<Bill> getListCont() { return this->repo.getBillsRepo(); }
	std::string get();

	int calculateDuration(const std::string priority);
	///desr: Computes the duration of the action having prioriy ''priority''
	///in: priority - string
	///out: the total duration (int)
	void testDuration();

};

