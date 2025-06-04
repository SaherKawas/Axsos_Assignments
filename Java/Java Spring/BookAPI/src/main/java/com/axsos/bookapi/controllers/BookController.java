package com.axsos.bookapi.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

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
	
	@RequestMapping("/books")
    public String index(Model model) {
        List<BookApi> books = bookApiService.allBooks();
        model.addAttribute("books", books);
        return "index.jsp";
    }
}
