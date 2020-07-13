package ro.ubb.catalog.web.converter;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;
import ro.ubb.catalog.core.model.Student;
import ro.ubb.catalog.web.dto.StudentDto;

import java.util.Set;
import java.util.stream.Collectors;

/**
 * Created by radu.
 */

@Component
public class StudentConverter extends BaseConverter<Student, StudentDto> {

    private static final Logger log = LoggerFactory.getLogger(StudentConverter.class);

    @Override
    public StudentDto convertModelToDto(Student student) {
        StudentDto studentDto = StudentDto.builder()
                .serialNumber(student.getSerialNumber())
                .name(student.getName())
                .groupNumber(student.getGroupNumber())
                .build();
        studentDto.setId(student.getId());
        studentDto.setDisciplines(student.getDisciplines().stream()
                .map(d -> d.getId())
                .collect(Collectors.toSet()));
        return studentDto;
    }
}
