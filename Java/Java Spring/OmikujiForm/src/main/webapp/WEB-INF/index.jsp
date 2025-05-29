<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Form Input</title>
    <link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css" />
    <style>
        .form-container {
            max-width: 600px;
            margin: 30px auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        textarea {
            min-height: 100px;
        }
    </style>
</head>
<body class="bg-light">
    <div class="container">
        <div class="form-container bg-white">
            <h2 class="mb-4 text-center">Please Fill Out This Form</h2>
            <form action="/show" method="POST">
                <div class="mb-3">
                    <label for="quantity" class="form-label">Pick any number from 5 to 25</label>
                    <input type="number" class="form-control" id="quantity" name="quantity" min="5" max="25" required>
                </div>
                
                <div class="mb-3">
                    <label for="city" class="form-label">Enter the name of any city:</label>
                    <input type="text" class="form-control" name="city" required>
                </div>
                
                <div class="mb-3">
                    <label for="name" class="form-label">Enter the name of any real person:</label>
                    <input type="text" class="form-control" name="name" required>
                </div>
                
                <div class="mb-3">
                    <label for="hobby" class="form-label">Enter professional endeavor or hobby:</label>
                    <input type="text" class="form-control" name="hobby" required>
                </div>
                
                <div class="mb-3">
                    <label for="living" class="form-label">Enter any type of living thing:</label>
                    <input type="text" class="form-control" name="living" required>
                </div>
                
                <div class="mb-3">
                    <label for="nice" class="form-label">Say something nice to someone:</label>
                    <textarea class="form-control" name="nice" required></textarea>
                </div>
                
                <div class="d-grid">
                    <button type="submit" class="btn btn-primary">Send and show a friend</button>
                </div>
            </form>
        </div>
    </div>
</body>
</html>