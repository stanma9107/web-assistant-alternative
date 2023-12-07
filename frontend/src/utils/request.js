import axios from 'axios'


export const fetchMessage = async function (message){
    const response = await axios.post('/chat', {
        "message" : message,
        "meta" : true
    })
    return response.data.response
  }