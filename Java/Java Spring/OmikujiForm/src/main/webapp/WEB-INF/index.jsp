<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	 <form action="/show" method="POST">
        <label for="text">Pick any number from 5 to 25</label>
        <input type="number" id="quantity" name="quantity" min="5" max="25">
        <label for="city">Enter the name of any city:</label>
        <input type="text" name="city">
        <label for="name">Enter the name of any real person:</label>
        <input type="text" name="name">
        <label for="hobby">Enter professional endeavor or hobby:</label>
        <input type="text" name="hobby">
        <label for="living">Enter any type of living thing</label>
        <input type="text" name="living">
        <label for="nice">Say something nice to someone:</label>
        <textarea name="nice"></textarea>
        <label for="send">Send and show a friend</label>
        <button>Send</button>
    </form>
</body>
</html>