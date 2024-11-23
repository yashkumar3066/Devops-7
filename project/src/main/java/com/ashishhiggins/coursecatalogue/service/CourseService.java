package com.ashishhiggins.coursecatalogue.service;

import com.ashishhiggins.coursecatalogue.entity.Courses;
import com.ashishhiggins.coursecatalogue.repository.CoursesRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CourseService {

    @Autowired
    public CoursesRepository coursesRepository;

    public Courses addCourse(Courses course) {
        return coursesRepository.save(course);
    }

    public void deleteCourse(String courseId) {
        coursesRepository.deleteById(courseId);
    }

    public List<Courses> getAllCourses() {
       return coursesRepository.findAll();
    }


}
