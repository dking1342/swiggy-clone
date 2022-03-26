<template>
    <div class="menu-card-btn-wrapper">
        <button v-if="!orderList?.order_item?.filter(x=>x.order_item_name.menu_id === menu.menu_id).length" class="init-btn" @click="userOrderChoice(menu)">Add</button>
        <div v-else-if="orderList?.order_item?.filter(x=>x.order_item_name.menu_id === menu.menu_id).length" class="menu-card-btn-tray">
            <button class="decrease-btn" @click="decreaseFromCart(menu.menu_id)">-</button>
            <span>{{ menu.menu_orderQuantity }}</span>
            <button class="add-btn" @click="addToCart(menu.menu_id)">+</button>
        </div>
    </div>
</template>

<script lang="ts">
import { Menu, Order } from '@/types/fetch-types';
import { computed, defineComponent, ref } from 'vue'
import { useStore } from 'vuex';

export default defineComponent({
    props:['menu','menuList'],
    setup (props) {
        const store = useStore();
        let menuList = ref(props.menuList);
        let menuArray = ref([] as Menu[]);

        // components functions/methods
        const userOrderChoice = (item:Menu) => {
            store.dispatch('cart/initCartAction',{item,menuList});
        }
        const addToCart = (id:string) => {
            menuArray.value = menuList.value.appData!.data;
            store.dispatch('cart/addToCartAction',{id,menuList:menuArray});
        }
        const decreaseFromCart = (id:string) => {
            menuArray.value = menuList.value.appData!.data;
            store.dispatch('cart/removeFromCartAction',{id,menuList:menuArray});
        }

        // computed
        const orderList = computed<Order>(()=> store.state.cart.order);
        

        return {
            userOrderChoice,
            addToCart,
            decreaseFromCart,
            orderList,
        }
    }
})
</script>

<style scoped>
    .menu-card-btn-wrapper{
        border:0.5px solid #ccc;
        width: 75%;
        height: 35px;
        transform:translateY(-25px);
    }
    .init-btn{
        width: 100%;
        height: 100%;
        background-color: #fff;
        outline:none;
        border:none;
        text-transform: uppercase;
        font-weight: 700;
        color:#60b246;
    }
    .menu-card-btn-tray{
        width: 100%;
        height: 100%;
        display: grid;
        grid-template-columns: repeat(3,1fr);
        background-color: #fff;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    .menu-card-btn-tray .add-btn,
    .menu-card-btn-tray .decrease-btn{
        outline:none;
        border:none;
        background:transparent;
        cursor: pointer;
        font-size: 18px;
        font-weight: 500;
    }
    .add-btn{
        color:#60b246;
    }
    .decrease-btn{
        color:#bebfc5;
    }
    .menu-card-btn-tray span{
        font-size: 12px;
        font-weight: 500;
        color:#60b246;
    }
@media (max-width:500px) {
    .menu-card-btn-wrapper{
        width: 100%;
        transform:translateY(-10px);
        height: 50px;
    }
}
</style>