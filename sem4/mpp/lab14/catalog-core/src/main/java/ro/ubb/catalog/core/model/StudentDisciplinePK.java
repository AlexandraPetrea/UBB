package ro.ubb.catalog.core.model;

import lombok.*;

import java.io.Serializable;

/**
 * Created by radu.
 */

@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter

public class StudentDisciplinePK implements Serializable {
    private Student student;
    private Discipline discipline;

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        StudentDisciplinePK that = (StudentDisciplinePK) o;

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
