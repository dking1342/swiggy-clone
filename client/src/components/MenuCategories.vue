<template>
    <div v-if="headerId == 'search'">
        <div class="menu-items-header">
            <h1 id="search">Search</h1>
            <p>{{ filterDishes.value.length }} items</p>
        </div>
        <div class="menu-card" v-for="dishes in filterDishes.value" :key="dishes.menu_id">
            <MenuItem 
                :menu="dishes"
                :menuList="menuList"
            />
        </div>        
    </div>
    <div v-else>
        <div class="menu-items-header">
            <h1 :id="headerId" style="scroll-margin-top:250px">{{ headerText }}</h1>
            <p>{{ menuList.value.appData.data.filter(x=> x.menu_category === menuCategory).length }} items</p>
        </div>
        <div class="menu-card" v-for="menu in menuList.value.appData.data.filter(x=>x.menu_category === menuCategory)" :key="menu.menu_id">
            <MenuItem 
                :menu="menu"
                :menuList="menuList"
            />
        </div>

    </div>

</template>

<script lang="ts">
import { Order } from '@/types/fetch-types';
import { computed, defineComponent, ref,  } from 'vue';
import MenuItem from './MenuItem.vue';
import { useStore } from 'vuex';

export default defineComponent({
    components:{
        MenuItem
    },
    props:{
        menuList:Object,
        headerId:String,
        headerText:String,
        menuCategory:String,
        filterDishes:Object
    },
    setup (props) {
        const store = useStore();
        const orderList = computed<Order>(()=> store.state.cart.order);
        let filterDishesRef = ref(props.menuList);

        return {
            orderList,
            filterDishesRef
        }
    }
})
</script>

<style scoped>
    .menu-container{
        display: grid;
        grid-template-columns: 1fr 2fr 1fr;
        gap:20px;
        margin-top: 30px;
        min-height: 500px;
        max-height: 70vh;
        overflow:hidden;
        position:relative;
        z-index: 4;
    }
    .menu-categories-container{
        display: flex;
        align-items: flex-start;
        justify-content: end;
        min-height: 500px;
        max-height: 70vh;
        overflow: scroll;
    }
    .menu-categories-container ul{
        text-align: right;
        list-style: none;
        font-size: 15px;
        color:#282c3f;
        text-overflow: ellipsis;
        overflow: hidden;
        font-weight: 500;
        width: 100%;
        height: 100%;
    }
    .menu-categories-container li{
        padding:2.5px 0px;
        margin-right: 5px;
    }
    .menu-categories-container a{
        border-right: 5px solid transparent;
        padding-right: 15px;
    }
    .menu-categories-container a:hover{
        color:orange;
        border-right: 5px solid orange;
        transition:all .3s ease;
    }


    .menu-items-container{
        min-height: 500px;
        max-height: 70vh;
        overflow: scroll;
    }
    .menu-items-header{
        margin-bottom: 30px;
        border-top:2px solid #171a29;
        margin-top: -25px;
        padding-top:25px;
    }
    .menu-items-header h1{
        font-size: 32px;
    }
    .menu-items-header p{
        font-size: 13px;
        color:#686b78;
        font-weight: 500;
        text-transform: uppercase;
    }
    .menu-card{
        display: grid;
        grid-template-columns: 65% 30%;
        grid-auto-rows: auto;
        margin-bottom: 25px;
        gap: 20px;
        border-bottom: 1px solid #ccc;
        padding:0 0 25px 0;
    }
    .menu-card:last-child{
        border-bottom: none;
    }



    @media (max-width:1150px) {
    .menu-container{
        grid-template-columns: 1fr 3fr 2fr;
    }
}

@media (max-width:850px) {
    .menu-container{
        grid-template-columns: 3fr 2fr;
        grid-template-rows: 40px auto;
    }
    .menu-categories-container{
        grid-column: 1/3;
        height: 100%;
        max-height: 100%;
        min-height: 100%;
    }
    .menu-categories-container ul{
        display: flex;
        align-items: center;
        overflow: scroll;
    }
    .menu-items-container{
        max-height: 50vh;
        grid-column: 1/3;
        grid-row: 2/3;
        z-index: 10;
        background-color: #fff;
    }
    .cart-container{
        max-height: 50vh;
        grid-column: 1/3;
        grid-row: 2/3;
        z-index: -10;
        background-color: #fff;
    }
    .cart-empty-img{
        width: 300px;
    }

    .header-main-container{
        grid-template-columns: 1fr;
        grid-template-rows: auto;
        gap:25px;
        padding:10px 20px;
    }
    .header-main-img-container{
        display: none;
    }
    .header-main-offers-container{
        justify-content: start;
    }
    .header-main-offers-container-wrapper{
        width: 100%;
    }
    .header-search-container .form-field{
        width: 90%;
    }
    .view-btn-toggle{
        display: block;
    }
    }
    @media (max-width:500px) {
        /* .menu-container{
            background-color: red;
            grid-template-columns: repeat(3,1fr );
        } */
        .menu-card{
            grid-template-columns: 1fr;
            grid-template-rows: 70% 25%;
            gap:15px;
            align-items: flex-start;
            /* height: 100%; */
        }
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
        .menu-card-btn-wrapper{
            width: 100%;
            transform:translateY(-10px);
            height: 50px;
        }
        .menu-card-img-wrapper img{
            width: 300px;
            object-fit: contain;
            object-position: center;
        }
        .header-main-content{
            gap:0px;
        }
        .header-main-content h1{
            font-size: 22px;
        }
        .header-main-content h2,
        .header-main-content h3{
            font-size: 12px;
        }

        .header-main-info-rating-container span:first-child,
        .header-main-info-cost-container span:first-child{
            font-size: 12px;
        }
        .header-main-info-rating-container span:nth-child(2),
        .header-main-info-cost-container span:nth-child(2){
            font-size: 10px;
        }
        .header-main-offers-container-wrapper-text{
            top:-15px;
            left:-5px;
            font-size: 12px;
        }
        .header-main-offers-inner-wrap-container{
            padding:8px 15px;
        }
        .header-main-offers-inner-wrap-container span{
            font-size: 12px;
        }
    }
</style>