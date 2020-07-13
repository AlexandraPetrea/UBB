package ro.ubb.catalog.core.model;

import lombok.Data;

import javax.persistence.*;

/**
 * Created by radu.
 */

@Entity
@Table(name = "app_user")
@Data
public class User extends BaseEntity<Long> {

    @Column(name = "first_name", nullable = false)
    private String firstName;

    @Column(name = "last_name", nullable = false)
    private String lastName;

    @Column(name = "user_name", nullable = false, unique = true)
    private String userName;

    @Column(name = "password", nullable = false)
    private String password;

    @Enumerated(EnumType.STRING)
    @Column(name = "user_role", nullable = false)
    private UserRole userRole;
}
