import axios from 'axios'


export const fetchMessage = async function (message){
    const response = await axios.post('https://ihr2z62zo5.execute-api.us-east-1.amazonaws.com/prod/chat', {
        "message" : message,
        "meta" : true
    })
    return response.data.response
  }