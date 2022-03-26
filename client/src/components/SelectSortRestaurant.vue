<template>
    <select name="links" class="link-dropdown" @change="e=>$emit('sortRestaurantsDropdown',e)">
        <option value="null" selected disabled>Sort Restaurants</option>
        <option value="Discounts">Discounts</option>
        <option value="Rating">Rating</option>
        <option value="Lowest cost">Lowest Cost</option>
        <option value="Highest cost">Highest Cost</option>
    </select>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    emits:['sortRestaurantsDropdown'],
    setup () {

        
        


        return {}
    }
})
</script>

<style scoped>

</style>