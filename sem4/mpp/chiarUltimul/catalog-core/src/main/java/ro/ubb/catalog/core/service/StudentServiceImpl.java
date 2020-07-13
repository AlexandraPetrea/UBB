package ro.ubb.catalog.core.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import ro.ubb.catalog.core.model.Discipline;
import ro.ubb.catalog.core.model.Student;
import ro.ubb.catalog.core.repository.DisciplineRepository;
import ro.ubb.catalog.core.repository.StudentRepository;

import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Created by radu.
 */

@Service
public class StudentServiceImpl implements StudentService {

    private static final Logger log = LoggerFactory.getLogger(StudentServiceImpl.class);

    @Autowired
    private StudentRepository studentRepository;

    @Autowired
    private DisciplineRepository disciplineRepository;

    @Override
    public List<Student> findAll() {
        log.trace("findAll");

//        List<Student> students = studentRepository.findAll();
//        List<Student> students = studentRepository.findAllWithDisciplinesGraph();
//        List<Student> students = studentRepository.findAllWithDisciplinesSqlQuery();
//        List<Student> students = studentRepository.findAllWithDisciplinesJpql();
        List<Student> students = studentRepository.findAllWithDisciplinesJpaCriteria();

        log.trace("findAll: students={}", students);

        return students;
    }

    @Override
    public Student findStudent(Long studentId) {
        log.trace("findStudent: studentId={}", studentId);

//        Student student = studentRepository.findOne(studentId);
        Student student = studentRepository.findOneWithDisciplines(studentId);

        log.trace("findStudent: student={}", student);

        return student;
    }

    @Override
    @Transactional
    public Student updateStudent(Long studentId, String serialNumber, String name, Integer groupNumber,
                                 Set<Long> disciplines) {
        log.trace("updateStudent: studentId={}, serialNumber={}, name={}, groupNumber={}, disciplines={}",
                studentId, serialNumber, name, groupNumber, disciplines);

        Student student = studentRepository.findOne(studentId);
        student.setSerialNumber(serialNumber);
        student.setName(name);
        student.setGroupNumber(groupNumber);

        student.getDisciplines().stream()
                .map(d -> d.getId())
                .forEach(id -> {
                    if (disciplines.contains(id)) {
                        disciplines.remove(id);
                    }
                });
        List<Discipline> disciplineList = disciplineRepository.findAll(disciplines);
        disciplineList.stream().forEach(d -> student.addDiscipline(d));

        log.trace("updateStudent: student={}", student);

        return student;
    }

    @Override
    public Student createStudent(String serialNumber, String name, Integer groupNumber) {
        log.trace("createStudent: serialNumber={}, name={}, groupNumber={}",
                serialNumber, name, groupNumber);

        Student student = Student.builder()
                .serialNumber(serialNumber)
                .name(name)
                .groupNumber(groupNumber)
                .build();
        student = studentRepository.save(student);

        log.trace("createStudent: student={}", student);

        return student;
    }

    @Override
    public void deleteStudent(Long studentId) {
        log.trace("deleteStudent: studentId={}", studentId);

        studentRepository.delete(studentId);

        log.trace("deleteStudent - method end");
    }

    @Override
    @Transactional
    public Student updateStudentGrades(Long studentId, Map<Long, Integer> grades) {
        log.trace("updateStudentGrades: studentId={}, grades={}", studentId, grades);

        Student student = studentRepository.findOne(studentId);
        student.getStudentDisciplines().stream()
                .forEach(sd -> sd.setGrade(grades.get(sd.getDiscipline().getId())));

        log.trace("updateStudentGrades: student={}", student);
        return student;
    }


}
