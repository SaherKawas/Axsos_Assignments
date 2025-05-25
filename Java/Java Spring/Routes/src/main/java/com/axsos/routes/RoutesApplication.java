package com.axsos.routes;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
@RequestMapping("/daikichi")
public class RoutesApplication {

	public static void main(String[] args) {
		SpringApplication.run(RoutesApplication.class, args);
	}
	
	@RequestMapping("/")
    public String index() {
		return "Welcome!";
    }
	
	@RequestMapping("/today")
    public String today() {
		return "Today you will find luck in all your endeavors!";
    }
	
	@RequestMapping("/tomorrow")
    public String tomorrw() {
		return "Tomorrow, an opportunity will arise, so be sure to be open to new ideas!";
    }

}
