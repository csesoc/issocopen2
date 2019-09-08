import React,{Component} from 'react';
import axios from 'axios';
import Emoji from './Emoji'

export default class RoomStatus extends Component{

	constructor(props){
		super(props);
		this.state = {
			roomStatus: "Loading",
			doorStatus : "Loading",
			isEmpty : "Loading",
		};
	}

	componentDidMount(){
    axios({
      method: 'get',
      url: 'http://localhost:5000/api',
    }).then((response) => {
      console.log(response)
      this.setState(response.data);
    });
  }

	//
	render(){
		return (
			<div>
				<h2><Emoji symbol="🤔"/>Is socs office open?<Emoji symbol="🤔"/></h2>
				<h1>{this.state.roomStatus}</h1>
				<h3><Emoji symbol="🚪"/> Is the door open? <Emoji symbol="🚪"/></h3>
        <h2>{this.state.doorStatus}</h2>
        <h3><Emoji symbol="⏳"/> Has anyone moved in the room recently? <Emoji symbol="⏳"/></h3>
        <h2>{this.state.isEmpty}</h2>
			</div>
		)
	}
}