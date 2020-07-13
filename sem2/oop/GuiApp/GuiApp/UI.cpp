#include "UI.h"
#include <string>
#include "WatchList.h"
#include "WatchListFile.h"
#include "HTMLWatchList.h"
#include "filmValidator.h"
#include "RepositoryException.h"
#include <fstream>
#include <cassert>
using namespace std;

void UI::printMenu()
{
	cout << "1 - Admin mode(Manage film repository)" << "\n";
	cout << "2 - User mode(Manage WatchList)" << endl;
	cout << "0 - Exit" << "\n";
}

void UI::printRepositoryMenu()
{
	cout << "Please chose an option: " << "\n";
	cout << " 1 - Add a film." << "\n";
	cout << " 2 - Delete a film." << "\n";
	cout << " 3 - Update a film." << "\n";
	cout << " 4 - Display all." << "\n";
	cout << " 5 - Filter by duration." << "\n";
	cout << " 0 - Back." << "\n";
}

void UI::printWatchListMenu()
{
	cout << "Please chose a command: " << "\n";
	cout << " 1 - Add a film to Watchlist." << "\n";
	cout << " 2 - Display all the films with a given genre." << "\n";
	cout << " 3 - Delete the movie." << "\n";
	cout << " 4 - Display the WatchList." << "\n";
	cout << " 5 - Display the WatchList in a file." << "\n";
	cout << " 0 - Back." << "\n";
}

int getInt(string s)
{
	int x = 0;
	bool loop = true;
	while (loop)
	{
		std::cout << s; 
		std::string s;
		std::getline(std::cin, s);

		std::stringstream stream(s);
		if (stream >> x)
		{
			loop = false;
			continue;
		}
		std::cout << "Please try again, an int this time! " << std::endl;
	}
	return x;
}

string readGenre()
{
	std::string genre;
		cout << "Enter the genre: ";
		getline(cin, genre);
	return genre;
}

void UI::addFilmToRepoUI()
{
	cout << "Enter the title: ";
	std::string title;
	getline(cin, title);
	bool ok = false;
	std::string genre;
	genre = readGenre();
	int year = 0, likes = 0, duration = 0;
	year = getInt("Enter the year: ");
	likes = getInt("Enter the likes: ");
	cout << "Youtube link: ";
	std::string link;
	getline(cin, link);
	duration = getInt("Enter the duration: ");

	/*
	int result = this->ctrl.addFilmToRepo(title, genre, year, likes, link, duration);
	if (result == 1)
		cout << "\n Added succesful! \n";
	else
		cout << "\n Film already exist! \n";
	*/
	try
	{
		this->ctrl.addFilmToRepo(title, genre, year, likes, link, duration);
	//	cout << "\n Added succesful! \n";
	}
	catch (FilmException& e)
	{
		for (auto d : e.getErrors())
			cout << d;
	}

	catch (RepositoryException& e)
	{
		cout << e.what() << endl;
	}

	catch (FileException& e)
	{
		cout << e.what() << endl;

	}
}

void UI::deleteFilmUI()
{
	cout << "Enter the title: ";
	std::string title;
	getline(cin, title);
	try {
		this->ctrl.deleteFilm(title);
	}
	catch (RepositoryException& e)
	{
		cout << e.what() << endl;
	}
	//if (result == 1)
		//cout << "\n Deleted succesful! \n";
	//else
		//cout << "\n Film doesn't exist! \n";
	
}

void UI::updateFilmUI()
{
	cout << "Enter the title: ";
	std::string title;
	getline(cin, title);
	std::string new_genre;
	new_genre = readGenre();
	int new_year = 0, new_likes = 0, new_duration;
	new_year = getInt("Enter the new_year: ");
	new_likes = getInt("Enter the new_likes: ");
	cout << "Youtube link: ";
	std::string new_link;
	getline(cin, new_link);
	new_duration = getInt("Enter the new_duration: ");

	this->ctrl.updateFilmController(title, new_genre, new_year, new_likes, new_link, new_duration);
}
void UI::displayAllFilmsRepoUI()
{
	vector<Film> v = this->ctrl.getRepo().getFilms();
	if (v.size() == 0)
	{
		cout << "There are no films in the repository." << endl;
		return;
	}

	for(auto f : v)
	{ 
		cout << f.getTitle() << " - " << f.getGenre() << " - " << f.getYear() << "; " << f.getLikes() << ";" << f.getDuration() << "\n";
	}
}

