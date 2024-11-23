package com.ashishhiggins.coursecatalogue.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDateTime;

@Entity@Getter@Setter
public class UserCourses {

    @Id
    private String userCourseId;

    @ManyToOne
    @JoinColumn(name = "user_id")
    private Users user;


    @ManyToOne
    @JoinColumn(name = "course_id")
    private Courses courses;

    private LocalDateTime enrolledAt;

    private boolean isEnrolled;



}
