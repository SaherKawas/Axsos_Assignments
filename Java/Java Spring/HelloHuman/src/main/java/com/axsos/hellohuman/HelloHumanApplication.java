package com.axsos.hellohuman;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestParam;

@SpringBootApplication
@RestController
public class HelloHumanApplication {

	public static void main(String[] args) {
		SpringApplication.run(HelloHumanApplication.class, args);
	}
	
	@RequestMapping("/")
    public String index() {
		return "Hello Human!";
    }
	
	@RequestMapping("/greet")
    public String name(
    		@RequestParam(value="name", required=false) String name,
    		@RequestParam(value="lastname", required=false) String lastname
    		) {
		
		return "Hello " + name + " " + lastname;
    }
	

}
