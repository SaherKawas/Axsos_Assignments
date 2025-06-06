<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Burger Tracker</title>
</head>
<body>
	<div>
    <h2>Edit Burger</h2>
    <form:form action="/edit/${burger.id}" method="post" modelAttribute="burger">
        <div>
            <form:label path="burgerName">Burger Name</form:label><br/>
            <form:input path="burgerName"/>
            <form:errors path="burgerName"/>
        </div>
        <br/>
        <div>
            <form:label path="restaurantName">Restaurant Name</form:label><br/>
            <form:textarea path="restaurantName" rows="2"/>
            <form:errors path="restaurantName"/>
        </div>
        <br/>
        <div>
            <form:label path="rating">Rating (1-5)</form:label><br/>
            <form:input type="number" path="rating" min="1" max="5"/>
            <form:errors path="rating"/>
        </div>
        <br/>
        <div>
            <form:label path="notes">Notes</form:label><br/>
            <form:input path="notes"/>
            <form:errors path="notes"/>
        </div>
        <br/>
        <div>
            <button type="submit">Edit burger</button>
        </div>
    </form:form>
</div>
</body>
</html>