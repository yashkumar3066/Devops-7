package com.ashishhiggins.coursecatalogue.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDateTime;

@Entity
@Getter@Setter
public class Users {

    @Id
    private String userId;

    private String username;

    private String email;

    private LocalDateTime createdAt;

}
