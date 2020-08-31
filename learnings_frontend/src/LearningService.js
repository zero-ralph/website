import axios from 'axios';
const API_URL = 'http://api.localhost:8000/learnings';


export default class LearningService{

    get_all_learnings(){
        const url = `${API_URL}`;
        return axios.get(url).then(response => response.data)
    }
}