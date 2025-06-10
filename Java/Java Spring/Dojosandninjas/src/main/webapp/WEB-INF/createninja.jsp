<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Create Ninja</title>
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom CSS -->
    <style>
        body {
            background-color: #f8f9fa;
            padding: 20px;
        }
        .form-container {
            max-width: 600px;
            margin: 30px auto;
            padding: 30px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
        }
        .form-header {
            color: #dc3545; /* Red color for ninja theme */
            margin-bottom: 25px;
            text-align: center;
            padding-bottom: 10px;
            border-bottom: 2px solid #dc3545;
        }
        .form-label {
            font-weight: 500;
            margin-bottom: 5px;
        }
        .error-message {
            color: #dc3545;
            font-size: 0.875em;
            margin-top: 5px;
        }
        .btn-ninja {
            background-color: #dc3545;
            border-color: #dc3545;
        }
        .btn-ninja:hover {
            background-color: #bb2d3b;
            border-color: #b02a37;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-md-8 mx-auto">
                <div class="form-container">
                    <h1 class="form-header">New Ninja</h1>
                    
                    <form:form action="/ninjas/new" method="post" modelAttribute="ninja">
                        <!-- Dojo Selection -->
                        <div class="mb-3">
                            <form:label path="dojo" class="form-label">Dojo:</form:label>
                            <form:select path="dojo" class="form-select">
                                <option value="" disabled selected>Select a Dojo</option>
                                <c:forEach var="oneDojo" items="${dojos}">
                                    <form:option value="${oneDojo.id}">
                                        <c:out value="${oneDojo.name}"/>
                                    </form:option>
                                </c:forEach>
                            </form:select>
                            <form:errors path="dojo" class="error-message" />
                        </div>
                        
                        <!-- First Name -->
                        <div class="mb-3">
                            <form:label path="firstName" class="form-label">First Name:</form:label>
                            <form:input path="firstName" class="form-control" />
                            <form:errors path="firstName" class="error-message" />
                        </div>
                        
                        <!-- Last Name -->
                        <div class="mb-3">
                            <form:label path="lastName" class="form-label">Last Name:</form:label>
                            <form:input path="lastName" class="form-control" />
                            <form:errors path="lastName" class="error-message" />
                        </div>
                        
                        <!-- Age -->
                        <div class="mb-4">
                            <form:label path="age" class="form-label">Age:</form:label>
                            <form:input path="age" type="number" class="form-control" />
                            <form:errors path="age" class="error-message" />
                        </div>
                        
                        <!-- Buttons -->
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                            <button type="submit" class="btn btn-ninja text-white">Register Ninja</button>
                        </div>
                    </form:form>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap 5 JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>