import { FetchResponse, Menu, Order, OrderItem, ResponseAppState } from "@/types/fetch-types";
import { Ref } from "vue";

const { ref } = require("vue");

// types
interface State {
    order:Order,
    isCartEmpty:boolean
}

// initial state
const state = () => ref({
    order:{
        cart_cost:0,
        cart_quantity:0,
        order_id:"",
        order_item:[]
    },
    isCartEmpty:true
});

// actions
const actions = {
    initCartAction:({commit}:any,{item,menuList}:{item:Menu,menuList:Ref<ResponseAppState<FetchResponse<Menu>>>}) => commit('initCartMutation',{item,menuList}),
    setCartAction:({commit}:any,menuList:Menu[]) => commit('setCartMutation',menuList),
    addToCartAction:({commit}:any,{id,menuList}:{id:string,menuList:Ref<Menu[]>}) => commit('addToCartMutation',{id,menuList}),
    removeFromCartAction:({commit}:any,{id,menuList}:{id:string,menuList:Ref<Menu[]>}) => commit('removeFromCartMutation',{id,menuList}),
    removeCartAction:({commit}:any) => commit('removeCartMutation'),
}

// mutations
const mutations = {
    initCartMutation:(state:State,{item,menuList}:any)=>{
        const order:OrderItem = {
            order_item_id:"",
            order_item_name:item,
            order_item_quantity:1,
            order_reference:"",
            order_restaurant:item.restaurant.restaurant_id
        }

        // check local state to set with new or existing values
        const localState = localStorage.getItem('cart');
        if(!localState){ // no state yet
            state.order = {
                ...state.order,
                order_id:"",
                order_item:[order],
                cart_quantity:order.order_item_quantity,
                cart_cost:order.order_item_quantity * order.order_item_name.menu_price
            };
            localStorage.setItem('cart',JSON.stringify(state.order));
        } else { // state is present
            const currentState:Order = JSON.parse(localState);
            const order_items = [...currentState.order_item,order];

            state.order = {
                ...state.order,
                order_item:order_items,
                cart_quantity:order_items.reduce((acc,val)=> acc + val.order_item_quantity,0),
                cart_cost:order_items.reduce((acc,val)=> acc + (val.order_item_quantity * val.order_item_name.menu_price),0)
            }
            localStorage.setItem('cart',JSON.stringify(state.order));                
        }
        const menuIndex = menuList.value.appData!.data.findIndex((x:Menu)=>x.menu_id === item.menu_id);
        menuList.value.appData!.data[menuIndex].menu_orderQuantity = 1;
    },
    setCartMutation:(state:State, menuList:Menu[]) => {
        if(localStorage.getItem('cart')){
            const localCartState:Order = JSON.parse(localStorage.getItem('cart')!);
            state.order = localCartState;

            if(menuList.length){
                menuList.map(menu=>{
                    localCartState.order_item.forEach(order=>{
                        if(order.order_item_name.menu_id === menu.menu_id){
                            menu.menu_orderQuantity = order.order_item_quantity;
                        }
                    })
                    return menu;
                });
            }
        } else {
            state.order = {
                cart_cost:0,
                cart_quantity:0,
                order_id:"",
                order_item:[]
            }
        }
    },
    addToCartMutation:(state:State,{id,menuList}:{id:string,menuList:Ref<Menu[]>}) => {
        // update order item for increment
        state.order.order_item.map(order=>{
            if(order.order_item_name.menu_id === id){
                order.order_item_quantity += 1;
            }
            return order;
        });

        // update total quantity and cost
        state.order.cart_quantity = state.order.order_item.reduce((acc,val)=> acc + val.order_item_quantity,0);
        state.order.cart_cost = state.order.order_item.reduce((acc,val)=> acc + (val.order_item_quantity * val.order_item_name.menu_price),0);
        
        // update menulist
        if(menuList.value.length){
            const orderIndex = state.order.order_item.findIndex(order=>order.order_item_name.menu_id === id);
            menuList.value = menuList.value.map(menu=>{
                if(menu.menu_id === id){
                    menu.menu_orderQuantity = state.order.order_item[orderIndex].order_item_quantity;
                }
                return menu;
            });
        }
        
        // set localstorage
        localStorage.setItem('cart',JSON.stringify(state.order));
    },
    removeFromCartMutation:(state:State,{id,menuList}:{id:string,menuList:Ref<Menu[]>}) => {
        // find quantity to determine next step
        const stateQuantity = state.order.order_item.find(order=>order.order_item_name.menu_id === id)?.order_item_quantity;
        if(stateQuantity && stateQuantity - 1 === 0){
            // update order item for decrement
            state.order.order_item.map(order=>{
                if(order.order_item_name.menu_id === id){
                    order.order_item_quantity -= 1;
                }
                return order;
            });    
            // removes order item from state
            state.order.order_item = state.order.order_item.filter(order=> order.order_item_name.menu_id !== id);
            
            // update menulist
            if(menuList.value.length){
                menuList.value = menuList.value.map(menu=>{
                    if(menu.menu_id === id){
                        menu.menu_orderQuantity = 0;
                    }
                    return menu;
                });
            }
        } else {
            // update order item for decrement
            state.order.order_item.map(order=>{
                if(order.order_item_name.menu_id === id){
                    order.order_item_quantity -= 1;
                }
                return order;
            });    

            // update menulist
            if(menuList.value.length){
                const orderIndex = state.order.order_item.findIndex(order=>order.order_item_name.menu_id === id);
                menuList.value = menuList.value.map(menu=>{
                    if(menu.menu_id === id){
                        menu.menu_orderQuantity = state.order.order_item[orderIndex].order_item_quantity;
                    }
                    return menu;
                });
            }
        }
        // update total quantity and cost
        state.order.cart_quantity = state.order.order_item.reduce((acc,val)=> acc + val.order_item_quantity,0);
        state.order.cart_cost = state.order.order_item.reduce((acc,val)=> acc + (val.order_item_quantity * val.order_item_name.menu_price),0);
        
        // set localstorage
        if(state.order.order_item.length){
            localStorage.setItem('cart',JSON.stringify(state.order));
        } else {
            localStorage.removeItem('cart');
        }
    },
    removeCartMutation:(state:State)=>{
        state = {
            ...state
        }
        localStorage.removeItem('cart');
    }
}


export default {
    namespaced: true,
    state,
    mutations,
    actions,
}