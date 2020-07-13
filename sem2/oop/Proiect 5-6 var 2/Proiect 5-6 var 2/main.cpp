#include "Film.h"
#include "UI.h"
#include "Test.h"
#include <crtdbg.h>

using namespace std;

int main()
{
	{//system("color f2");
		Test test;
		test.test_everything();


		Repository repo{};

		Film f1{ "Home again", "romance", 2017, 211118, "https://www.youtube.com/watch?v=y-oFOgFB2uM&t",12 };
		Film f2{ "Everybody loves somebody", "romance", 2017, 20000, "https://www.youtube.com/watch?v=CQ6p9YQ4PuI",13};
		Film f3{ "Pearl Harbour", "drama", 2001, 20000, "https://www.youtube.com/watch?v=oGYcxjywx0o",14 };
		Film f4{ "Top Gun", "drama", 1986, 50000, "https://www.youtube.com/watch?v=xa_z57UatDY",15 };
		Film f5{ "La la land", "romance", 2016, 1278, "https://www.youtube.com/watch?v=0pdqf4P9MB8",15 };
		Film f6{ "Me before you", "romance", 2016, 22657, "https://www.youtube.com/watch?v=Eh993__rOxA",20 };
		Film f7{ "Girls trip", "comedy", 2017, 4845, "https://www.youtube.com/watch?v=7jE61BzKmgQ&t",25 };
		Film f8{ "Baywatch", "action", 2017, 11306, "https://www.youtube.com/watch?v=nZ5tqzw841s",15 };
		Film f9{ "Star Wars: The Force Awakens", "fantasy", 2015, 101207, "https://www.youtube.com/watch?v=sGbxmsDFVnE",19 };
		Film f10{ "Edge of tomorrow", "SF", 2014, 13764, "https://www.youtube.com/watch?v=vw61gCe2oqI",40 };
		repo.addFilm(f1);
		repo.addFilm(f2);
		repo.addFilm(f3);
		repo.addFilm(f4);
		repo.addFilm(f5);
		repo.addFilm(f6);
		repo.addFilm(f7);
		repo.addFilm(f8);
		repo.addFilm(f9);
		repo.addFilm(f10);
		Controller ctrl{ repo };
		UI ui{ ctrl };
		ui.run();
	}
	
	
	_CrtDumpMemoryLeaks();
	return 0;
}