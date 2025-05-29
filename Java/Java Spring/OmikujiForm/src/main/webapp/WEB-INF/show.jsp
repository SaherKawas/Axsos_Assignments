<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Omikuji Result</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light text-dark">
    <div class="container mt-5">
        <div class="card shadow">
            <div class="card-body">
                <h1 class="card-title text-primary">Here is your Omikuji</h1>
                <p class="bg-primary text-white p-4 rounded">
				    In <strong><c:out value="${quantity}"/></strong> years, you will live in 
				    <strong><c:out value="${city}"/></strong> with 
				    <strong><c:out value="${name}"/></strong> as your roommate, 
				    doing <strong><c:out value="${hobby}"/></strong> for a living. 
				    The next time you see a <strong><c:out value="${living}"/></strong>, 
				    you will have good luck. 
				    <strong><c:out value="${nice}"/></strong>
				</p>
                <a href="/" class="btn btn-secondary mt-3">Go back</a>
            </div>
        </div>
    </div>
</body>
</html>