#pragma once

#include <string>

class Bill
{
	std::string description;
	int duration;
	int priority;

public:
	Bill();
	Bill(const std::string &description, const int &duration, const int &priority);
	~Bill();

	bool operator<(const Bill &b);
	Bill &operator=(const Bill &b);

	std::string getDescription() const { return this->description; }
	int getDuration() const { return this->duration;}
	int getPriority() const { return this->priority; }
	
	void setDescription(const std::string &company) {
		this->description = company;
	}
	void setPriority(const int &priority) { this->priority = priority; }
	void setDuration(const int &duration) { this->duration = duration; }


	friend std::istream &operator>>(std::istream & is, Bill & c);
};