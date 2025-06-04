<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
    
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title><c:out value="${book.title}"/> - Book Details</title>
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Bootstrap Icons -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css">
    <style>
        .book-detail-card {
            max-width: 800px;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            border: none;
        }
        .book-header {
            background-color: #f8f9fa;
            border-bottom: 1px solid #eee;
        }
        .detail-item {
            margin-bottom: 1rem;
        }
        .detail-label {
            font-weight: 600;
            color: #495057;
        }
    </style>
</head>
<body class="bg-light">
    <div class="container py-5">
        <div class="row justify-content-center">
            <div class="col-lg-8">
                <div class="card book-detail-card mb-4">
                    <div class="card-header book-header py-3">
                        <h1 class="h2 mb-0">
                            <i class="bi bi-book me-2"></i>
                            <c:out value="${book.title}"/>
                        </h1>
                    </div>
                    <div class="card-body">
                        <div class="detail-item">
                            <h3 class="h5 detail-label">Description</h3>
                            <p class="lead"><c:out value="${book.description}"/></p>
                        </div>
                        
                        <div class="row">
                            <div class="col-md-6">
                                <div class="detail-item">
                                    <h3 class="h5 detail-label">Language</h3>
                                    <p><span class="badge bg-primary"><c:out value="${book.language}"/></span></p>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="detail-item">
                                    <h3 class="h5 detail-label">Number of Pages</h3>
                                    <p><i class="bi bi-file-text me-2"></i><c:out value="${book.numberOfPages}"/></p>
                                </div>
                            </div>
                        </div>
                        
                        <div class="mt-4">
                            <a href="/books" class="btn btn-outline-primary">
                                <i class="bi bi-arrow-left me-1"></i> Back to All Books
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap 5 JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>