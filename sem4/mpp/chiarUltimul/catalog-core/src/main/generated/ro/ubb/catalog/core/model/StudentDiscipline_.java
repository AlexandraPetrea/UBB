package ro.ubb.catalog.core.model;

import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value = "org.hibernate.jpamodelgen.JPAMetaModelEntityProcessor")
@StaticMetamodel(StudentDiscipline.class)
public abstract class StudentDiscipline_ {

	public static volatile SingularAttribute<StudentDiscipline, Student> student;
	public static volatile SingularAttribute<StudentDiscipline, Integer> grade;
	public static volatile SingularAttribute<StudentDiscipline, Discipline> discipline;

}

