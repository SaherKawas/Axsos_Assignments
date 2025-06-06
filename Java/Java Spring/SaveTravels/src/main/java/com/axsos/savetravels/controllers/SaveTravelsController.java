package com.axsos.savetravels.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import com.axsos.savetravels.models.SaveTravels;
import com.axsos.savetravels.services.SaveTravelsService;

import jakarta.validation.Valid;

@Controller
public class SaveTravelsController {
	
	@Autowired
	SaveTravelsService saveTravelsService;
	
	@GetMapping("/")
	public String index(Model model, @ModelAttribute SaveTravels saveTravels) {
		model.addAttribute("travels", saveTravelsService.allTravels());
		return "index.jsp";
	}
	
	@PostMapping("/create")
	public String createTravels(@Valid @ModelAttribute SaveTravels saveTravels, BindingResult result) {
		if(result.hasErrors()) {
			return "index.jsp";
		}
		saveTravelsService.createTravels(saveTravels);
		return "redirect:/";
	}	
	
	@GetMapping("/edit/{id}")
    public String edit(@PathVariable Long id, Model model) {
        SaveTravels saveTravels = saveTravelsService.findTravels(id);
        model.addAttribute("saveTravels", saveTravels);
        return "edit.jsp";
	}
	
	@PostMapping("/edit/{id}")
    public String edit(@Valid @ModelAttribute SaveTravels travel,BindingResult result) {
        if (result.hasErrors()) {
            return "index.jsp";
        }
        saveTravelsService.updateTravels(travel);
        return "redirect:/";
    	}
	
	@GetMapping("/delete/{id}")
	public String destroy(@PathVariable("id") Long id) {
	    saveTravelsService.deleteTravels(id);
	    return "redirect:/";
	}
	@GetMapping("/expenses/{id}")
	public String showexpense(@PathVariable("id") Long id, Model model) {
	      
		SaveTravels travel =saveTravelsService.findTravels(id);
		model.addAttribute("travel", travel);
  
		return "details.jsp";

	}
}

