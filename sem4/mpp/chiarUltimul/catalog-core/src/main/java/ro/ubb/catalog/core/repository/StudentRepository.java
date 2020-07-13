package ro.ubb.catalog.core.repository;

import org.springframework.data.jpa.repository.EntityGraph;
import org.springframework.data.jpa.repository.Query;
import ro.ubb.catalog.core.model.Student;

import java.util.List;

/**
 * Created by radu.
 */


public interface StudentRepository extends CatalogRepository<Student, Long>, StudentRepositoryCustom{

    @Query("select distinct s from Student s")
    @EntityGraph(value = "studentWithDisciplines", type = EntityGraph.EntityGraphType.LOAD)
    List<Student> findAllWithDisciplinesGraph();

    @Query("select distinct s from Student s where s.id=?1")
    @EntityGraph(value = "studentWithDisciplines", type = EntityGraph.EntityGraphType.LOAD)
    Student findOneWithDisciplines(Long studentId);
}
