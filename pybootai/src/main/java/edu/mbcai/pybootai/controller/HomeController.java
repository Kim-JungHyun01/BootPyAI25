package edu.mbcai.pybootai.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class HomeController {

//  http://localhost:80/
    @GetMapping("/")
    public String home(){
        return "index"; // resources/templates/index.html을 찾아감
    }//end home -> 테스트 완료
    



}//end class
