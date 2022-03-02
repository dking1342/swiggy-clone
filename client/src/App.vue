<template>
  <h1>Swiggy</h1>
  <Restaurants />
</template>

<script>
import Restaurants from './components/Restaurants.vue'

export default {
  name: 'App',
  components: {
    Restaurants  
  }
}
</script>

<style>
*{
  margin:0;
  padding:0;
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  font-family: Avenir, Helvetica, Arial, sans-serif;
}
#app {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
</style>
