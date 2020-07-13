package ro.ubb.catalog.core.model;

import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value = "org.hibernate.jpamodelgen.JPAMetaModelEntityProcessor")
@StaticMetamodel(Student.class)
public abstract class Student_ extends ro.ubb.catalog.core.model.BaseEntity_ {

	public static volatile SingularAttribute<Student, String> serialNumber;
	public static volatile SetAttribute<Student, StudentDiscipline> studentDisciplines;
	public static volatile SingularAttribute<Student, String> name;
	public static volatile SingularAttribute<Student, Integer> groupNumber;

}

