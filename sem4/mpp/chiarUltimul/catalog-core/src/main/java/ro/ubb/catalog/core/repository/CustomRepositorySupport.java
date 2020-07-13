package ro.ubb.catalog.core.repository;

import lombok.Getter;
import lombok.Setter;
import ro.ubb.catalog.core.model.BaseEntity;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import java.io.Serializable;

/**
 * Created by radu.
 */
@Getter
@Setter
public abstract class CustomRepositorySupport<T extends BaseEntity<ID>, ID extends Serializable> {

    @PersistenceContext
    private EntityManager entityManager;

}
