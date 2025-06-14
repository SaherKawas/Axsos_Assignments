package com.axsos.bookclub.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.axsos.bookclub.models.Book;
import com.axsos.bookclub.repositories.BookRepository;

@Service
public class BookService {

	@Autowired
	private BookRepository bookRepository;
	
	public Book createBook(Book book) {
        return bookRepository.save(book);
    }
	
	public List<Book> allBooks() {
        return bookRepository.findAll();
	}
        
    public Book findBook(Long id) {
        Optional<Book> optionalBook = bookRepository.findById(id);
            if(optionalBook.isPresent()) {
                return optionalBook.get();
            } else {
                return null;
            }
    }
    
    public Book updateBook(Long id, String title, String author, String thoughts) {
	    Optional<Book> optionalBook = bookRepository.findById(id);
	    if (optionalBook.isPresent()) {
	        Book book = optionalBook.get();
	        book.setTitle(title);
	        book.setAuthor(author);
	        book.setThoughts(thoughts);
	        return bookRepository.save(book);
	    } else {
	        return null;
	    }
    }
    
    public void deleteBook(Long id) {
        bookRepository.deleteById(id);
    }


}
