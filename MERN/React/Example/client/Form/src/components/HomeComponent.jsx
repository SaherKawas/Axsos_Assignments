import React, { useState } from  'react';
    
const HomeComponent = (props) => {
    const [firstName, setFirstName] = useState("");
    const [firstNameError, setFirstNameError]= useState("");

    const [lastName, setLastName] = useState("");
    const [lastNameError, setLastNameError]= useState("");

    const [email, setEmail] = useState("");
    const [emailError, setEmailError]= useState("");

    const [password, setPassword] = useState("");
    const [passwordError, setPasswordError]= useState(""); 

    const [confirmPassword, setConfirmPassword] = useState("");
    const [confirmPasswordError, setConfirmPasswordError]= useState("");

    const handleFirstName = (e) =>{
        setFirstName(e.target.value);
        if (e.target.value.length<1){
            setFirstNameError("First Name is required");
        } else if (e.target.value.length<4){
            setFirstNameError("First Name must be 4 characters or longer!")
        } else {
            setFirstNameError("");
        }
    }

    const handleLastName = (e) =>{
        setLastName(e.target.value);
        if (e.target.value.length<1){
            setLastNameError("Last Name is required");
        } else if (e.target.value.length<4){
            setLastNameError("Last Name must be 4 characters or longer!")
        } else {
            setLastNameError("");
        }
    }

    const handleEmail = (e) =>{
        setEmail(e.target.value);
        if (e.target.value.length<1){
            setEmailError("Email is required");
        } else if (e.target.value.length<5){
            setEmailError("Email must be 5 characters or longer!")
        } else {
            setEmailError("");
        }
    }

    const handlePassword = (e) =>{
        setPassword(e.target.value);
        if (e.target.value.length<1){
            setPasswordError("Password is required");
        } else if (e.target.value.length<8){
            setPasswordError("Password must be at least 8 characters or more!")
        } else {
            setPasswordError("");
        }
    }

    const handleConfirmPassword = (e) => {
        const value = e.target.value;
        setConfirmPassword(value);

        if (value.length < 1) {
            setConfirmPasswordError("Password is required");
        } else if (value.length < 8) {
            setConfirmPasswordError("Password must be at least 8 characters or more!");
        } else if (value !== password) {
            setConfirmPasswordError("Passwords must match!");
        } else {
            setConfirmPasswordError("");
        }
    };
    
    const createUser = (e) => {
        e.preventDefault();
        
        const newUser = { firstName, lastName, email, password, confirmPassword };
        console.log("Welcome", newUser);
        setFirstName("");
        setLastName("");
        setEmail("");
        setPassword("");
        setConfirmPassword("");
        setFirstNameError("");
        setLastNameError("");
        setEmailError("");
        setPasswordError("");
        setConfirmPasswordError("");
    };
    
    return(
        <form onSubmit={ createUser }>
            <div>
                <label>First Name: </label> 
                <input type="text" value={firstName} onChange={ handleFirstName } />
                {
                    firstNameError?
                    <p>{firstNameError}</p>:
                    ''
                }
            </div>
           
            <div>
                <label>Last Name: </label> 
                <input type="text" value={lastName} onChange={ handleLastName } />
            {
                lastNameError ?
                <p>{lastNameError}</p> :
                ''
            }
            </div>
            <div>
                <label>Email Address: </label> 
                <input type="text" value={email} onChange={ handleEmail } />
            {
                emailError ?
                <p>{emailError}</p> :
                ''
            }
            </div>
            <div>
                <label>Password: </label>
                <input type="password" value={password} onChange={ handlePassword } />
            {
                passwordError ?
                <p>{passwordError}</p> :
                ''
            }
            </div>
            <div>
                <label>Confirm Password: </label>
                <input type="password" value={confirmPassword} onChange={ handleConfirmPassword } />
            {
                confirmPasswordError ?
                <p>{confirmPasswordError}</p> :
                ''
            }
            </div>
            {
                <input type="submit" value="Create User" disabled={
                firstNameError || lastNameError || emailError ||passwordError ||confirmPasswordError
                }/>
            }
            
        </form>
    );
};
    
export default HomeComponent;