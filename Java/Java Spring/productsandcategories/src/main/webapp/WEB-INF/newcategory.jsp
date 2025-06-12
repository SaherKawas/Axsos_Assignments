<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page isErrorPage="true" %>
<!DOCTYPE html>
<html>
<head>
<title>New Category</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="container mt-5">
<a href="/" class="btn btn-outline-primary mb-3">Home</a>
<h1 class="mb-4">New Category</h1>
<form:form action="/category/form" method="post" modelAttribute="category" class="w-50">
<div class="mb-3">
<form:label path="name" class="form-label">Name:</form:label>
<form:input path="name" class="form-control" />
<form:errors path="name" class="text-danger" />
</div>
<button type="submit" class="btn btn-success">Create</button>
</form:form>
</body>
</html>