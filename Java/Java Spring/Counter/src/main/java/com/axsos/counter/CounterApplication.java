package com.axsos.counter;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import jakarta.servlet.http.HttpSession;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;


@SpringBootApplication
@Controller
public class CounterApplication {

	public static void main(String[] args) {
		SpringApplication.run(CounterApplication.class, args);
	}
	@RequestMapping("/")
	public String welcome(HttpSession session){
		if (session.getAttribute("count") == null) {
			session.setAttribute("count", 0);
		}
		else {
		int counter= (int) session.getAttribute("count");
		session.setAttribute("count", counter+1);
		}
		
	    return "welcome.jsp";
    }
	@RequestMapping("/counter")
	public String index(HttpSession session) {
		return "index.jsp";
	}
	

}
