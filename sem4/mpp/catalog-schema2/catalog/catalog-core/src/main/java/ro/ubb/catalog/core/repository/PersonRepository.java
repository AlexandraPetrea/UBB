package ro.ubb.catalog.core.repository;

import ro.ubb.catalog.core.model.Person;

import java.util.List;

public interface PersonRepository extends CatalogRepository<Person, Long> {
    Iterable<Person> findByName(String lastname);
}

