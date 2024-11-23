package com.ashishhiggins.coursecatalogue.repository;

import com.ashishhiggins.coursecatalogue.entity.Courses;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CoursesRepository extends JpaRepository<Courses, String> {

}
