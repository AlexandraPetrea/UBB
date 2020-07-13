package ro.ubb.catalog.core.model;

import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value = "org.hibernate.jpamodelgen.JPAMetaModelEntityProcessor")
@StaticMetamodel(Discipline.class)
public abstract class Discipline_ extends ro.ubb.catalog.core.model.BaseEntity_ {

	public static volatile SingularAttribute<Discipline, String> teacher;
	public static volatile SingularAttribute<Discipline, Integer> credits;
	public static volatile SetAttribute<Discipline, StudentDiscipline> studentDisciplines;
	public static volatile SingularAttribute<Discipline, String> name;

}

