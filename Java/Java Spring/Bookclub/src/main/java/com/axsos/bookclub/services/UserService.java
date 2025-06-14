package com.axsos.bookclub.services;

import java.util.Optional;

import org.mindrot.jbcrypt.BCrypt;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.validation.BindingResult;

import com.axsos.bookclub.models.LoginUser;
import com.axsos.bookclub.models.User;
import com.axsos.bookclub.repositories.UserRepository;

@Service
public class UserService {
	
	@Autowired
	private UserRepository userRepository;
	
	public User register(User user , BindingResult bindingResult) {
		// Check if email is already taken
		Optional<User> potentialNewUser = userRepository.findByEmail(user.getEmail());
		if (potentialNewUser.isPresent()) {
			bindingResult.rejectValue("email", "Email.Exists", "This Email already exists!" );
		}
		
    // Check if passwords match
		if (!user.getPassword().equals(user.getConfirmPassword())) {
			bindingResult.rejectValue("password", "Not.Match", "Passwords not match!" );
		}
		
    // Return null if result has errors
		if (bindingResult.hasErrors()) {
			return null;
		}

    // Hash and set password, save user to database
		String hashedPassword = BCrypt.hashpw(user.getPassword(), BCrypt.gensalt());
		user.setPassword(hashedPassword);
		return userRepository.save(user);

	}
	
	
	public User login(LoginUser userLogin, BindingResult bindingResult) {
		
		// Find user in the DB by email
		Optional<User> loginUser = userRepository.findByEmail(userLogin.getEmail());
		if (loginUser.isEmpty()) {
			bindingResult.rejectValue( "email", "Not Found" , "Email does not exist" );
			return null;
		}
		
		// Get the user object
		User user = loginUser.get();
		
		 // Reject if BCrypt password match fails
		if (!BCrypt.checkpw(userLogin.getPassword(), user.getPassword())) {
			bindingResult.rejectValue("password", "invalid" , "Username or Password does not exist");
		}
		
		// Return null if result has errors
    	if (bindingResult.hasErrors()) {
    		return null;
    	}
    	else {
    		return user;
    	}
	}
}
