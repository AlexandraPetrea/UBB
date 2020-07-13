package ro.ubb.catalog.core.service;

import ro.ubb.catalog.core.model.Student;

import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Created by radu.
 */
public interface StudentService {
    List<Student> findAll();

    Student findStudent(Long studentId);

    Student updateStudent(Long studentId, String serialNumber, String name, Integer groupNumber,
                          Set<Long> disciplines);

    Student createStudent(String serialNumber, String name, Integer groupNumber);

    void deleteStudent(Long studentId);

    Student updateStudentGrades(Long studentId, Map<Long, Integer> grades);
}
