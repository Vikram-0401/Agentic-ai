const express = require("express");

const PORT = process.env.PORT ? +process.env.PORT : 8000;

const app = express();

app.get("/", (req, res) => {
  return res.json({
    status: "Success",
    message: "Hello from express server",
  });
});

app.listen(PORT, () => console.log(`Server started on PORT ${PORT}`));

