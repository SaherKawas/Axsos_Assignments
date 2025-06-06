<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Save Travels</title>
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container py-5">
        <h1 class="text-center mb-4">Save Travels</h1>

        <!-- Table of Expenses -->
        <div class="card mb-5 shadow-sm">
            <div class="card-header bg-primary text-white">
                <h5 class="mb-0">Expense List</h5>
            </div>
            <div class="card-body p-0">
                <table class="table table-striped mb-0">
                    <thead class="table-dark">
                        <tr>
                            <th>Expense</th>
                            <th>Vendor</th>
                            <th>Amount</th>
                            <th colspan="2">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <c:forEach var="travel" items="${travels}">
                            <tr>
                                <td>
                                    <a href="/expenses/${travel.id}" class="text-decoration-none text-dark">
                                        ${travel.name}
                                    </a>
                                </td>
                                <td>${travel.vendor}</td>
                                <td>${travel.amount}</td>
                                <td>
                                    <a href="/edit/${travel.id}" class="btn btn-sm btn-warning">Edit</a>
                                </td>
                                <td>
                                    <a href="/delete/${travel.id}" class="btn btn-sm btn-danger"
                                       onclick="return confirm('Are you sure you want to delete this expense?');">
                                        Delete
                                    </a>
                                </td>
                            </tr>
                        </c:forEach>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Add New Expense Form -->
        <div class="card shadow">
            <div class="card-header bg-success text-white">
                <h5 class="mb-0">Add an Expense</h5>
            </div>
            <div class="card-body">
                <form:form action="/create" method="post" modelAttribute="saveTravels">
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

                    <button type="submit" class="btn btn-primary w-100">Submit</button>
                </form:form>
            </div>
        </div>
    </div>

    <!-- Optional Bootstrap JS Bundle -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>