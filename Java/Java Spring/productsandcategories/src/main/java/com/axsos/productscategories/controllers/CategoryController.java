package com.axsos.productscategories.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.axsos.productscategories.models.Category;
import com.axsos.productscategories.models.Product;
import com.axsos.productscategories.services.CategoryService;
import com.axsos.productscategories.services.ProductService;

import jakarta.validation.Valid;

@Controller
public class CategoryController {
	
	@Autowired
	private CategoryService categoryService;
	
	@Autowired
	private ProductService productService;
	
	@GetMapping("/newcategory")
	public String newCategory(Model model) {
		model.addAttribute("category", new Category());
		return "newcategory.jsp";
		
	}
	
	@PostMapping("/category/form")
	public String createCategory(@Valid @ModelAttribute ("category") Category category, BindingResult result, Model model) {
		if(result.hasErrors()) {
			model.addAttribute("category", category);
			return "newcategory.jsp";
			
		}
		categoryService.createCategory(category);
		return "redirect:/";
	}
	
	@GetMapping("/categories/{id}")
	public String categoryDetails(Model model, @PathVariable("id") Long id) {
		Category category = categoryService.findCategoryById(id);
		model.addAttribute("category", category);
		model.addAttribute("unassigned", productService.getProductsByNotContain(category));
		return "categorydetails.jsp";
	}
	
	@PostMapping("/categories/{category_id}/addProduct")
	public String addProdToCat(@PathVariable("category_id") Long category_id, @RequestParam("productId")Long product_id) {
		Product product = productService.findProductById(product_id);
		Category category = categoryService.findCategoryById(category_id);
		categoryService.addProdToCat(product, category);
		
		return "redirect:/categories/" + category_id;	
		}

}
