<template>
<div class="w-full flex flex-col items-center justify-center min-h-screen">
  <div class="w-[95%] lg:w-[60%] flex-1 h-full">
    <div class="chat" v-for="message in messages" :key="message" :class="{
      'chat-start': message.type === 'outgoing',
      'chat-end': message.type === 'income',
    }">
      <div class="chat-bubble">{{  message.message  }}</div>
    </div>
  </div>
  <div class="w-[95%] lg:w-[60%] my-2 join">
    <input v-model="message" type="text" placeholder="Type here" class="input input-bordered w-full join-item" />
    <button class="btn btn-square join-item" @click="sendMessage">
      <img
        src="/location-svgrepo-com.svg"
      />
    </button>
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