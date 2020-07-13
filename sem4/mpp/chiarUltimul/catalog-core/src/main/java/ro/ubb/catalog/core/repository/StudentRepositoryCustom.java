package ro.ubb.catalog.core.repository;

import ro.ubb.catalog.core.model.Student;

import java.util.List;

/**
 * Created by radu.
 */
public interface StudentRepositoryCustom {
    List<Student> findAllWithDisciplinesSqlQuery();

    List<Student> findAllWithDisciplinesJpql();

    List<Student> findAllWithDisciplinesJpaCriteria();
}
