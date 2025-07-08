import React, {useState} from "react";
import { useNavigate } from "react-router-dom";

const Home = () => {
    const[resource, setResource]=useState("people")
    const [id, setId] = useState("");
    const navigate = useNavigate();

    const handleSubmit = (e) => {
    e.preventDefault();
    if (id.trim() !== "") {
      navigate(`/${resource}/${id}`);
    }
  };

    return(

        <>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="text">Search for:</label>
                    <select id="resource" value={resource} onChange={(e) => setResource(e.target.value)}>
                        <option value="people">People</option>
                        <option value="planets">Planets</option>
                    </select>
                </div>
                <div>
                    <label htmlFor="text">ID:</label>
                    <input type="text" value={id} onChange={(e) => setId(e.target.value)} />
                    <button type="submit">Search</button>
                </div>
            </form>
        </>
    )
}
export default Home;