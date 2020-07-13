package ro.ubb.catalog.core.model;

import lombok.*;

import javax.persistence.*;
import java.io.Serializable;

/**
 * Created by radu.
 */

@Entity
@Table(name = "student_discipline")
@IdClass(StudentDisciplinePK.class)
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
public class StudentDiscipline implements Serializable {

    @Id
    @ManyToOne(optional = false, fetch = FetchType.LAZY)
    @JoinColumn(name = "student_id")
    private Student student;

    @Id
    @ManyToOne(optional = false, fetch = FetchType.LAZY)
    @JoinColumn(name = "discipline_id")
    private Discipline discipline;

    @Column(name = "grade")
    private Integer grade = 0;

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        StudentDiscipline that = (StudentDiscipline) o;

        if (!student.equals(that.student)) return false;
        return discipline.equals(that.discipline);
    }

    @Override
    public int hashCode() {
        int result = student.hashCode();
        result = 31 * result + discipline.hashCode();
        return result;
    }
}
