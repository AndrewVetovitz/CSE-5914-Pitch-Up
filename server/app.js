const express = require('express');
const path = require('path');
const app = express();

const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
    res.send('hello');
});

app.listen(port, () => {
    console.log('Example app listening on port 3000!');
});