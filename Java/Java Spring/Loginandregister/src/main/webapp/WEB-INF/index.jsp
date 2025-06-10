<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ page isErrorPage="true" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Login and Registration</title>
</head>
<body>
	<h1>Welcome!</h1>
	<p>Join our growing community.</p>
	<h1>Register</h1>
	<form:form action="/usersignup" method="post" modelAttribute="userSignup">
	    <p>
	        <form:label path="username">User name:</form:label>
	        <form:errors path="username"/>
	        <form:input path="username"/>
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