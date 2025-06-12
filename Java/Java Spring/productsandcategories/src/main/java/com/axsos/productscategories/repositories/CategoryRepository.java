package com.axsos.productscategories.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;

import com.axsos.productscategories.models.Category;
import com.axsos.productscategories.models.Product;


public interface CategoryRepository extends CrudRepository<Category, Long>{
	
	List<Category>findAll();

	List<Category> findByProductsNotContains(Product product);
}
