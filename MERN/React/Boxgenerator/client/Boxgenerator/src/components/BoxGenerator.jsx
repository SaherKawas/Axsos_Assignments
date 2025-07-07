import React, { useState } from "react";

const BoxGenerator = () => {
  const [color, setColor] = useState("");
  const [boxes, setBoxes] = useState([]);

  const generateColor = (e) => {
    e.preventDefault();

    if (color.trim() === "") return;

    setBoxes([...boxes, color]); 
    setColor(""); 
  };

  return (
    <div>
      <form onSubmit={generateColor}>
        <div>
          <label>Color: </label>
          <input
            type="text"
            value={color}
            onChange={(e) => setColor(e.target.value)}
          />
        </div>
        <input type="submit" value="Add" />
      </form>

      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
          marginTop: "20px",
          gap: "10px"
        }}
      >
        {boxes.map((boxColor, idx) => (
          <div
            key={idx}
            style={{
              backgroundColor: boxColor,
              width: "100px",
              height: "100px",
              border: "1px solid #000"
            }}
          ></div>
        ))}
      </div>
    </div>
  );
};
export default BoxGenerator;