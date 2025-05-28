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
	<h1>Here is your Omikuji</h1>
   	<p>In <c:out value="${quantity}"/> years, you will live in <c:out value="${city}"/> with <c:out value="${name}"/> as your roommate, <c:out value="${hobby}"/> for a living. The next time you see a <c:out value="${living}"/>, you will have good luck. <c:out value="${nice}"/></p>
   	<a href="/">Go back</a>
</body>
</body>
</html>