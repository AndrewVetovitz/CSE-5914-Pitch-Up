import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
    constructor(){
        super();
        this.state = {
            phrase: ''
        };
    }

    UNSAFE_componentWillMount(){
        fetch('http://localhost:5000/').then(response => {
            return response.text();
        }).then(data => {
            this.setState({phrase: data});
        })
    }

    render() {
        return (
            <div className="App">
                <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <h1 className="App-title">Welcome to React</h1>
                </header>
                <p className="App-intro">
                    {this.state.phrase}
                </p>
            </div>
        );
  }
}

export default App;
