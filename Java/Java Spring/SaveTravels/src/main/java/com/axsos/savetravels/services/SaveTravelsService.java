package com.axsos.savetravels.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.axsos.savetravels.models.SaveTravels;
import com.axsos.savetravels.repositories.SaveTravelsRepository;

@Service
public class SaveTravelsService {
	
	private final SaveTravelsRepository saveTravelsRepository;

	public SaveTravelsService(SaveTravelsRepository saveTravelsRepository) {

	this.saveTravelsRepository = saveTravelsRepository;
	}
	
	public List<SaveTravels> allTravels() {
        return saveTravelsRepository.findAll();
    }
	public SaveTravels createTravels(SaveTravels t) {
        return saveTravelsRepository.save(t);
    }

	public SaveTravels findTravels(Long id) {
        Optional<SaveTravels> optionalTravels = saveTravelsRepository.findById(id);
        if(optionalTravels.isPresent()) {
            return optionalTravels.get();
        } else {
            return null;
        }
	}
	public SaveTravels updateTravels(SaveTravels saveTravels){
		return saveTravelsRepository.save(saveTravels);
	}
	
	public void deleteTravels(Long id) {
        saveTravelsRepository.deleteById(id);
    }

}
