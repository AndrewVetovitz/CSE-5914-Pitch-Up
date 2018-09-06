import React, { Component } from 'react';
import axios from 'axios';
import NavBar from './NavBar';
import './App.css';

class App extends Component {
    constructor() {
        super();
        this.state = {
            phrase: ''
        };
    }

    UNSAFE_componentWillMount() {
        axios.get('/hello')
            .then(response => {
                console.log(response);
                this.setState({phrase: response.data});
            });

        axios.get('/analyze')
            .then(response => {
                console.log(response);
            });
    }

    render() {
        return (
            <div>
                <NavBar/>
                {this.state.phrase}
            </div>
        );
    }
}

export default App;
