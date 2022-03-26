<template>
    <div class="menu-card-body">
        <div><span v-if="menu.menu_isBestseller">⭐️ Bestseller</span></div>
        <div><h2>{{ menu.menu_item }}</h2></div>
        <div><h3>${{ menu.menu_price}}</h3></div>
        <div><p>{{ menu.menu_description }}</p></div>
    </div>
    <div class="menu-card-img">
        <div class="menu-card-img-wrapper">
            <img :src="menu.menu_image" :alt="menu.menu_item">
        </div>
        <MenuToggleBtn 
            :menu="menu"
            :menuList="menuList"
        />
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import MenuToggleBtn from './MenuToggleBtn.vue';

export default defineComponent({
    components:{
        MenuToggleBtn,
    },
    props:['menu','menuList'],
    setup () {        

        return {}
    }
})
</script>

<style scoped>
    .menu-card-body{
        display: flex;
        flex-direction: column;
        gap:10px;
        align-items: flex-start;
        justify-content: center;
    }
    .menu-card-body div{
        width: 100%;
    }
    .menu-card-body span{
        font-size: 12px;
        color:#ee9c00;
        font-weight: 500;
    }
    .menu-card-body h2{
        font-size: 18px;
        font-weight: 500;
        color:#3e4152;
        word-break:break-all;
    }
    .menu-card-body h3{
        font-size: 14px;
        font-weight: 400;
        color:#3e4152;
    }
    .menu-card-body p{
        color:rgba(40,44,63,.45);
        font-size: 12px;
    }
    .menu-card-img{
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .menu-card-img-wrapper img{
        width: 100%;
        object-fit: contain;
    }
@media (max-width:500px) {
    .menu-card-body{
        grid-row: 2/3;
        display: grid;
        grid-template-columns: repeat(12,1fr);
        grid-auto-rows: auto;
    }
    .menu-card-body div:nth-child(1){
        grid-column: 1/-1;
        grid-row: 1/2;
    }
    .menu-card-body div:nth-child(2){
        grid-column: 1/9;
        grid-row: 2/3;
    }
    .menu-card-body div:nth-child(3){
        grid-column: 10/-1;
        grid-row: 2/3;
        text-align: right;
    }
    .menu-card-body div:nth-child(4){
        grid-row: 3/4;
        grid-column: 1/-1;
        padding-bottom: 25px;
    }
    .menu-card-img{
        align-items: center;
        justify-content: end;
        grid-row: 1/2;
    }
    .menu-card-img-wrapper img{
        width: 300px;
        object-fit: contain;
        object-position: center;
    }
}
</style>