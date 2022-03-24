<template>
    <div>
        <svg version="1.1" id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
            viewBox="0 0 350 350" enable-background="new 0 0 0 0" xml:space="preserve">
            <circle fill="#fc8019" stroke="none" cx="30%" cy="25%" r="15">
                <animate
                attributeName="opacity"
                dur="2s"
                values="0;1;0"
                repeatCount="indefinite"
                begin="0.1"/>    
            </circle>
            <circle fill="#fc8019" stroke="none" cx="50%" cy="25%" r="15">
                <animate
                attributeName="opacity"
                dur="2s"
                values="0;1;0"
                repeatCount="indefinite" 
                begin="0.2"/>       
            </circle>
            <circle fill="#fc8019" stroke="none" cx="70%" cy="25%" r="15">
                <animate
                attributeName="opacity"
                dur="2s"
                values="0;1;0"
                repeatCount="indefinite" 
                begin="0.3"/>     
            </circle>
        </svg>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    setup () {
        

        return {}
    }
})
</script>

<style scoped>

</style>