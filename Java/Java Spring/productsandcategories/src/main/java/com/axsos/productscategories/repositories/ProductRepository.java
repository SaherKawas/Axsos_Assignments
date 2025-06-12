package com.axsos.productscategories.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;

import com.axsos.productscategories.models.Category;
import com.axsos.productscategories.models.Product;


public interface ProductRepository extends  CrudRepository<Product, Long>{
	
	List<Product>findAll();
	
	List<Product> findByCategoriesNotContains(Category category);

}
