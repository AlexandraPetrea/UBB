package ro.ubb.catalog.core.repository;


import org.hibernate.Criteria;
import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.jpa.HibernateEntityManager;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.transaction.annotation.Transactional;
import ro.ubb.catalog.core.model.Student;
import ro.ubb.catalog.core.model.StudentDiscipline;
import ro.ubb.catalog.core.model.StudentDiscipline_;
import ro.ubb.catalog.core.model.Student_;

import javax.persistence.criteria.*;
import java.util.List;

/**
 * Created by radu.
 */
public class StudentRepositoryImpl extends CustomRepositorySupport<Student, Long> implements StudentRepositoryCustom {
    private static final Logger log = LoggerFactory.getLogger(StudentRepositoryImpl.class);

    @Override
    @Transactional
    public List<Student> findAllWithDisciplinesSqlQuery() {
        log.trace("findAllWithDisciplinesSqlQuery: method entered");

        HibernateEntityManager hibernateEntityManager = getEntityManager().unwrap(HibernateEntityManager.class);
        Session session = hibernateEntityManager.getSession();

        Query query = session.createSQLQuery("select distinct {s.*}, {sd.*}, {d.*}" +
                " from student s" +
                " left join student_discipline sd on sd.student_id = s.id" +
                " left join discipline d on d.id = sd.discipline_id")
                .addEntity("s", Student.class)
                .addJoin("sd", "s.studentDisciplines")
                .addJoin("d", "sd.discipline")
                .addEntity("s", Student.class)
                .setResultTransformer(Criteria.DISTINCT_ROOT_ENTITY);
        List<Student> students = query.list();

        log.trace("findAllWithDisciplinesSqlQuery: students={}", students);
        return students;
    }

    @Override
    @Transactional
    public List<Student> findAllWithDisciplinesJpql() {
        log.trace("findAllWithDisciplinesJpql: method entered");

        javax.persistence.Query query = getEntityManager().createQuery("select distinct s from Student s" +
                " left join fetch s.studentDisciplines sd" +
                " left join fetch sd.discipline d");

        List<Student> students = query.getResultList();

        log.trace("findAllWithDisciplinesJpql: students={}", students);
        return students;
    }



    @Override
    @Transactional
    public List<Student> findAllWithDisciplinesJpaCriteria() {
        log.trace("findAllWithDisciplinesJpaCriteria: method entered");

        CriteriaBuilder criteriaBuilder = getEntityManager().getCriteriaBuilder();
        CriteriaQuery<Student> query = criteriaBuilder.createQuery(Student.class);

        query.distinct(Boolean.TRUE);

        Root<Student> from = query.from(Student.class);

        Fetch<Student, StudentDiscipline> studentDisciplineFetch = from.fetch(Student_.studentDisciplines, JoinType.LEFT);
        studentDisciplineFetch.fetch(StudentDiscipline_.discipline, JoinType.LEFT);

        List<Student> students = getEntityManager().createQuery(query).getResultList();

        log.trace("findAllWithDisciplinesJpaCriteria: students={}", students);

        return students;
    }
}
