import React, { useEffect, useState } from 'react'
import axios from 'axios';
import { useParams, Link, useNavigate } from "react-router-dom";
    
const Detail = (props) => {
    const [product, setProduct] = useState({})
    const { id } = useParams();
    const navigate = useNavigate();
    
    useEffect(() => {
        axios.get(`http://localhost:8000/api/products/${id}`)
            .then(res => setProduct(res.data))
            .catch(err => console.error(err));
    }, [id]);

    const deleteProduct = () => {
    axios.delete('http://localhost:8000/api/products/' + id)
      .then(res => {
        console.log('Deleted:', res.data);
        navigate('/products'); // Go back to list after deletion
      })
      .catch(err => console.error(err));
  };
    
    return (
        <div>
            <h1>Product Details</h1>
            <p>Title: {product.title}</p>
            <p>Price: {product.price}</p>
            <p>Description: {product.description}</p>
            <Link to={"/products/" + product._id + "/edit"}>
                Edit
            </Link>
            <button onClick={deleteProduct}>Delete</button>
            <hr></hr>
            <Link to={"/products/"}>
                Home
            </Link>

        </div>
    )
}
export default Detail;