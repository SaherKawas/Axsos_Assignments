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
	<h1>Welcome, <c:out value="${loggedUser.name}"/></h1>
	<p>Books from everyone's shelves</p>
	<a href="/addbook">+ Add to my shelf</a>
	
	<table>
        <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Author</th>
            <th>Posted by</th>
        </tr>
        <c:forEach var="book" items="${books}">
	        <tr>
	        	<td><c:out value="${book.id}"/></td>
	            <td><a href="/books/${book.id}"><c:out value="${book.title}"/></a></td>
		        <td><c:out value="${book.author}"/></td>
	            <td><c:out value="${book.user.name}"></c:out></td>  
	        </tr>
        </c:forEach>
    </table>
	<a href="/logout">Log out</a>

</body>
</html>