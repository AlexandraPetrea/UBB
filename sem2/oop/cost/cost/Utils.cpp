#include "Utils.h"
#include <sstream>
#include <string>
#include <vector>

std::vector<std::string> tokenize(const std::string &str, char delimiter)
{
	std::vector<std::string> result;
	std::stringstream ss(str);
	std::string token;
	while (std::getline(ss, token, delimiter))
		result.push_back(token);

	return result;
}