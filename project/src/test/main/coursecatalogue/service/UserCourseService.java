package com.coursecatalogue.service;

import com.coursecatalogue.entity.Courses;
import com.coursecatalogue.entity.UserCourses;
import com.coursecatalogue.repository.CoursesRepository;
import com.coursecatalogue.repository.UserCoursesRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;



@Service
public class UserCourseService {

    @Autowired
    private UserCoursesRepository userCoursesRepository;

    @Autowired
    private CoursesRepository  coursesRepository;

    public List<Courses> getUserCourses(String userId) {
        List<UserCourses> userCourses = userCoursesRepository.findByUser_UserId(userId);
        List<Courses> coursesList = new ArrayList<>();

        for(UserCourses user : userCourses){
            coursesList.add(coursesRepository.findById(user.getCourses().getCourseId()).get());
        }
        return coursesList;
    }

}