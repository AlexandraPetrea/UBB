package ro.ubb.catalog.core.model;

import lombok.*;


import javax.persistence.Entity;

@Entity
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class Person extends BaseEntity<Long> {
 //   @UniqueElements

    private String ssn;

    private String name;
}
