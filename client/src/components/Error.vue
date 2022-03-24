<template>
    <div class="error-view">
        <img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto/connection_error_bsppck" alt="error image">
        <h1>Oops! Looks like something went wrong</h1>
        <p>{{ errorMessage }}</p>
        <button @click="sendHome">Go Home</button>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';

export default defineComponent({
    props:{
        message:String
    },
    setup (props) {
        const errorMessage = ref(props.message);
        const router = useRouter();
        const store = useStore();

        const sendHome = () => {
            store.dispatch('location/removeLocationAction');
            router.push({name:"Home"});
        }

        return {
            errorMessage,
            sendHome,
        }
    }
})
</script>

<style scoped>
    .error-view{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap:15px;
        width: 100%;
        text-align: center;
    }
    .error-view img{
        width: 500px;
        max-width: 100%;
    }
    .error-view p{
        font-size: 18px;
        color:rgb(143, 138, 138);
        width: 500px;
        max-width: 100%;
    }
    .error-view button{
        padding:10px 20px;
        outline:0;
        border:0;
        background-color: orange;
        color:#fff;
        font-size: 20px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
</style>