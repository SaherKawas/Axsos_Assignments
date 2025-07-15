import React, { useEffect, useState } from 'react'
import ProductForm from '../components/ProductForm';
import ProductList from '../components/ProductList';
import axios from 'axios';
    
const Main = () => {
    const [products, setProducts] = useState([]);
    
    
    useEffect(()=>{
        axios.get('http://localhost:8000/api/products')
            .then(res=>{
                setProducts(res.data);
                
            })
            .catch(err => console.error(err));
    },[]);

    const removeFromDom = productId => {
            setProducts(products.filter(product => product._id !== productId));
        }
    
    return (
        <div>
           <ProductForm products={products} setProducts={setProducts}/>
           <hr/>
           <ProductList products={products} removeFromDom={removeFromDom}/>
        </div>
    )
}
    
export default Main;