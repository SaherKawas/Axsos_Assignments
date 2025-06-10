<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>


<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Expense Details</title>
    <!-- Bootstrap 5 CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <div class="card shadow-sm">
            <div class="card-header bg-primary text-white">
                <h2 class="mb-0">Expense Details</h2>
            </div>
            <div class="card-body">
                <p><strong>Expense Name:</strong> <c:out value="${travel.name}"/></p>
                <p><strong>Description:</strong> <c:out value="${travel.description}"/></p>
                <p><strong>Vendor:</strong> <c:out value="${travel.vendor}"/></p>
                <p><strong>Amount Spent:</strong> $<c:out value="${travel.amount}"/></p>
            </div>
            <div class="card-footer">
                <a href="/" class="btn btn-secondary">← Back to List</a>
            </div>
        </div>
    </div>
</body>
</html>