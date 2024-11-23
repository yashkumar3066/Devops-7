package com.ashishhiggins.coursecatalogue.Controller;

import com.ashishhiggins.coursecatalogue.entity.Courses;
import com.ashishhiggins.coursecatalogue.service.CourseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/courses")
public class CourseController {

    @Autowired
    private CourseService courseService;

    @PostMapping("/addCourse")
    public Courses addCourse(@RequestBody Courses course) {
        return courseService.addCourse(course);
    }

    @DeleteMapping("/{courseId}")
    public void deleteCourse(@PathVariable String courseId) {
        courseService.deleteCourse(courseId);
    }

    @GetMapping("/allCourses")
    public List<Courses> getAllCourses() {
        return courseService.getAllCourses();
    }
}
