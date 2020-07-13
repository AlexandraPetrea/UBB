#include "Controller.h"
#include <assert.h>

Controller::Controller()
{
}

Controller::Controller(Repository & r)
	:repo{ r }
{
}


Controller::~Controller()
{
}

int Controller::calculateDuration(const std::string priority)
{
	int sum = 0;
	for (auto p : this->getListCont())
	{
		if (p.getPriority() == stoi(priority))
			sum += p.getDuration();
	}
	return sum;
}
void Controller::testDuration()
{
	std::string description{ "solve_oop" };
	assert(int(this->calculateDuration(description)) == 120);
	assert(int(this->calculateDuration("alt")) == 0);
}
std::string Controller::get() {
	std::vector <Bill> List = this->repo.getBillsRepo();
	std::string allFilms;

	for (int i = 0; i < List.size(); i++)
		allFilms += std::to_string(i + 1) + ". " + List[i].getDescription()  + " " + std::to_string(List[i].getPriority()) + "\n";
	return allFilms;
}
