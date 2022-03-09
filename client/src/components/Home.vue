<template>
    <div>
        home page
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { useRouter } from 'vue-router';

export default defineComponent({
    setup () {
        const router = useRouter();
        let hasLocation = true;

        if(hasLocation){
            router.push({
                name:"Restaurants"
            })
        }

        return {}
    }
})
</script>

<style scoped>

</style>