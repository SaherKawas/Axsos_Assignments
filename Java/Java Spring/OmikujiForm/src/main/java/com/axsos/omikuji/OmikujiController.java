package com.axsos.omikuji;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import jakarta.servlet.http.HttpSession;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class OmikujiController {
    
    @RequestMapping("/")
    public String index() {
        return "index.jsp";
    }
    
    @RequestMapping(value="/show", method=RequestMethod.POST)
    public String show(HttpSession session,
        @RequestParam(value="quantity") Integer quantity,
        @RequestParam(value="city") String city, 
        @RequestParam(value="name") String name,
        @RequestParam(value="hobby") String hobby,
        @RequestParam(value="living") String living, 
        @RequestParam(value="nice") String nice) {
        
        session.setAttribute("quantity", quantity);
        session.setAttribute("city", city);
        session.setAttribute("name", name);
        session.setAttribute("hobby", hobby);
        session.setAttribute("living", living);
        session.setAttribute("nice", nice);
        
        return "redirect:/show";
    }
    
    @RequestMapping("/show")
    public String showFortune() {
        return "show.jsp";
    }
}