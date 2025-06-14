package com.axsos.pathvariables;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;



@RestController
@SpringBootApplication
@RequestMapping("/daikichi")
public class PathvariablesApplication {

	public static void main(String[] args) {
		SpringApplication.run(PathvariablesApplication.class, args);
	}
	
	@RequestMapping("")
    public String index() {
		return "Welcome!";
    }
	
	@RequestMapping("/today")
    public String today() {
		return "Today you will find luck in all your endeavors!";
    }
	
	@RequestMapping("/tomorrow")
    public String tomorrow() {
		return "Tomorrow, an opportunity will arise, so be sure to be open to new ideas!";
	}

	@RequestMapping("/travel/{country}")
    public String travel(@PathVariable("country") String country) {
		return "Congratulations! You will soon travel to " + country;
    }

	@RequestMapping("/lotto/{number}")
    public String lotto(@PathVariable("number") int number) {
		if (number%2==0) {
			return "You will take a grand journey in the near future but be wary of tempting offers.";
		}else {
		return "You have enjoyed the fruits of your labor, but now is a great time to spend time with family and friends.";
		}
    }


}
