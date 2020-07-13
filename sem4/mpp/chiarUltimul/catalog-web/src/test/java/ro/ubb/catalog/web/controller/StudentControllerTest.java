package ro.ubb.catalog.web.controller;


import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.hamcrest.Matchers;
import org.junit.Before;
import org.junit.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.ResultActions;
import org.springframework.test.web.servlet.request.MockHttpServletRequestBuilder;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;

import static org.hamcrest.CoreMatchers.anyOf;
import static org.hamcrest.CoreMatchers.containsString;
import static org.mockito.Mockito.*;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

import ro.ubb.catalog.core.model.Student;
import ro.ubb.catalog.core.service.StudentService;
import ro.ubb.catalog.web.converter.StudentConverter;
import ro.ubb.catalog.web.dto.StudentDto;


import java.util.*;

import static org.hamcrest.Matchers.hasSize;
import static org.hamcrest.core.Is.is;
import static org.junit.Assert.assertEquals;
import static org.mockito.Mockito.*;
import static org.mockito.MockitoAnnotations.initMocks;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

/**
 * Created by radu.
 */
public class StudentControllerTest {

    private MockMvc mockMvc;

    @InjectMocks
    private StudentController studentController;

    @Mock
    private StudentService studentService;

    @Mock
    private StudentConverter studentConverter;

    private Student student1;
    private Student student2;
    private StudentDto studentDto1;
    private StudentDto studentDto2;


    @Before
    public void setup() throws Exception {
        initMocks(this);
        this.mockMvc = MockMvcBuilders
                .standaloneSetup(studentController)
                .build();
        initData();
    }

    @Test
    public void getStudents() throws Exception {
        List<Student> students = Arrays.asList(student1, student2);
        Set<StudentDto> studentDtos =
                new HashSet<>(Arrays.asList(studentDto1, studentDto2));
        when(studentService.findAll()).thenReturn(students);
        when(studentConverter.convertModelsToDtos(students)).thenReturn(studentDtos);

        ResultActions resultActions = mockMvc
                .perform(MockMvcRequestBuilders.get("/students"))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON_UTF8))
                .andExpect(jsonPath("$", hasSize(2)))
                .andExpect(jsonPath("$[0].name", anyOf(is("s1"), is("s2"))))
                .andExpect(jsonPath("$[1].serialNumber", anyOf(is("sn1"), is("sn2"))));

        String result = resultActions.andReturn().getResponse().getContentAsString();
//        System.out.println(result);

        verify(studentService, times(1)).findAll();
        verify(studentConverter, times(1)).convertModelsToDtos(students);
        verifyNoMoreInteractions(studentService, studentConverter);


    }

    @Test
    public void updateStudent() throws Exception {

        when(studentService.updateStudent(student1.getId(),
                studentDto1.getSerialNumber(),studentDto1.getName(),
                studentDto1.getGroupNumber(),studentDto1.getDisciplines()))
        .thenReturn(student1);

        when(studentConverter.convertModelToDto(student1)).thenReturn(studentDto1);

//        Map<String, StudentDto> studentDtoMap = new HashMap<>();
//        studentDtoMap.put("student", studentDto1);

        ResultActions resultActions = mockMvc
                .perform(MockMvcRequestBuilders
                .put("/students/{studentId}", student1.getId(), studentDto1)
                        .contentType(MediaType.APPLICATION_JSON_UTF8)
                .content(toJsonString(studentDto1)))

                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON_UTF8))
                .andExpect(jsonPath("$.name", is("s1")));

        verify(studentService, times(1)).updateStudent(student1.getId(),
                studentDto1.getSerialNumber(),studentDto1.getName(),
                studentDto1.getGroupNumber(),studentDto1.getDisciplines());
        verify(studentConverter, times(1)).convertModelToDto(student1);
        verifyNoMoreInteractions(studentService, studentConverter);
    }

    private String toJsonString(Map<String, StudentDto> studentDtoMap) {
        try {
            return new ObjectMapper().writeValueAsString(studentDtoMap);
        } catch (JsonProcessingException e) {
            throw new RuntimeException(e);
        }
    }

    private String toJsonString(StudentDto studentDto) {
        try {
            return new ObjectMapper().writeValueAsString(studentDto);
        } catch (JsonProcessingException e) {
            throw new RuntimeException(e);
        }
    }

    @Test
    public void createStudent() throws Exception {

    }

    @Test
    public void deleteStudent() throws Exception {

    }

    private void initData() {
        student1 = Student.builder().serialNumber("sn1").name("s1").build();
        student1.setId(1l);
        student2 = Student.builder().serialNumber("sn2").name("s2").build();
        student2.setId(2l);

        studentDto1 = createStudentDto(student1);
        studentDto2 = createStudentDto(student2);

    }

    private StudentDto createStudentDto(Student student) {
        StudentDto studentDto = StudentDto.builder()
                .serialNumber(student.getSerialNumber())
                .name(student.getName())
                .groupNumber(student.getGroupNumber())
                .build();
        studentDto.setId(student.getId());
        return studentDto;
    }


}