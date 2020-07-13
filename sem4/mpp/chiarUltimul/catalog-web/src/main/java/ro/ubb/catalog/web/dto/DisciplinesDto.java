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
@ToString
public class DisciplinesDto {
    private Set<DisciplineDto> disciplines;
}
