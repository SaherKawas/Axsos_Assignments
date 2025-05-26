package com.axsos.displaydate;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import java.text.SimpleDateFormat;
import org.springframework.ui.Model;

@SpringBootApplication
@Controller
public class DisplayDateApplication {

	public static void main(String[] args) {
		SpringApplication.run(DisplayDateApplication.class, args);
	}
	
	@RequestMapping("/")
	public String index() {
        return "index.jsp";
    }
	
	@RequestMapping("/date")
	public String date() {
        return "date.jsp";
    }
	
	@RequestMapping("/time")
	public String time(Model model) {
		String pattern = "h:mm a";
		SimpleDateFormat simpleDateFormat = new SimpleDateFormat(pattern);
		String date = simpleDateFormat.format(new java.util.Date());
		model.addAttribute("date",date);
		return "time.jsp";
    }
	
	
	
	
	

}
