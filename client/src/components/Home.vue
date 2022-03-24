<template>
    <section>
        <div class="bg-filter">
            <article>
                <img src="https://upload.wikimedia.org/wikipedia/en/thumb/1/12/Swiggy_logo.svg/1200px-Swiggy_logo.svg.png" alt="">
                <h1>Select a location to get started</h1>
            </article>
        </div>
    </section>
</template>

<script lang="ts">
import { computed, defineComponent, onMounted } from 'vue'
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';

export default defineComponent({
    setup () {
        const router = useRouter();
        const store = useStore();
        


        // computed
        const userLocation = computed(()=>store.state.location.state.location);
        

        onMounted(()=>{
            store.dispatch('location/setLocationAction',"");
            if(userLocation.value){
                router.push({
                    name:"Restaurants"
                })
            }
        })

        return {
            userLocation,
        }
    }
})
</script>

<style scoped>
    section{
        width: 100vw;
        height: 100vh;
        background-color: red;
        margin:-5%;
        background:url('https://images.pexels.com/photos/1391487/pexels-photo-1391487.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2');
        background-size: cover;
        position:fixed;
    }
    .bg-filter{
        width: 100vw;
        height: 110vh;
        background-color: midnightblue;
        mix-blend-mode: hard-light;
    }
    article{
        height: 100vh;
        width: 100vw;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap:25px;
        margin-top:-50px;
    }
    article img{
        width: 80%;
    }
    article h1{
        width: 100%;
        text-align: center;
        font-size: 2rem;
        color:#d86b08;
    }

    @media (max-width:769px) {
        article h1{
            font-size: 1.2rem;
        }
    }
</style>