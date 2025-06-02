package com.axsos.bookapi.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;

import com.axsos.bookapi.models.BookApi;

public interface BookApiRepository extends CrudRepository<BookApi, Long>{
	
	List<BookApi> findAll();

}
