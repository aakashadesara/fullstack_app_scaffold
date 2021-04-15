import React, { Component } from "react";
import { GET, POST } from "../api/api";

class Sample extends Component {
  query = () => {
    GET("/search/", {
      val: this.state.queryVal,
    }).then((res) =>
      this.setState({
        queryResponse: res,
      })
    );
  };

  getAll = () => {
    GET("/nodes/").then((res) =>
      this.setState({
        getResponse: res,
      })
    );
  };

  post = () => {
    POST("/addnode/", { val: this.state.val }).then((res) => {
      this.setState({
        postResponse: res,
      });
    });
  };

  render() {
    return (
      <div style={{ width: "50%", margin: "0% auto", marginTop: "20px" }}>
        <div>
          <button onClick={this.getAll}>GET ALL</button>
          <p>Response: {JSON.stringify(this.state?.getResponse)}</p>
        </div>

        <hr></hr>

        <div>
          <input
            placeholder="value for new node"
            onChange={(e) =>
              this.setState({
                val: e.target.value,
              })
            }
          />
          <button onClick={this.post}>POST NEW NODE</button>
          <p>Response: {JSON.stringify(this.state?.postResponse)}</p>
        </div>

        <hr></hr>

        <div>
          <input
            placeholder="query by value for node"
            onChange={(e) =>
              this.setState({
                queryVal: e.target.value,
              })
            }
          />
          <button onClick={this.query}>QUERY FOR NODE</button>
          <p>Response: {JSON.stringify(this.state?.queryResponse)}</p>
        </div>
      </div>
    );
  }
}

export default Sample;
