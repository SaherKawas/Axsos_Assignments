package com.axsos.dojosninjas.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.axsos.dojosninjas.models.Dojo;
import com.axsos.dojosninjas.models.Ninja;
import com.axsos.dojosninjas.repositories.NinjaRepository;

@Service
public class NinjaService {
	
	@Autowired
	NinjaRepository ninjaRepository;
	
	public Ninja createNinja(Ninja ninja) {
        return ninjaRepository.save(ninja);
    }
	
	public List<Ninja> allNinjas() {
        return ninjaRepository.findAll();
}

}
