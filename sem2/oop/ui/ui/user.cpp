#include "user.h"
#include "ui_user.h"

#include <Windows.h>

User::User(QWidget *parent) : QWidget(parent), ui(new Ui::User)
{
	ui->setupUi(this);

	this->current = 1;

	std::vector <Film> d = this->controller.getFilmList();

	if (d.size() == 0) {
		ui->textEdit->setText(QString::fromStdString("No more films"));
		return;
	}

	ui->textEdit->setText(QString::fromStdString(d[this->current].convert()));

	//std::string command = "open " + d[this->current].getPhotograph();
	//system(command.c_str());

}

User::~User()
{
	delete ui;
}

void User::on_user_addW_clicked()
{
	std::vector <Film> d = this->controller.getFilmList();

	if (d.size() == 0) {
		ui->textEdit->setText(QString::fromStdString("No more films!"));
		return;
	}

	std::string message = this->controller.addToWatchList(d[this->current]);
	std::string message_aux = this->controller.removeFilm(std::to_string(this->current));

	this->current = (this->current + 1) % d.size();

	ui->textEdit->setText(QString::fromStdString(message));

}

void User::on_user_next_clicked()
{
	// next film 
	std::vector <Film> d = this->controller.getFilmList();

	if (d.size() == 0) {
		ui->textEdit->setText(QString::fromStdString("No more films"));
		return;
	}

	this->current = (this->current + 1) % d.size();

	ui->textEdit->setText(QString::fromStdString(d[this->current].convert()));

//	d[this->current].play();
	
}

void User::on_user_see_watch_list_clicked()
{
	// CSV
	std::ofstream f("watchlist.csv");

	std::vector <Film> list = this->controller.getWatchList();

	for (int i = 0; i < (int)list.size(); i++)
		f << std::to_string(i + 1) + ". " + list[i].getTitle() + " | " + list[i].getGenre() + " | Year:  " + std::to_string(list[i].getYear()) + " | Likes:  " + std::to_string(list[i].getLikes()) + " | Duration: " + std::to_string(list[i].getDuration()) + " minutes \n";

	f.close();

	std::string command = "open watchlist.csv";
	system(command.c_str());
	ShellExecuteA(NULL, NULL, "notepad.exe", "watchlist.csv", NULL, SW_SHOWMAXIMIZED);
}

void User::on_user_filter_clicked()
{
	QString Qage = ui->user_age->text();

	std::string duration = Qage.toStdString();

	std::string message = this->controller.filter(stoi(duration));

	ui->textEdit->setText(QString::fromStdString(message));

}

void User::on_see_watch_list_html_clicked()
{
	// HTML

	std::vector <Film> list = this->controller.getWatchList();

	std::ofstream f("watchlist.html");

	f << "<!DOCTYPE html><html><head><title>WatchList</title></head><body><table border=1>";

	for (int i = 0; i < (int)list.size(); i++)
		f << "<tr>" << "<td>" << list[i].getTitle() << "</td>" << "<td>" << list[i].getGenre() << "</td>" << "<td><a href =" << list[i].getTrailer() << ">Link</a></td>" << "</tr>";

	f << "</table></body></html>";

	f.close();

	//std::string command = "open watchlist.html";
	//system(command.c_str());
	ShellExecuteA(NULL, NULL, "chrome.exe", "watchlist.html", NULL, SW_SHOWMAXIMIZED);

}