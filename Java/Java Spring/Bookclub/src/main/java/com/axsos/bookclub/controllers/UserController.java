package com.axsos.bookclub.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.axsos.bookclub.models.LoginUser;
import com.axsos.bookclub.models.User;
import com.axsos.bookclub.services.BookService;
import com.axsos.bookclub.services.UserService;

import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;

@Controller
public class UserController {
	@Autowired
	private UserService userService;
	
	@Autowired
	private BookService bookService;
	
	@GetMapping("/")
	public String index(Model model, @ModelAttribute("userLogin") LoginUser userLogin, @ModelAttribute("userSignup") User user ) {
	     model.addAttribute("userLogin", new LoginUser());
	     model.addAttribute("userSignup", new User() );
		 return "index.jsp";
	}
	
	@PostMapping("/userlogin")
	public String login(@Valid @ModelAttribute("userLogin") LoginUser userLogin ,BindingResult result,HttpSession session ,Model model) {
		User userlogged = userService.login(userLogin, result);
		if (result.hasErrors()) {
			model.addAttribute("userSignup", new User());
    		return "index.jsp";
		}
		else {
			session.setAttribute("loggedUser", userlogged);
    		return "redirect:/books";
		}
	}
	
	
	
	@PostMapping("/usersignup")
	public String signUp(@Valid @ModelAttribute("userSignup") User user, BindingResult result, HttpSession session , Model model) {
		User signedUpUser = userService.register( user , result);
		if ( result.hasErrors()) {
			model.addAttribute("userLogin", new LoginUser());
			return "index.jsp";
		}else {
    		session.setAttribute("loggedUser", signedUpUser);
    		return "redirect:/books";
    	}	
	}
	@GetMapping("/books")
	public String home(HttpSession session, Model model) {
        if (session.getAttribute("loggedUser") != null) {
        	model.addAttribute("books", bookService.allBooks());
        	return "books.jsp";
        }
        else {
            return "redirect:/";
        }
	}
	
	
	 @GetMapping("/logout")
	    public String logout(HttpSession session) {
	        session.invalidate();
	        return "redirect:/";
	    }

}
