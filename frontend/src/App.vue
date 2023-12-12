<template>
<div class="w-full flex flex-col items-center justify-center min-h-screen border-y-4 border-orange-700 bg-orange-100">
  <div class="w-[95%] lg:w-[60%] flex-1 h-full">
    <div class="navbar bg-orange-500 rounded my-4">
      <div class="flex-1 text-white">
        <a class="text-2xl font-bold" v-if="mode == 'openai'">Web AI</a>
        <a class="text-2xl font-bold" v-else>Restaurant Bot</a>
      </div>
      <div class="dropdown dropdown-end">
        <div tabindex="0" role="button" class="btn btn-square btn-ghost m-1">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-5 h-5 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z"></path></svg>
        </div>
        <ul tabindex="0" class="dropdown-content z-[1] menu p-2 shadow bg-orange-400 text-white rounded-box w-52">
          <li v-show="mode == 'openai'" @click="changeMode('resaturant')"><a>Switch to Restaurant Bot</a></li>
          <li v-show="mode == 'resaturant'" @click="changeMode('openai')"><a>Switch to ChatGPT</a></li>
        </ul>
      </div>
    </div>
    <div class="chat" v-for="message in messages" :key="message" :class="{
      'chat-start': message.type === 'outgoing',
      'chat-end': message.type === 'income',
    }">
      <div v-if="message.type === 'outgoing'" class="chat-bubble bg-orange-400 text-black whitespace-pre-wrap">{{  message.message  }}</div>
      <div v-else-if="message.type === 'income'" class="chat-bubble bg-white text-black border-solid border-2 whitespace-pre-wrap">{{  message.message  }}</div>
    </div>
    <div class="w-full px-10 flex flex-row gap-x-4 max-w-full overflow-x-auto">
      <button class="btn rounded-full px-10 btn-accent" v-for="option in options" :key="option.title" @click="sendOptionValue(option.value.input.text, option.label)">
        {{  option.label  }}
      </button>
    </div>
  </div>
  <div class="w-[95%] lg:w-[60%] my-2 join">
    <input v-model="message" @keyup.enter="send" type="text" placeholder="Type here" class="input input-bordered input-error w-full join-item" />
    <button class="btn btn-square bg-orange-500 join-item" @click="send">
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
  import { fetchMessage, fetchIBMMessage } from '@/utils/request'
  const message = ref("")
  const messages = ref([])
  const mode = ref("openai")
  const session_id = ref(undefined)
  const options = ref([])

  const send = () => {
    if (mode.value == "openai") {
      sendMessage()
    } else {
      sendToIBM()
    }
  }

  const changeMode = (changedMode) => {
    mode.value = changedMode
  }

  const sendOptionValue = async (value, label) => {
    try {
      messages.value.push({
        type: "income",
        message: label,
      })

      const res = await fetchIBMMessage(value, session_id.value)
      for (const generic of res.generic) {
        console.log(generic)
        switch (generic.response_type) {
          case "text":
            messages.value.push({
              type: "outgoing",
              message: generic.text,
            })
            break;
          default:
            break;
        }
      }
      message.value = ""
      options.value = []
    } catch (error) {
      alert("Server Error")
    }
  }

  const sendToIBM = async () => {
    try {
      messages.value.push({
        type: "income",
        message: message.value,
      })
      const res = await fetchIBMMessage(message.value, session_id.value)
      session_id.value = res.session_id
      for (const generic of res.generic) {
        console.log(generic)
        switch (generic.response_type) {
          case "text":
            messages.value.push({
              type: "outgoing",
              message: generic.text,
            })
            break;
          case "option":
            messages.value.push({
              type: "outgoing",
              message: generic.title,
            })
            options.value = generic.options
            break;
          default:
            break;
        }
      }
      message.value = ""
    } catch (error) {
      console.log(error)
      alert("Server Error")
    }
  }

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
