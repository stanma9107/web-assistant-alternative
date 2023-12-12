import axios from 'axios'

export const fetchMessage = async function (message){
    const response = await axios.post('https://ihr2z62zo5.execute-api.us-east-1.amazonaws.com/prod/chat', {
        "message" : message,
        "meta" : true
    })
    return response.data.response
}

export const fetchIBMMessage = async (message, sessionId) => {
    const response = await axios.post("https://ihr2z62zo5.execute-api.us-east-1.amazonaws.com/prod/ibm", {
        "message": message,
        "session_id": sessionId,
    })
    return response.data;
}