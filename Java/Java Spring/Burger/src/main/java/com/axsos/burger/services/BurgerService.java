package com.axsos.burger.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.axsos.burger.models.Burger;
import com.axsos.burger.repositories.BurgerRepository;

@Service
public class BurgerService {
	
	@Autowired
	BurgerRepository burgerRepository;
	
	public List<Burger> allBurgers(){
		return burgerRepository.findAll();	
	}
	
	public Burger createBurger(Burger burger){
		return burgerRepository.save(burger);
	}
	
	public Burger findBurger(Long id) {
        Optional<Burger> optionalBurger = burgerRepository.findById(id);
        if(optionalBurger.isPresent()) {
            return optionalBurger.get();
        } else {
            return null;
        }
	}
	public Burger updateBurger(Burger burger){
		return burgerRepository.save(burger);
	}
	
	
}
