<template>
<div class="w-full flex flex-col items-center justify-center min-h-screen">
  <div class="w-[60%] flex-1 h-full">
    <div class="chat chat-start">

    <div class="chat-header">
      Obi-Wan Kenobi
      <time class="text-xs opacity-50">12:45</time>
    </div>
    <div class="chat-bubble">You were the Chosen One!</div>
    <div class="chat-footer opacity-50">
      Delivered
    </div>
    </div>
    <div class="chat chat-end">

    <div class="chat-header">
      Anakin
      <time class="text-xs opacity-50">12:46</time>
    </div>

    <div class="chat-bubble">I hate you!</div>
    <div class="chat-footer opacity-50">
      Seen at 12:46
    </div>
    </div>
    </div>
    <div class="w-[60%] my-2 join"> 
      <input type="text" placeholder="Type here" class="input input-bordered w-full join-item" />
      <button class="btn btn-square join-item">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
      </button>
    </div>
    
  </div>

</template>

<script>

export default {
  name: 'App',
}
</script>