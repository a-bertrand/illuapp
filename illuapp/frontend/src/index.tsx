import React, { Component } from "react"
import {render} from "react-dom"
import BasicCard from "./CardTest.tsx";

export default class App extends Component{
    constructor(props) {
        super(props);
    }

    render(){
        return <div>
            <Toot />
            <BasicCard />
            <p style={{color:'red'}}>This is what we will see in our application!</p>
        </div>
    }
}

const Toot = () => {
    return (
        <>Coucou</>
    )
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);