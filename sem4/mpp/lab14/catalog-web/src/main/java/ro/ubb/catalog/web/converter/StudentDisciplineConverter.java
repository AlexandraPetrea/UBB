package ro.ubb.catalog.web.converter;

import org.springframework.stereotype.Component;
import ro.ubb.catalog.core.model.StudentDiscipline;
import ro.ubb.catalog.web.dto.StudentDisciplineDto;
import ro.ubb.catalog.web.dto.StudentDisciplinesDto;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by radu.
 */
@Component
public class StudentDisciplineConverter extends BaseConverterGeneric<StudentDiscipline, StudentDisciplineDto> {
    @Override
    public StudentDiscipline convertDtoToModel(StudentDisciplineDto studentDisciplineDto) {
        throw new RuntimeException("not yet implemented.");
    }

    @Override
    public StudentDisciplineDto convertModelToDto(StudentDiscipline studentDiscipline) {
        StudentDisciplineDto studentDisciplineDto = StudentDisciplineDto.builder()
                .studentId(studentDiscipline.getStudent().getId())
                .disciplineId(studentDiscipline.getDiscipline().getId())
                .disciplineName(studentDiscipline.getDiscipline().getName())
                .grade(studentDiscipline.getGrade())
                .build();
        return studentDisciplineDto;
    }

    public Map<Long, Integer> convertDtoToMap(StudentDisciplinesDto studentDisciplinesDto) {
        Map<Long, Integer> grades = new HashMap<>();
        studentDisciplinesDto.getStudentDisciplines().stream()
                .forEach(sd -> grades.put(sd.getDisciplineId(), sd.getGrade()));
        return grades;
    }
}
