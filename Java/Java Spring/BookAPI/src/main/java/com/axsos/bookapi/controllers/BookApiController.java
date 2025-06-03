package com.axsos.bookapi.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.axsos.bookapi.models.BookApi;
import com.axsos.bookapi.services.BookApiService;

import ch.qos.logback.core.joran.spi.HttpUtil.RequestMethod;

@RestController
public class BookApiController {

	@Autowired
	BookApiService bookApiService;
	
	@GetMapping(value="/api/books")
	  public List<BookApi> all(){
	    	return bookApiService.allBooks();
	  }
	 
	    
	@PostMapping(value="/api/books/create")
	    public BookApi create(
	    		@RequestParam(value="title") String title,
	    		@RequestParam(value="description") String desc,
	    		@RequestParam(value="language") String lang,
	    		@RequestParam(value="pages") Integer numOfPages) {
	    	BookApi book = new BookApi(title, desc, lang, numOfPages);
	    	return bookApiService.createBook(book);
	    }
	
	@PutMapping("/edit/{id}")
	public BookApi update(
	    @PathVariable("id") Long id,
	    @RequestParam(value="title") String title,
	    @RequestParam(value="description") String desc,
	    @RequestParam(value="language") String lang,
	    @RequestParam(value="pages") Integer numOfPages) {
	    BookApi book = bookApiService.updateBook(id, title, desc, lang, numOfPages);
	    return book;
	}

	@DeleteMapping("/{id}")
	public void destroy(@PathVariable("id") Long id) {
	    bookApiService.deleteBook(id);
	}
	
	
}
