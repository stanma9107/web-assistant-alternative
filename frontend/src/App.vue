<template>
<div class="w-full flex flex-col items-center justify-center min-h-screen border-y-4 border-indigo-500 border-orange-700 bg-orange-100">
  <div class="w-[95%] lg:w-[60%] flex-1 h-full">
    <div class="navbar bg-orange-500 rounded my-4">
      <div class="flex-1">
        <a class="text-2xl font-bold">&nbsp;Web AI</a>
      </div>
      <div class="flex-none">
        <button class="btn btn-square btn-ghost">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-5 h-5 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z"></path></svg>
        </button>
      </div>
  </div>
    <div class="chat" v-for="message in messages" :key="message" :class="{
      'chat-start': message.type === 'outgoing',
      'chat-end': message.type === 'income',
    }">
      <div v-if="message.type === 'outgoing'">
        <div class="chat-bubble bg-orange-400 text-black">{{  message.message  }}</div>
      </div>
      <div v-else-if="message.type === 'income'">
        <div class="chat-bubble bg-white text-black border-solid border-2 border-indigo-500 border-orange-700">{{  message.message  }}</div>
      </div>
    </div>
  </div>
  <div class="w-[95%] lg:w-[60%] my-2 join">
    <input v-model="message" @keyup.enter="sendMessage" type="text" placeholder="Type here" class="input input-bordered input-error w-full join-item" />
    <button class="btn btn-square bg-orange-500 join-item" @click="sendMessage">
      <img src="/location-svgrepo-com.svg"/>
    </button>
  </div>
  <div class="w-[95%] lg:w-[60%] join flex items-center">
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="stroke-info shrink-0 w-6 h-6 join-item"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
    <span class="text-xs align-baseline">&nbsp;Web AI can make mistakes. Consider checking important information.</span>
  </div>

  
</div>

</template>

<script setup>
  import { ref } from 'vue'
  import './assets/style.css'
  import { fetchMessage } from '@/utils/request'
  const message = ref("")
  const messages = ref([])

  const sendMessage = async () => {
    try {
      messages.value.push({
        type: 'income',
        message: message.value,
      })
      const incomingMessage = await fetchMessage(message.value)
      messages.value.push({
        type: 'outgoing',
        message: incomingMessage,
      })
      message.value = ""
    }
    catch(error){
      alert("Server Error")
    }
  }
</script>
