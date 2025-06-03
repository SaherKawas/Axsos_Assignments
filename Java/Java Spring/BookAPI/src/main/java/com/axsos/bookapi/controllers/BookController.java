package com.axsos.bookapi.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import com.axsos.bookapi.models.BookApi;
import com.axsos.bookapi.services.BookApiService;

@Controller
public class BookController {
	
	@Autowired
	BookApiService bookApiService;
	
	@GetMapping("/book/{id}")
	public String showbook(@PathVariable("id") Long id, Model model) {
        
		BookApi book =bookApiService.findBook(id);
 		model.addAttribute("book", book);
    
        return "show.jsp";
	}
}
