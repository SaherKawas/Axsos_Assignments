package com.axsos.burger.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.axsos.burger.models.Burger;
import com.axsos.burger.services.BurgerService;

import jakarta.validation.Valid;

@Controller
public class burgerController {
	
	@Autowired
	BurgerService burgerService;
	
	@GetMapping("/")
	public String index(Model model, @ModelAttribute Burger burger) {
		model.addAttribute("burgers", burgerService.allBurgers());
		return "index.jsp";
	}
	
	@PostMapping("/create")
	public String createBurger(@Valid @ModelAttribute Burger burger, BindingResult result) {
		if(result.hasErrors()) {
			return "index.jsp";
		}
		burgerService.createBurger(burger);
		return "redirect:/";
	}

}
