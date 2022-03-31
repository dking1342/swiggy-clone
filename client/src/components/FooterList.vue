<template>
    <div class="footer-col top-col">
        <h1>{{ payload.title}}</h1>
        <ul>
            <li v-for="item in payload.list" :key="item.link"><a href="#">{{item.link}}</a></li>
        </ul>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    props:{
        payload:Object,
    },
    setup () {
        

        return {}
    }
})
</script>

<style scoped>
    .top-col{
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: flex-start;
        gap:7px;
    }
    .top-col h1{
        font-size: 18px;
        color:#fff;
        text-transform: uppercase;
    }
    .top-col ul{
        list-style: none;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap:7px;
    }
    .top-col a{
        color:#fff;
        font-size: 14px;
    }
</style>