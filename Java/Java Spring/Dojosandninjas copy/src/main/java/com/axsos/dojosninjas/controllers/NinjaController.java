package com.axsos.dojosninjas.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.axsos.dojosninjas.models.Ninja;
import com.axsos.dojosninjas.services.DojoService;
import com.axsos.dojosninjas.services.NinjaService;

import jakarta.validation.Valid;

@Controller
public class NinjaController {
	@Autowired
	NinjaService ninjaService;
	
	@Autowired
	DojoService dojoService;
	
	@GetMapping("/ninjas/new")
	public String showNinja(@ModelAttribute("ninja") Ninja ninja, Model model) {
	    model.addAttribute("ninja", new Ninja());
	    model.addAttribute("dojos", dojoService.allDojos());
	    return "createninja";
	}
	@PostMapping("/ninjas/new")
	public String createNinja(@Valid @ModelAttribute Ninja ninja, BindingResult result) {
		if(result.hasErrors()) {
			return "createninja";
		}
		ninjaService.createNinja(ninja);
		return "redirect:/ninjas/new";
	}

}
