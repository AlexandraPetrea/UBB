package ro.ubb.catalog.web.converter;

import org.springframework.stereotype.Component;
import ro.ubb.catalog.core.model.Person;
import ro.ubb.catalog.web.dto.PersonDto;

@Component
public class PersonConverter extends BaseConverter<Person, PersonDto> {

    @Override
    public Person convertDtoToModel(PersonDto personDto) {
        throw new RuntimeException("Not yet implemented!");
    }

    @Override
    public PersonDto convertModelToDto(Person client) {
        PersonDto clientDto = PersonDto.builder()
                .name(client.getName())
                .ssn(client.getSsn())
                .build();
        clientDto.setId(client.getId());
        return clientDto;
    }
}
