#include "repositoryexception.h"

FileException::FileException(const std::string & msg) : message(msg)
{
}

const char * FileException::what()
{
	return message.c_str();
}

RepositoryException::RepositoryException() : exception{}, message{ "" }
{
}

RepositoryException::RepositoryException(const std::string & msg) : message{ msg }
{
}

const char * RepositoryException::what()
{
	return this->message.c_str();
}

const char * DuplicateFilmException::what()
{
	return "There is another film with the same title and genre!\n";
}

const char * InFilmException::what()
{
	return "Film doesn't exist!\n";
}