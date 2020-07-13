package ro.ubb.catalog.core.repository;


import ro.ubb.catalog.core.model.Person;

public interface PersonJpaRepository extends IRepository<Person, Long>, CustomPersonRepository{
}
