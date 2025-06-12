package com.axsos.productscategories.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.axsos.productscategories.models.Category;
import com.axsos.productscategories.models.Product;
import com.axsos.productscategories.repositories.CategoryRepository;

@Service
public class CategoryService {
	@Autowired
	private CategoryRepository categoryRepository;
	
	public Category createCategory(Category category) {
	    return categoryRepository.save(category);
	}

	public List<Category> allCategory() {
	    return categoryRepository.findAll();
	}
	
	public List<Category> getCategoriesByNotContain(Product product){
		  return categoryRepository.findByProductsNotContains(product);
	}
	
	public Category findCategoryById(Long id) {
		return categoryRepository.findById(id).orElse(null);
	}
	
	public void addProdToCat(Product product, Category category) {

		category.getProducts().add(product);
		categoryRepository.save(category);
	}
	
}
