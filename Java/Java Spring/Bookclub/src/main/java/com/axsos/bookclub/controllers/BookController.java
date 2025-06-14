package com.axsos.bookclub.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import com.axsos.bookclub.models.Book;
import com.axsos.bookclub.models.User;
import com.axsos.bookclub.services.BookService;

import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;

@Controller
public class BookController {
	
	@Autowired
	private BookService bookService;
	
	@GetMapping("/addbook")
	public String addBookForm(HttpSession session, Model model) {
        if (session.getAttribute("loggedUser") != null) {
        	model.addAttribute("book", new Book());
            model.addAttribute("books", bookService.allBooks());

        	return "addbook.jsp";
        }
        else {
            return "redirect:/";
        }
	}

	@PostMapping ("/bookaddition")
	public String addBook(@Valid @ModelAttribute Book book, BindingResult result, HttpSession session) {
		if(result.hasErrors()) {
			return "addbook.jsp";
		}
		
		User loggedUser = (User) session.getAttribute("loggedUser");
	    book.setUser(loggedUser);
	    
		bookService.createBook(book);
		return "redirect:/books";
	}
	
	@GetMapping("/books/{id}")
	public String showBook(Model model, HttpSession session, @PathVariable("id") Long id) {
	    if (session.getAttribute("loggedUser") != null) {

	        Book book = bookService.findBook(id);
	        User loggedUser = (User) session.getAttribute("loggedUser");

	        model.addAttribute("book", book);
	        model.addAttribute("userId", loggedUser.getId());

	        return "bookdetails.jsp";
	    } else {
	        return "redirect:/";
	    }
	}
	
	@GetMapping ("/books/{id}/edit")
	public String showBookEditForm(@PathVariable("id") Long id, Model model, HttpSession session) {
		if (session.getAttribute("loggedUser") != null) {
			Book book =bookService.findBook(id);
			model.addAttribute("book", book);
	  
			return "editbook.jsp";
		}
		else {
	            return "redirect:/";
	        }
	}
	
	@PostMapping ("/books/{id}/editing")
	public String editBook(@PathVariable("id") Long id, @Valid @ModelAttribute Book book, BindingResult result, HttpSession session) {
		if(result.hasErrors()) {
			return "editbook.jsp";
		}
		
		User loggedUser = (User) session.getAttribute("loggedUser");
	    book.setUser(loggedUser);
	    
	    bookService.updateBook(id, book.getTitle(), book.getAuthor(), book.getThoughts());
		return "redirect:/books/"+ id;
	}
	
	@PostMapping("/books/{id}/delete")
	public String deleteBook(@PathVariable("id") Long id, HttpSession session) {
		User loggedUser = (User) session.getAttribute("loggedUser");
		if (loggedUser == null) {
		    return "redirect:/";
	    }

	    bookService.deleteBook(id);
	    return "redirect:/books";
	}
}
	
	


