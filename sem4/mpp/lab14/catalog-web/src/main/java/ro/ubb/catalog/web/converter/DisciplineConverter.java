package ro.ubb.catalog.web.converter;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;
import ro.ubb.catalog.core.model.Discipline;
import ro.ubb.catalog.web.dto.DisciplineDto;

/**
 * Created by radu.
 */

@Component
public class DisciplineConverter extends BaseConverter<Discipline, DisciplineDto> {

    private static final Logger log = LoggerFactory.getLogger(DisciplineConverter.class);

    @Override
    public DisciplineDto convertModelToDto(Discipline discipline) {
        DisciplineDto disciplineDto = DisciplineDto.builder()
                .credits(discipline.getCredits())
                .name(discipline.getName())
                .teacher(discipline.getTeacher())
                .build();
        disciplineDto.setId(discipline.getId());
        return disciplineDto;
    }
}
