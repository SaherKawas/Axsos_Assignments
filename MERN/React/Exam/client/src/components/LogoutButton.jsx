import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const LogoutButton = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    axios.post('http://localhost:8000/api/logout', {}, { withCredentials: true })
      .then(() => {
        navigate('/');  
      })
      .catch(err => {
        console.error("Logout failed:", err);
      });
  };

  return <button onClick={handleLogout}>Logout</button>;
};

export default LogoutButton;
