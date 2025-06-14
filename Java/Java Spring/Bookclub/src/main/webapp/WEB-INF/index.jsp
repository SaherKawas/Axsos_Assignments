<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ page isErrorPage="true" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Read Share</title>
</head>
<body>
	<h1>Book Club</h1>
	<p>A place for friends to share thoughts about books.</p>
	<h1>Register</h1>
	<form:form action="/usersignup" method="post" modelAttribute="userSignup">
	    <p>
	        <form:label path="name">Name:</form:label>
	        <form:errors path="name"/>
	        <form:input path="name"/>
	    </p>
	    <p>
	        <form:label path="email">Email:</form:label>
	        <form:errors path="email"/>
	        <form:input path="email"/>
	    </p>
	     <p>
	        <form:label path="password">Password:</form:label>
	        <form:errors path="password"/>
	        <form:input path="password" type="password"/>
	    </p>
	    <p>
	        <form:label path="confirmPassword">Confirm Password:</form:label>
	        <form:errors path="confirmPassword"/>
	        <form:input path="confirmPassword" type="password"/>
	    </p>
	    <input type="submit" value="Submit"/>
	</form:form>
	
	<h1>Login</h1>
		<form:form action="/userlogin" method="post" modelAttribute="userLogin">
	    <p>
	        <form:label path="email">Email:</form:label>
	        <form:errors path="email"/>
	        <form:input path="email"/>
	    </p>
	     <p>
	        <form:label path="password">Password:</form:label>
	        <form:errors path="password"/>
	        <form:input path="password" type="password"/>
	    </p>
	    <input type="submit" value="Submit"/>
	</form:form>
</body>
</html>