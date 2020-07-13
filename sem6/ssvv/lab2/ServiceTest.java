package MaxPointsParticipantsMV;

import java.util.stream.StreamSupport;

import org.junit.Test;

import domain.Nota;
import domain.Student;
import domain.Tema;
import javafx.beans.value.ObservableBooleanValue;
import repository.NotaXMLRepository;
import repository.StudentXMLRepository;
import repository.TemaXMLRepository;
import service.Service;
import validation.NotaValidator;
import validation.StudentValidator;
import validation.TemaValidator;
import validation.ValidationException;
import validation.Validator;

import static javafx.beans.binding.Bindings.when;
import static junit.framework.TestCase.assertEquals;
import static junit.framework.TestCase.assertTrue;

/**
 * Created by Vlad.Ovadiuc on 3/18/2020
 */
public class ServiceTest {


	Validator<Student> studentValidator = new StudentValidator();
	Validator<Tema> temaValidator = new TemaValidator();
	Validator<Nota> notaValidator = new NotaValidator();
	StudentXMLRepository fileRepository1 = new StudentXMLRepository(studentValidator, "src/main/studentiTest.xml");
	TemaXMLRepository fileRepository2 = new TemaXMLRepository(temaValidator, "src/main/temeTest.xml");
	NotaXMLRepository fileRepository3 = new NotaXMLRepository(notaValidator, "src/main/noteTest.xml");
	Service service = new Service(fileRepository1, fileRepository2, fileRepository3);


	private long getSize(Iterable<Student> students) {
		return StreamSupport.stream(students.spliterator(), false).count();
	}

	@Test
	public void saveStudent() {
		assertEquals(0, getSize(service.findAllStudents()));
		assertEquals(1, service.saveStudent("1", "Name", 123));
		assertEquals(1, getSize(service.findAllStudents()));
		service.deleteStudent("1");
		assertEquals(0, getSize(service.findAllStudents()));
	}

	@Test
	public void saveStudentWithNullName(){
		assertEquals(0, getSize(service.findAllStudents()));
		assertEquals(1, service.saveStudent("1", null, 123));
		assertEquals(0, getSize(service.findAllStudents()));
	}

	@Test
	public void saveStudentWithInvalidGroup(){
		assertEquals(0, getSize(service.findAllStudents()));
		assertEquals(1, service.saveStudent("1", "Name", 1234));
		assertEquals(0, getSize(service.findAllStudents()));
	}
}