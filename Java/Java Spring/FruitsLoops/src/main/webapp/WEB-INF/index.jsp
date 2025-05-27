<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>

    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Fruit Store</title>
<link rel="stylesheet" type="text/css" href="/css/style.css">
</head>
<body>
	<h1>Fruit Store</h1>
	<table>
        <tr>
            <th>Name</th>
            <th>Price</th>
        </tr>
        <c:forEach var="storeFruit" items="${fruitStore}">
	        <tr>
	            <td><c:out value="${storeFruit.name}"></c:out></td>
	            <td><c:out value="${storeFruit.price}"></c:out></td>  
	        </tr>
        </c:forEach>
    </table>
</body>
</html>