package com.ashishhiggins.coursecatalogue.repository;

import com.ashishhiggins.coursecatalogue.entity.UserCourses;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface UserCoursesRepository extends JpaRepository<UserCourses, String> {

    List<UserCourses> findByUser_UserId(String userId);

}
