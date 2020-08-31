import axios from 'axios';
import React, { Component } from 'react';
//import LearningService from './LearningService';

//const learning_service = new LearningService();


class LearningList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            learnings: [],
        };
    }

    componentDidMount(){
        let self = this
        axios.get('http://api.localhost:8000/learnings', {})
        .then((response) => {
            console.log(response.data);
            self.setState({learnings: response.data})
        }).catch((err) => {
            console.log(err);
        });
    }

    render() {
        return (
            <section>
                {this.state.learnings.map(learning => 
                    <div>
                        <h1>{learning.id}</h1>
                        <h1>{learning.title}</h1>
                        <h1>{learning.description}</h1>
                    <h1></h1>
                    </div>
                )}
            </section>
        );
    }
    
}

export default LearningList;