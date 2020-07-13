package ro.ubb.catalog.core.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import ro.ubb.catalog.core.model.Discipline;
import ro.ubb.catalog.core.repository.DisciplineRepository;

import java.util.List;

/**
 * Created by radu.
 */

@Service
public class DisciplineServiceImpl implements DisciplineService {

    private static final Logger log = LoggerFactory.getLogger(DisciplineServiceImpl.class);


    @Autowired
    private DisciplineRepository disciplineRepository;

    @Override
    @Transactional
    public List<Discipline> findAll() {
        log.trace("findAll");

        List<Discipline> disciplines = disciplineRepository.findAll();

        log.trace("findAll: disciplines={}", disciplines);

        return disciplines;
    }

    @Override
    public Discipline createDiscipline(String name, String teacher, Integer credits) {
        log.trace("createDiscipline: name={}, teacher={}, credits={}", name, teacher, credits);

        Discipline d = Discipline.builder()
                .credits(credits)
                .name(name)
                .teacher(teacher)
                .build();
        Discipline discipline = disciplineRepository.save(d);

        log.trace("createDiscipline: discipline={}", discipline);

        return discipline;
    }
}
