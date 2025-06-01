<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="/css/style.css">
    <title>Burger trackers</title>
</head>
<body class="bg-light">
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card shadow">
                    <div class="card-header bg-primary text-white">
                        <h1 class="h3 mb-0">Burger Tracker</h1>
                    </div>
                    <div class="card-body">
                        <div class="table-responsive">
                            <table class="table table-striped table-hover">
                                <thead class="table-dark">
                                    <tr>
                                        <th>Burger Name</th>
                                        <th>Restaurant Name</th>
                                        <th>Rating (out of 5)</th>
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
                                                        <span class="star ${i <= burger.rating ? 'text-warning' : 'text-secondary'}">★</span>
                                                    </c:forEach>
                                                </div>
                                            </td>
                                        </tr>
                                    </c:forEach>
                                </tbody>
                            </table>
                        </div>
                        
                        <div class="mt-5">
                            <h2 class="h4 mb-4">Add a Burger</h2>
                            <form:form action="/create" method="post" modelAttribute="burger" class="needs-validation" novalidate="novalidate">
                                <div class="mb-3">
                                    <form:label path="burgerName" class="form-label">Burger Name</form:label>
                                    <form:input path="burgerName" class="form-control ${not empty burgerNameError ? 'is-invalid' : ''}"/>
                                    <form:errors path="burgerName" class="invalid-feedback"/>
                                </div>
                                <div class="mb-3">
                                    <form:label path="restaurantName" class="form-label">Restaurant Name</form:label>
                                    <form:textarea path="restaurantName" class="form-control ${not empty restaurantNameError ? 'is-invalid' : ''}" rows="2"/>
                                    <form:errors path="restaurantName" class="invalid-feedback"/>
                                </div>
                                <div class="mb-3">
                                    <form:label path="rating" class="form-label">Rating (1-5)</form:label>
                                    <form:input type="number" path="rating" min="1" max="5" class="form-control ${not empty ratingError ? 'is-invalid' : ''}"/>
                                    <form:errors path="rating" class="invalid-feedback"/>
                                </div>
                                <div class="mb-3">
                                    <form:label path="notes" class="form-label">Notes</form:label>
                                    <form:input path="notes" class="form-control ${not empty notesError ? 'is-invalid' : ''}"/>
                                    <form:errors path="notes" class="invalid-feedback"/>
                                </div>
                                <div class="d-grid">
                                    <button type="submit" class="btn btn-primary btn-lg">Add a burger</button>
                                </div>
                            </form:form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    
    <!-- Optional: Add some custom styling for the stars -->
    <style>
        .rating {
            font-size: 1.2em;
        }
        .star {
            margin-right: 2px;
        }
    </style>
</body>
</html>