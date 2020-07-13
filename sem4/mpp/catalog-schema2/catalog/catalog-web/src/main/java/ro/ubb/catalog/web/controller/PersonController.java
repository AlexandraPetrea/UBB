package ro.ubb.catalog.web.controller;

import org.apache.catalina.connector.Response;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import ro.ubb.catalog.core.model.Person;
import ro.ubb.catalog.core.service.PersonService;
import ro.ubb.catalog.web.converter.PersonConverter;
import ro.ubb.catalog.web.dto.PersonDto;
import ro.ubb.catalog.web.dto.PersonsDto;

import javax.validation.Valid;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.concurrent.ExecutionException;
@RestController
@RequestMapping(value = "/api")
public class PersonController {
    private static final Logger log =  LoggerFactory.getLogger(PersonController.class);

    @Autowired
    private PersonService personService;

    @Autowired
    private PersonConverter personConverter;

    @RequestMapping(value = "/persons", method = RequestMethod.GET)
    public List<PersonDto> getPersons() {
        log.trace("getStudents");

        List<Person> students = personService.getAllPersons();

        log.trace("getStudents: students={}", students);

        return new ArrayList<>(personConverter.convertModelsToDtos(students));
    }

    @RequestMapping(value = "/persons/search", method = RequestMethod.GET)
    public String getByName(@RequestParam(value = "surname", required = false) String surname, Model model) {
        model.addAttribute("search", personService.findByName(surname));
        return "students";
    }

    @RequestMapping(value="/persons/{username}",method= RequestMethod.GET)
    Set<PersonDto> getUserByUsername(@PathVariable String username) throws ExecutionException, InterruptedException {
        log.trace("getUserByUsername for username: {}",username);
        Set<Person> user=this.personService.getUserByUsername(username);
        Set<PersonDto> result = personConverter.convertModelsToDtos(user);
        log.trace("getUserByUsername in controller left");
        return result;
    }

    @RequestMapping(value = "/persons", method = RequestMethod.POST)
    public PersonDto createPerson(
            @RequestBody final PersonDto personDto
    ) {
        log.trace("createClient: clientDtoMap={}", personDto);

        Person client = personService.addPerson(
              personDto.getName(),
                personDto.getSsn()
        );
        //Person client = personService.addPerson("alexandra", "121");

        PersonDto result = personConverter.convertModelToDto(client);

        log.trace("createClient: result={}", result);
        return result;
    }
}
