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
	<h1>Change your entry</h1>
	<a href="/books">Back to the shelves</a>
	<form:form action="/books/${book.id}/editing" method="post" modelAttribute="book">
	    <p>
	        <form:label path="title">Title:</form:label>
	        <form:errors path="title"/>
	        <form:input path="title"/>
	    </p>
	    <p>
	        <form:label path="author">Author:</form:label>
	        <form:errors path="author"/>
	        <form:input path="author"/>
	    </p>
	     <p>
	        <form:label path="thoughts">My thoughts:</form:label>
	        <form:errors path="thoughts"/>
	        <form:textarea path="thoughts"/>
	    </p>
	    <input type="submit" value="Update"/>
	</form:form>
</body>
</html>