import { http, HttpResponse } from 'msw'

export default [
  http.post('/chat', async ({ request }) => {
    const requestBody = await request.json()
    return HttpResponse.json({
      response: requestBody.message,
    })
  })
]