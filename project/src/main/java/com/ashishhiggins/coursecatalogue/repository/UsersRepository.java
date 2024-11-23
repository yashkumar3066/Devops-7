package com.ashishhiggins.coursecatalogue.repository;

import com.ashishhiggins.coursecatalogue.entity.Users;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UsersRepository extends JpaRepository<Users, String> {

}
