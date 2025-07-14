const express = require('express');
const cors = require('cors');
const app = express();
require('./config/mongoose.config');

app.use(cors())
const port = process.env.PORT;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
require('./routes/product.routes')(app);

const PORT = process.env.PORT || 8000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});