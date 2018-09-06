const express = require('express');
const path = require('path');
const app = express();

const port = process.env.PORT || 5000;

app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

app.get('/hello', (req, res) => {
    res.send('hello');
});

app.get('/analyze', (req, res) => {
    const response =
        {
            "bad": 3,
            "good": 5
        };

    res.send(response);
});

app.listen(port, () => {
    console.log('Server started on port %s', port);
});