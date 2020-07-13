package ro.ubb.catalog.core.service;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import ro.ubb.catalog.core.model.Person;
import ro.ubb.catalog.core.repository.PersonJpaRepository;
import ro.ubb.catalog.core.repository.PersonRepository;

import java.util.List;
import java.util.Optional;
import java.util.Set;
import java.util.stream.Collectors;

@Service
public class PersonService {
    private static final Logger LOG = LoggerFactory.getLogger(PersonService.class);
    @Autowired
    private PersonRepository persons;


    public List<Person> getAllPersons(){
        LOG.trace("findAll --- method entered");

        List<Person> students = persons.findAll();

        LOG.trace("findAll: students={}", students);

        return students;
    }


    public Iterable<Person> findByName(String surname) {
        return persons.findByName(surname);
    }

    @Transactional
    public Set<Person> getUserByUsername(String username) {
        LOG.trace("getUserByUsername: username={}",username);

                long nr = persons.findAll()
                        .stream()
                        .filter(e -> e.getName().equals(username))
                        .count();

                if (nr!=0){
                    Set<Person> cuser = persons.findAll()
                            .stream()
                            .filter(e -> e.getName().equals(username))
                            .collect(Collectors.toSet());
                    return cuser;
                }else{
                    return null;
                }

    }

    public Person addPerson(String name, String ssn) {
        LOG.trace("addClient --- method entered - firstName {}, lastName {}", name, ssn);
        Person c = Person.builder()
                .name(name)
                .ssn(ssn)
                .build();
      //  Errors errors = new org.springframework.validation.BindException(c, "client");
        //clientValidator.validate(c, errors);
        c = persons.save(c);
        LOG.trace("addClient --- method exit client {}", c);
        return c;
    }

}
