<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Burger Tracker</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="/css/style.css">
</head>
<body class="bg-light py-4">
    <div class="container">
        <h1 class="mb-4">🍔 Burger Tracker</h1>

        <!-- Table of Burgers -->
        <div class="card mb-5">
            <div class="card-header bg-primary text-white">Burger List</div>
            <div class="card-body p-0">
                <table class="table table-striped mb-0">
                    <thead class="table-dark">
                        <tr>
                            <th>Burger Name</th>
                            <th>Restaurant Name</th>
                            <th>Rating (out of 5)</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <c:forEach var="burger" items="${burgers}">
                            <tr>
                                <td>${burger.burgerName}</td>
                                <td>${burger.restaurantName}</td>
                                <td>
                                    <div class="rating">
                                        <c:forEach begin="1" end="5" var="i">
                                            <span style="color: ${i <= burger.rating ? 'orange' : 'lightgray'};">★</span>
                                        </c:forEach>
                                    </div>
                                </td>
                                <td>
                                    <a href="/edit/${burger.id}" class="btn btn-sm btn-outline-secondary">Edit</a>
                                </td>
                            </tr>
                        </c:forEach>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Add Burger Form -->
        <div class="card">
            <div class="card-header bg-success text-white">Add a Burger</div>
            <div class="card-body">
                <form:form action="/create" method="post" modelAttribute="burger">
                    <div class="mb-3">
                        <form:label path="burgerName" class="form-label">Burger Name</form:label>
                        <form:input path="burgerName" class="form-control"/>
                        <form:errors path="burgerName" class="text-danger"/>
                    </div>
                    <div class="mb-3">
                        <form:label path="restaurantName" class="form-label">Restaurant Name</form:label>
                        <form:textarea path="restaurantName" rows="2" class="form-control"/>
                        <form:errors path="restaurantName" class="text-danger"/>
                    </div>
                    <div class="mb-3">
                        <form:label path="rating" class="form-label">Rating (1-5)</form:label>
                        <form:input type="number" path="rating" min="1" max="5" class="form-control"/>
                        <form:errors path="rating" class="text-danger"/>
                    </div>
                    <div class="mb-3">
                        <form:label path="notes" class="form-label">Notes</form:label>
                        <form:input path="notes" class="form-control"/>
                        <form:errors path="notes" class="text-danger"/>
                    </div>
                    <div>
                        <button type="submit" class="btn btn-success">Add Burger</button>
                    </div>
                </form:form>
            </div>
        </div>
    </div>

    <!-- Bootstrap JS (optional) -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>