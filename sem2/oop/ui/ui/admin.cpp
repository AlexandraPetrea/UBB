#include "admin.h"
#include "ui_admin.h"

#include <QString>
#include <cstring>
#include <ctime>
#include <QMessageBox>
#include"repositoryexception.h"

admin::admin(QWidget *parent) : QWidget(parent), ui(new Ui::admin)
{
	ui->setupUi(this);
}

admin::~admin()
{
	delete ui;
}

void admin::on_admin_add_clicked()
{
	// Adding a new film

	QString Qtitle = ui->admin_title->text();
	QString Qgenre = ui->admin_genre->text();
	QString Qyear = ui->admin_year->text();
	QString Qlikes = ui->admin_likes->text();
	QString Qtrailer = ui->admin_trailer->text();
	QString Qduration = ui->admin_duration->text();

	std::string title = Qtitle.toStdString();
	std::string genre = Qgenre.toStdString();
	std::string year = Qyear.toStdString();
	std::string likes = Qlikes.toStdString();
	std::string trailer = Qtrailer.toStdString();
	std::string duration = Qduration.toStdString();
	std::string message;
	try
	{
		message = this->controller.addFilm(title, genre, stoi(year), stoi(likes), trailer, stoi(duration));
	}
	catch (FilmException& e)
	{
		QMessageBox messageBox;
		messageBox.critical(0, "Error", "Eroare");
	}
	catch (DuplicateFilmException& e2)
	{
		QMessageBox messageBox;
		messageBox.critical(0, "Error", e2.what());
	}

	ui->admin_message_label->setText(QString::fromStdString(message));

}

void admin::on_admin_delete_clicked()
{
	// Remove a film from the repository
	QString Qfilm = ui->admin_delete_label->text();
	std::string film_id = Qfilm.toStdString();
	std::string message;

	try {
		message = this->controller.removeFilm(film_id);
	}
	catch (InFilmException& er)
	{
		QMessageBox messageBox;
		messageBox.critical(0, "Error", er.what());
	}
	ui->admin_message_label->setText(QString::fromStdString(message));
}

void admin::on_admin_update_clicked()
{
	// Update a film

	QString Qtitle = ui->admin_title->text();
	QString Qgenre = ui->admin_genre->text();
	QString Qyear = ui->admin_year->text();
	QString Qlikes = ui->admin_likes->text();
	QString Qtrailer = ui->admin_trailer->text();
	QString Qduration = ui->admin_duration->text();

	std::string title = Qtitle.toStdString();
	std::string genre = Qgenre.toStdString();
	std::string year = Qyear.toStdString();
	std::string likes = Qlikes.toStdString();
	std::string trailer = Qtrailer.toStdString();
	std::string duration = Qduration.toStdString();

	QString Qfilm = ui->admin_update_label->text();
	std::string film_id = Qfilm.toStdString();

	std::cout << film_id <<"\n";

	std::string message = this->controller.updateFilm(film_id, title, genre, stoi(year), stoi(likes), trailer, stoi(duration) );

	ui->admin_message_label->setText(QString::fromStdString(message));
}

void admin::on_admin_display_clicked()
{
	// Displays all the films from the repository

	const QString content = QString::fromStdString(this->controller.getFilms());

	ui->textEdit->setPlainText(content);
}

void admin::on_radioButton1_clicked()
{
	// Sorted
	std::vector <Film> d = this->controller.getFilmList();

	for (int i = 0; i < d.size(); i++) {
		for (int j = i + 1; j < d.size() - 1; j++) {
			if (d[i].getTitle() > d[j].getTitle()) {
				Film aux = d[i];
				d[i] = d[j];
				d[j] = aux;
			}
		}
	}

	std::string allFilms;

	for (int i = 0; i < d.size(); i++)
		allFilms += std::to_string(i + 1) + ". " + d[i].getTitle() + " | " + d[i].getGenre() + " | " + std::to_string(d[i].getYear()) + " | " + std::to_string(d[i].getLikes()) + " | " + std::to_string(d[i].getDuration()) + "\n";

	ui->textEdit->setPlainText(QString::fromStdString(allFilms));

}

void admin::on_radioButton_clicked()
{

	// Shuffled

	std::vector <Film> d = this->controller.getFilmList();

	srand(time(0));

	for (int i = 0; i < d.size(); i++) {
		int k = rand() % d.size();
		int l = rand() % d.size();
		Film aux = d[k];
		d[k] = d[l];
		d[l] = aux;
	}

	std::string allFilms;

	for (int i = 0; i < d.size(); i++)
		allFilms += std::to_string(i + 1) + ". " + d[i].getTitle() + " | " + d[i].getGenre() + " | " + std::to_string(d[i].getYear()) + " | " + std::to_string(d[i].getLikes()) + " | " + std::to_string(d[i].getDuration()) + "\n";

	ui->textEdit->setPlainText(QString::fromStdString(allFilms));

}