package com.axsos.loginregister.repositories;

import java.util.List;
import java.util.Optional;

import org.springframework.data.repository.CrudRepository;

import com.axsos.loginregister.models.LoginRegister;


public interface LoginRegisterRepository extends  CrudRepository<LoginRegister, Long>{
	
	Optional<LoginRegister> findByEmail(String email);
}