void UI::filterByDuration()
{
	int duration;
	duration = getInt("Enter the duration: ");

	std::vector<Film> nou;
	nou = ctrl.filterByDuration(duration);

	for (auto f : nou)
	{
		cout << f.getTitle() << " - " << f.getGenre() << " - " << f.getYear() << "; " << f.getLikes() << ";" << f.getDuration() << "\n";
	}


	//if (ok == false)
		//cout << "There are no films with duration less than the one introduced. " << "\n";
}

void UI::addFilmByGenre()
{
	std::string genre;
	genre = readGenre();

	this->ctrl.addFilmByGenreToWatchlist(genre);

}

void UI::displayFilm()
{
	cout << "You want to select the genre or to see all the films?" << "\n";
	cout << " 1. See all the movies." << "\n";
	cout << " 2. Select the genre." << "\n";

	int opt{ 0 };
	cin >> opt;
	cin.ignore();
	switch (opt)
	{
	case 1:
	{
		vector<Film> films = this->ctrl.getRepo().getFilms();
		int i = 0;
		while (i < films.size())
		{
			Film f = films[i];
				cout << "\n" << f.getTitle() << "- " << f.getGenre() << "; " << f.getLikes() << "; " << f.getYear() << "\n";
				//f.play();

				cout << " 1 - Add a film to Watchlist." << "\n";
				cout << " 2 - Next." << "\n";
				cout << " 0  - Break." << "\n";
				int commandPlaylist{ 0 };
				cout << "Input the command: ";
				cin >> commandPlaylist;
				cin.ignore();
				if (commandPlaylist == 0)
				{
					break;
				}
				switch (commandPlaylist)
				{
				case 1:
					this->ctrl.addFilmToWatchlist(f);
					if (i == films.size() - 1)
						i = 0;
					else
						i++;
					break;
				case 2:
				{
					if (i == films.size() - 1)
						i = 0;
					else
						i++;
					break;
				}


				}
			}

			if (i == films.size() - 1)
				i = 0;
			else i = i + 1;
			break;
		}

	case 2:
	{
		std::string genre;
		genre = readGenre();

		vector<Film> films = this->ctrl.getRepo().getFilms();
		int i = 0;
		while (i < films.size())
		{
			Film f = films[i];
			if (f.getGenre() == genre)
			{
				cout << "\n" << f.getTitle() << "- " << f.getGenre() << "; " << f.getLikes() << "; " << f.getYear() << "\n";
				//f.play();

				cout << " 1 - Add a film to Watchlist." << "\n";
				cout << " 2 - Next." << "\n";
				cout << " 0  - Break." << "\n";
				int commandPlaylist{ 0 };
				cout << "Input the command: ";
				cin >> commandPlaylist;
				cin.ignore();
				if (commandPlaylist == 0)
				{
					break;
				}
				switch (commandPlaylist)
				{
				case 1:
					this->ctrl.addFilmToWatchlist(f);
					if (i == films.size() - 1)
						i = 0;
					else
						i++;
					break;
				case 2:
				{
					if (i == films.size() - 1)
						i = 0;
					else
						i++;
					break;
				}


				}
			}
			else
			{
				if (i == films.size() - 1)
					i = 0;
				else i = i + 1;
			}

		}

	}

	}

	


}

