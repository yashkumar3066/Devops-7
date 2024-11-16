package com.ashishhiggins.coursecatalogue.Controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @GetMapping("/hello")
    public String sayHello() {

        return "Hello, World! ";
    }
    @GetMapping("/hello2")
    public String sayHello2() {

        return "Hello, World! again";
    }
    @GetMapping("/hello3")
    public String sayHello3() {

        return "Hello, World! 3 again";
    }
    @GetMapping("/hello4")
    public String sayHello4() {

        return "Hello, World! 4 again";
    }
    @GetMapping("/hello5")
    public String sayHello5() {

        return "Hello, World! 5 again";
    }
}
