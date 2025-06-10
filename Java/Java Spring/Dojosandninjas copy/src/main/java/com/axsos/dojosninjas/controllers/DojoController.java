package com.axsos.dojosninjas.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import com.axsos.dojosninjas.models.Dojo;
import com.axsos.dojosninjas.services.DojoService;
import com.axsos.dojosninjas.services.NinjaService;

import jakarta.validation.Valid;

@Controller
public class DojoController {
	@Autowired
	DojoService dojoService;
	
	@Autowired
	NinjaService ninjaService;
	
	@GetMapping("/dojos/new")
	public String showCreateDojoForm(Model model) {
	    model.addAttribute("dojo", new Dojo());
	    return "createdojo";
	}
	@PostMapping("/dojos/new")
	public String createDojo(@Valid @ModelAttribute Dojo dojo, BindingResult result) {
		if(result.hasErrors()) {
			return "createdojo";
		}
		dojoService.createDojo(dojo);
		return "redirect:/dojos/new";
	}
	
	@GetMapping("/dojos/{id}")
	public String showNinjasList(@PathVariable("id") Long id, Model model) {
		Dojo dojo = dojoService.findDojo(id);
		model.addAttribute("dojo", dojo);
		model.addAttribute("ninjas", dojo.getNinjas());
		return "dojodetails";
	}
}