void UI::addFilmToWatchlist()
{
	cout << "Enter the title: ";
	std::string title;
	getline(cin, title);
	std::string genre;
	genre = readGenre();

	// search for the film in the repository
	Film f = this->ctrl.getRepo().findByTitleAndGenre(title, genre);
	if (f.getTitle() == "" && f.getGenre() == "")
	{
		cout << "There are no films with the given data in the repository. Nothing will be added to the watchlist." << endl;
		return;
	}

	this->ctrl.addFilmToWatchlist(f);
}
void UI::deleteFilmWatchList()
{
	cout << "Enter the title: ";
	std::string title;
	getline(cin, title);

	int pos= this->ctrl.getRepo().findByTitle(title);
	if (pos == -1)
	{
		cout << "There are no films with the given data in the repository. Nothing will be added to the watchlist." << endl;
		return;
	}

	cout << "Would you like to add a like to this film (yes/no): ";
	std::string ans;
	getline(cin, ans);
	if (ans == "yes")
	{
		Film f = this->ctrl.getRepo().getFilms()[pos];
		cout << " old likes:" << f.getLikes() << "\n";
		this->ctrl.updateFilmController(f.getTitle(), f.getGenre(), f.getYear(), f.getLikes()+1, f.getTrailer(), f.getDuration());
		f = this->ctrl.getRepo().getFilms()[pos];
		cout << " new likes:" << f.getLikes() << "\n";
	}
	pos = this->ctrl.getRepo().findByTitle(title);
	this->ctrl.deleteFilmToWatchlist(pos);
}

void UI::displayWatchListToFile()
{
	std::string filename;
	cout << "Input the file name (absolute path): ";
	getline(cin, filename);

	try
	{
		this->ctrl.saveWatchList(filename);

		if (this->ctrl.getWatchlist() == nullptr)
		{
			cout << "WatchList cannot be displayed!" << endl;
			return;
		}
		else
			this->ctrl.openWatchList();
	}
	catch (FileException& e)
	{
		cout << e.what() << endl;
	}
}

void UI::run()
{
	while (true)
	{
		UI::printMenu();
		int command{ 0 };
		cout << "Input the command: ";
		cin >> command;
		if (command == 0)
			break;

		// admin mode
		if (command == 1)
		{
			while (true)
			{
				UI::printRepositoryMenu();
				int commandRepo{ 0 };
				cout << "Please input the command: ";
				cin >> commandRepo;
				cin.ignore();
				if (commandRepo == 0)
					break;
				switch (commandRepo)
				{
				case 1:
					this->addFilmToRepoUI();
					break;
				case 2:
					this->deleteFilmUI();
					break;
				case 3:
					this->updateFilmUI();
					break;
				case 4:
					this->displayAllFilmsRepoUI();
					break;
				case 5:
					this->filterByDuration();
					break;
				}
			}
		}

		//user mode
		if (command == 2)
		{
			while (true)
			{
				UI::printWatchListMenu();
				int commandPlaylist{ 0 };
				cout << "Input the command: ";
				cin >> commandPlaylist;
				cin.ignore();
				if (commandPlaylist == 0)
					break;
				switch (commandPlaylist)
				{
				case 1:
					this->addFilmToWatchlist();
					break;
				case 2:
					this->displayFilm();
					break;
				case 3:
					if (this->ctrl.getWatchlist()->isEmpty())
					{
						cout << "Nothing to delete, the watchlist is empty." << "\n";
						continue;
					}
					this->deleteFilmWatchList();
					break;
				case 4:
				{
					if (this->ctrl.getWatchlist()->isEmpty())
					{
						cout << "Nothing to play, the watchlist is empty." << "\n";
						continue;
					}
					cout << "\n";
					for (int i = 0; i < ctrl.getWatchlist()->size(); i++)
					{
						this->ctrl.nextFilmWatchlist1();
						Film f = this->ctrl.getWatchlist()->getCurrentFilm();
						cout << f.getTitle() << " - " << f.getGenre() << "; " << f.getYear() << "; " << f.getLikes() << "\n";
					}
					cout << "\n";
					break;

				case 5:
					this->displayWatchListToFile();
					break;
				}	
				}
			}
		}
	}
}
			