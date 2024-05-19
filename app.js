const express = require("express");
const cors = require("cors");
const dotenv = require("dotenv");

dotenv.config();

const app = express();

app.use(
  cors({ //allows servers to specify not only who can access the assets, but also how they can be accessed
    origin: "*", // restrict calls to those this address
    credentials: true,
    methods: "GET,PUT,PATCH,POST,DELETE",
  })
);

const port = process.env.PORT || 5000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
