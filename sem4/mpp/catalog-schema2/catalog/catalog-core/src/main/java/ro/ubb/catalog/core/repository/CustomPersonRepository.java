package ro.ubb.catalog.core.repository;

import ro.ubb.catalog.core.model.Person;

import java.util.List;

public interface CustomPersonRepository {
    List<Person> findAllPersonsNameContaining(String text);

    List<Person> getAll();
}
