package ro.ubb.catalog.web.dto;

import lombok.*;

import javax.validation.constraints.NotEmpty;

@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@Builder
public class PersonDto extends BaseDto {
    @NotEmpty
    private String name;
    @NotEmpty
    private String ssn;

    @Override
    public String toString() {
        return "PersonDto{" +
                "name='" + name + '\'' +
                ", ssn='" + ssn + '\'' +
                '}' + super.toString();
    }
}

