package com.axsos.loginregister.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.axsos.loginregister.models.LoginRegister;
import com.axsos.loginregister.models.LoginUser;
import com.axsos.loginregister.services.LoginRegisterService;

import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;

@Controller
public class LoginRegisterController {
	
	@Autowired
	private LoginRegisterService loginRegisterService;
	
	@GetMapping("/")
	public String index(Model model, @ModelAttribute("userLogin") LoginUser userLogin, @ModelAttribute("userSignup") LoginRegister user ) {
	     model.addAttribute("userLogin", new LoginUser());
	     model.addAttribute("userSignup", new LoginRegister() );
		 return "index.jsp";
	}
	@PostMapping("/userlogin")
	public String login(@Valid @ModelAttribute("userLogin") LoginUser userLogin ,BindingResult result,HttpSession session ,Model model) {
		LoginRegister userlogged = loginRegisterService.login(userLogin, result);
		if (result.hasErrors()) {
			model.addAttribute("userSignup", new LoginRegister());
    		return "index.jsp";
		}
		else {
			session.setAttribute("loggedUser", userlogged);
    		return "redirect:/welcome";
		}
	}
	
	@GetMapping("/welcome")
	public String home(HttpSession session, Model model) {
        if (session.getAttribute("loggedUser") != null) {
        	return "welcome.jsp";
        }
        else {
            return "redirect:/";
        }
	}
	
	@PostMapping("/usersignup")
	public String signUp(@Valid @ModelAttribute("userSignup") LoginRegister user, BindingResult result, HttpSession session , Model model) {
		LoginRegister signedUpUser = loginRegisterService.register( user , result);
		if ( result.hasErrors()) {
			model.addAttribute("userLogin", new LoginUser());
			return "index.jsp";
		}else {
    		session.setAttribute("loggedUser", signedUpUser);
    		return "redirect:/welcome";
    	}	
	}
	
	 @GetMapping("/logout")
	    public String logout(HttpSession session) {
	        session.invalidate();
	        return "redirect:/";
	    }
}
