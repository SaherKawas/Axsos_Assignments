<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ page isErrorPage="true" %> 
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Create Dojo</title>
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom CSS -->
    <style>
        body {
            background-color: #f8f9fa;
            padding: 20px;
        }
        .form-container {
            max-width: 500px;
            margin: 30px auto;
            padding: 30px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
        }
        .form-header {
            color: #0d6efd;
            margin-bottom: 20px;
            text-align: center;
            padding-bottom: 10px;
            border-bottom: 2px solid #0d6efd;
        }
        .form-label {
            font-weight: 500;
        }
        .error-message {
            color: #dc3545;
            font-size: 0.875em;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-md-8 mx-auto">
                <div class="form-container">
                    <h1 class="form-header">New Dojo</h1>
                    
                    <form:form action="/dojos/new" method="post" modelAttribute="dojo">
                        <div class="mb-3">
                            <form:label path="name" class="form-label">Dojo Name:</form:label>
                            <form:input path="name" class="form-control" />
                            <form:errors path="name" class="error-message" />
                        </div>
                        
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                            <input type="submit" value="Create Dojo" class="btn btn-primary"/>
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