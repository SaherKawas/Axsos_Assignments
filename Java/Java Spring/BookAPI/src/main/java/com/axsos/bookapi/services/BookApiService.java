package com.axsos.bookapi.services;


import com.axsos.bookapi.models.BookApi;
import java.util.List;

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
	
}
