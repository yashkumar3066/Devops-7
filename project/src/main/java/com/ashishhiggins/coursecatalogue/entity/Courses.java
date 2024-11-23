package com.ashishhiggins.coursecatalogue.entity;

import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.CascadeType;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDateTime;
import java.util.List;

@Entity@Getter@Setter
public class Courses {

    @Id
    private String courseId;

    private String title;

    private String details;

    private String semester;

    private LocalDateTime createdAt;

    @OneToMany(mappedBy = "courses", cascade = CascadeType.REMOVE)
    @JsonIgnore
    private List<UserCourses> userCourses;
}
