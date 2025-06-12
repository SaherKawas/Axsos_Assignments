package com.axsos.productscategories.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.axsos.productscategories.models.Category;
import com.axsos.productscategories.models.Product;
import com.axsos.productscategories.repositories.ProductRepository;

@Service
public class ProductService {
	
	@Autowired
	private ProductRepository productRepository;
	
	public Product createProduct(Product product) {
	    return productRepository.save(product);
	}
	
	public List<Product> allProduct() {
	    return productRepository.findAll();
	}
	
	public Product findProductById(Long id) {
		return productRepository.findById(id).orElse(null);
	}
	
	public List<Product> getProductsByNotContain(Category category){
		  return productRepository.findByCategoriesNotContains(category);
	}
	public void addCatToProd(Product product, Category category) {
		System.out.println(product.getCategories());

		product.getCategories().add(category);
		productRepository.save(product);
	}
}
