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
public class ProductController {

	@Autowired
	private ProductService productService;
	
	@Autowired
	private CategoryService categoryService;
	
	@GetMapping ("/")
	public String index(Model model) {
		model.addAttribute("categories", categoryService.allCategory());
		model.addAttribute("products", productService.allProduct());
		return "index.jsp";
	}
	
	@GetMapping ("/newproduct")
	public String newProduct(Model model) {
		model.addAttribute("product", new Product());
		return "newproduct.jsp";
	}
	
	@PostMapping("/product/form")
	public String createProdcut(@Valid @ModelAttribute ("product") Product product, BindingResult result, Model model) {
		if(result.hasErrors()) {
			model.addAttribute("product", product);
			return "newproduct.jsp";
			
		}
		productService.createProduct(product);
		return "redirect:/";
	}
	
	@GetMapping("/products/{id}")
	public String productDetails(Model model, @PathVariable("id") Long id) {
		Product product = productService.findProductById(id);
		model.addAttribute("product", product);
		model.addAttribute("unassigned", categoryService.getCategoriesByNotContain(product));
		return "productdetails.jsp";
	}
	
	
	@PostMapping("/products/{product_id}/addCategory")
	public String addCategoryToProduct(@PathVariable("product_id") Long product_id, @RequestParam("categoryId")Long categoryid) {
		Product product = productService.findProductById(product_id);
		Category category = categoryService.findCategoryById(categoryid);
		productService.addCatToProd(product, category);
		
		return "redirect:/products/" + product_id;	
		}
}
