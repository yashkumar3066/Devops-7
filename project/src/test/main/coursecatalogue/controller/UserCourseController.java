package main.coursecatalogue.Controller;

import main.coursecatalogue.entity.Courses;
import main.coursecatalogue.service.CourseService;
import main.coursecatalogue.service.UserCourseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/myCourses")
public class UserCourseController {

    @Autowired
    private UserCourseService userCourseService;
    @Autowired
    private CourseService courseService;

    @GetMapping("/{userId}")
    public List<Courses> getUserCourses(@PathVariable String userId) {
        return userCourseService.getUserCourses(userId);
    }


}
