import React, { Component } from "react";
import "./App.css";

import { BrowserRouter, Switch, Route } from "react-router-dom";
import Sample from "./components/Sample";

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route exact path="/">
            <Sample />
          </Route>
        </Switch>
      </BrowserRouter>
    );
  }
}

export default App;
