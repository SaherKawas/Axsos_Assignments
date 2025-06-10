<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Dojo Page</title>
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom CSS -->
    <style>
        body {
            padding: 20px;
            background-color: #f8f9fa;
        }
        .dojo-header {
            color: #0d6efd;
            margin-bottom: 30px;
            padding-bottom: 10px;
            border-bottom: 2px solid #0d6efd;
        }
        .table-container {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            padding: 20px;
        }
        .table thead th {
            background-color: #0d6efd;
            color: white;
        }
        .table-hover tbody tr:hover {
            background-color: rgba(13, 110, 253, 0.1);
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-md-10 mx-auto">
                <h1 class="dojo-header text-center"><c:out value="${dojo.name}"/> Ninjas</h1>
                
                <div class="table-container">
                    <table class="table table-hover table-striped">
                        <thead>
                            <tr>
                                <th scope="col">First Name</th>
                                <th scope="col">Last Name</th>
                                <th scope="col">Age</th>
                            </tr>
                        </thead>
                        <tbody>
                            <c:forEach var="ninja" items="${ninjas}">
                            <tr>
                                <td><c:out value="${ninja.firstName}"/></td>
                                <td><c:out value="${ninja.lastName}"/></td>
                                <td><c:out value="${ninja.age}"/></td>
                            </tr>
                            </c:forEach>
                        </tbody>
                    </table>
                </div>
                
                <div class="mt-4 text-center">
                    <a href="/dojos/new" class="btn btn-primary">Back to creating Dojos</a>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap 5 JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>