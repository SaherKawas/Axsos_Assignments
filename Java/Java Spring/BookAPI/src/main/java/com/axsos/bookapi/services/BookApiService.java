package com.axsos.bookapi.services;


import com.axsos.bookapi.models.BookApi;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.axsos.bookapi.repositories.BookApiRepository;

@Service
public class BookApiService {
	
	@Autowired
	BookApiRepository bookApiRepository;
	
	public List<BookApi> allBooks(){
		return bookApiRepository.findAll();	
	}
	
	public BookApi createBook(BookApi books){
		return bookApiRepository.save(books);
	}
	
	public BookApi updateBook(Long id, String title, String desc, String lang, Integer numOfPages) {
        Optional<BookApi> optionalBook = bookApiRepository.findById(id);
        if (optionalBook.isPresent()) {
            BookApi book = optionalBook.get();
            book.setTitle(title);
            book.setDescription(desc);
            book.setLanguage(lang);
            book.setNumberOfPages(numOfPages);
            return bookApiRepository.save(book); 
        } else {
            return null;
        }
	}
    
    public void deleteBook(Long id) {
        bookApiRepository.deleteById(id);
    }
	
}
