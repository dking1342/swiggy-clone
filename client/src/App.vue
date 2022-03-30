<template>
  <body>
    <Navbar />
    <main>
      <router-view />
    </main>
  </body>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Navbar from './components/Navbar.vue';

export default defineComponent({
  name: 'App',
  components: {
    Navbar,
  }
});
</script>

<style>
*{
  margin:0;
  padding: 0;
  box-sizing: border-box;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
a{
  text-decoration: none;
}
button{
  cursor: pointer;
}
main{
  height: 100%;
  width: 100%;
  /* overflow-y: scroll; */
  margin-top: 95px;
  padding:0 5%;
  z-index: -1;
}
</style>
