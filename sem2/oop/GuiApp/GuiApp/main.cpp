#include "GuiApp.h"
#include "CSV.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
	QApplication a(argc, argv);
	Repository repo{ "films.txt" };
	FileWatchList* watchlist = new CSVWatchList{};
	Controller ctrl{ repo, watchlist, FilmValidator{} };
	WatchlistQt w{ ctrl };
	w.show();
	return a.exec();
	delete watchlist;

	
}
