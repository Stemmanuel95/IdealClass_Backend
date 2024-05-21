const express = require("express");
const morgan = require("morgan");
const cors = require("cors");
const dotenv = require("dotenv");

dotenv.config();

const app = express();

// Middleware
app.use(morgan("dev"));
app.use(express.json());
app.use(
  cors({ //allows servers to specify not only who can access the assets, but also how they can be accessed
    origin: "*", // restrict calls to those this address
    credentials: true,
    methods: "GET,PUT,PATCH,POST,DELETE",
  })
);

// Routes
app.get("/", (req, res) => {
  res.json({ message: "Welcome to my app!" });
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
