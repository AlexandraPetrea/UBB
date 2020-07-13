package ro.ubb.catalog.web.dto;

import lombok.*;

import java.util.Set;

/**
 * Created by radu.
 */

@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@Builder
public class StudentDto extends BaseDto {
    private String serialNumber;
    private String name;
    private Integer groupNumber;
    private Set<Long> disciplines;

    @Override
    public String toString() {
        return "StudentDto{" +
                "serialNumber='" + serialNumber + '\'' +
                ", name='" + name + '\'' +
                ", groupNumber=" + groupNumber +
                ", disciplines=" + disciplines +
                "} " + super.toString();
    }
}
