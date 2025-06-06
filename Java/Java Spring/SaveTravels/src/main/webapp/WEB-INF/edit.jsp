<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Edit Expense</title>
    <!-- Bootstrap 5 CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <div class="card shadow">
            <div class="card-header bg-warning">
                <h2 class="mb-0">Edit Expense</h2>
            </div>
            <div class="card-body">
                <form:form action="/edit/${saveTravels.id}" method="post" modelAttribute="saveTravels">
                    <div class="mb-3">
                        <form:label path="name" cssClass="form-label">Expense</form:label>
                        <form:input path="name" cssClass="form-control"/>
                        <form:errors path="name" cssClass="text-danger"/>
                    </div>

                    <div class="mb-3">
                        <form:label path="vendor" cssClass="form-label">Vendor</form:label>
                        <form:input path="vendor" cssClass="form-control"/>
                        <form:errors path="vendor" cssClass="text-danger"/>
                    </div>

                    <div class="mb-3">
                        <form:label path="amount" cssClass="form-label">Amount</form:label>
                        <form:input type="number" path="amount" min="1" cssClass="form-control"/>
                        <form:errors path="amount" cssClass="text-danger"/>
                    </div>

                    <div class="mb-3">
                        <form:label path="description" cssClass="form-label">Description</form:label>
                        <form:textarea path="description" cssClass="form-control"/>
                        <form:errors path="description" cssClass="text-danger"/>
                    </div>

                    <div class="d-flex justify-content-between">
                        <a href="/" class="btn btn-secondary">Cancel</a>
                        <button type="submit" class="btn btn-primary">Update</button>
                    </div>
                </form:form>
            </div>
        </div>
    </div>
</body>
</html>