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
	<a href="/books">Back to the shelves</a>
	<h1><c:out value="${book.title}"/></h1>
	<p><c:out value="${book.user.name}"/> read <c:out value="${book.title}"/> by <c:out value="${book.author}"/>.</p>
	<p><c:out value="Here are ${book.user.name}'s thoughts"/></p>
	<textarea rows="" cols=""><c:out value="${book.thoughts}"/></textarea>
	

	<c:if test="${book.user.id == userId}">
			<a href="/books/${book.id}/edit">Edit</a>
			<form action="/books/${book.id}/delete" method="post">
				<button>Delete</button>
			</form>
		</c:if>
</body>
</html>