package com.axsos.loginregister.services;

import java.util.Optional;

import org.mindrot.jbcrypt.BCrypt;
import org.springframework.stereotype.Service;
import org.springframework.validation.BindingResult;

import com.axsos.loginregister.models.LoginRegister;
import com.axsos.loginregister.models.LoginUser;
import com.axsos.loginregister.repositories.LoginRegisterRepository;

@Service
public class LoginRegisterService {
	
	private final LoginRegisterRepository loginRegisterRepository;
	
	public LoginRegisterService(LoginRegisterRepository loginRegisterRepository) {
		this.loginRegisterRepository= loginRegisterRepository;
	}
	
	public LoginRegister register(LoginRegister newUser, BindingResult result) {
		
		Optional<LoginRegister> potentialNewUser = loginRegisterRepository.findByEmail(newUser.getEmail());
		if (potentialNewUser.isPresent()) {
			result.rejectValue("email", "Email.Exists", "This email already exists!" );
		}
		
		if (!newUser.getPassword().equals(newUser.getConfirmPassword())) {
			result.rejectValue("password", "Not.Match", "Passwords do not match!" );
		}
		if (result.hasErrors()) {
			return null;
		}
		
		String hashedPassword = BCrypt.hashpw(newUser.getPassword(), BCrypt.gensalt());
		newUser.setPassword(hashedPassword);
		return loginRegisterRepository.save(newUser);

	}
	
	public LoginRegister login(LoginUser newLoginObject, BindingResult result) {
		
		Optional<LoginRegister> loginUser = loginRegisterRepository.findByEmail(newLoginObject.getEmail());
		if (loginUser.isEmpty()) {
			result.rejectValue( "email", "Not Found" , "Email does not exist" );
			return null;
		}
		LoginRegister user = loginUser.get();
		
		if (!BCrypt.checkpw(newLoginObject.getPassword(), user.getPassword())) {
			result.rejectValue("password", "invalid" , "Email or Password does not exist");
		}
		if (result.hasErrors()) {
    		return null;
    	}
    	else {
    		return user;
    	}
	}
	      
}
	
