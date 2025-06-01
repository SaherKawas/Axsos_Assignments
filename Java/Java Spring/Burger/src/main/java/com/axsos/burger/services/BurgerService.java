package com.axsos.burger.services;

import java.util.List;

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

}
