<template>
    <section v-if="restaurantList.dataState == 'LOADING'">
        <Loading />
    </section>
    <section v-else-if="restaurantList.dataState == 'SUCCESS'" @scroll="handleScroll" class="restaurant-body">
        <header  >
            <div class="header-breadcrumb-container">
                <router-link to="/"><span class="link-text">Home</span></router-link>
                <span>/</span>
                <span><strong>{{restaurantList.appData.data[0].restaurant_name}}</strong></span>
            </div>
            <div class="header-main-container">
                <div class="header-main-img-container">
                    <div class="header-main-img-container-wrap">
                        <img :src="restaurantList.appData.data[0].restaurant_main_img" alt="">
                    </div>
                </div>
                <div class="header-main-content">
                    <h1>{{restaurantList.appData.data[0].restaurant_name}}</h1>
                    <h2>{{restaurantList.appData.data[0].restaurant_cuisines.slice(0,2).join(", ")}}</h2>
                    <h3>{{restaurantList.appData.data[0].restaurant_city}}</h3>
                    <div class="header-main-info-container">
                        <div class="header-main-info-rating-container">
                            <span>⭐️ {{restaurantList.appData.data[0].restaurant_rating}}</span>
                            <span>Rating</span>
                        </div>
                        <div class="header-main-info-cost-container">
                            <span>₹ {{restaurantList.appData.data[0].restaurant_cost}}</span>
                            <span>Cost for two</span>
                        </div>
                    </div>
                </div>
                <div class="header-main-offers-container" v-if="restaurantList.appData.data[0].discount_isValid">
                    <div class="header-main-offers-container-wrapper">
                        <span class="header-main-offers-container-wrapper-text">Offer</span>
                        <div class="header-main-offers-inner-wrap-container">
                            <span>✅ {{restaurantList.appData.data[0].discounts.discount_text}}</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="header-search-container">
                <div class="form-field">
                    <span>🔎</span>
                    <input 
                        autocomplete="off" 
                        id="search" 
                        type="text" 
                        name="search" 
                        placeholder="Search for dishes" 
                        maxlength="35"
                        v-model="userFilter" 
                        @keyup="userFilterInput"
                    >
                    <button @click="clearSearch()">X</button>
                </div>
            </div>
        </header>
        <section v-if="menuList.dataState == 'LOADING'">
            <Loading />
        </section>
        <section v-else-if="menuList.dataState == 'SUCCESS'">
            <section class="menu-container">
                <aside class="menu-categories-container">
                    <ul>
                        <li v-if="userFilter"><a href="#search" @click="categoryScroll">Search</a></li>
                        <li v-if="menuList.appData.data.filter(x=>x.menu_category === 'BR').length"><a href="#breakfast" @click="categoryScroll">Breakfast</a></li>
                        <li v-if="menuList.appData.data.filter(x=>x.menu_category === 'M').length"><a href="#main" @click="categoryScroll">Main</a></li>
                        <li v-if="menuList.appData.data.filter(x=>x.menu_category === 'S').length"><a href="#sides" @click="categoryScroll">Side</a></li>
                        <li v-if="menuList.appData.data.filter(x=>x.menu_category === 'D').length"><a href="#desserts" @click="categoryScroll">Desserts</a></li>
                        <li v-if="menuList.appData.data.filter(x=>x.menu_category === 'B').length"><a href="#beverages" @click="categoryScroll">Beverages</a></li>
                    </ul>
                </aside>
                <article class="menu-items-container">
                    <div v-if="userFilter">
                        <MenuCategories 
                            v-bind="searchProps"
                        />
                    </div>
                    <div v-if="menuList.appData.data.filter(x=>x.menu_category === 'BR').length">
                        <MenuCategories 
                            v-bind="breakfastProps"
                        />                        
                    </div>
                    <div v-if="menuList.appData.data.filter(x=>x.menu_category === 'M').length">
                        <MenuCategories 
                            v-bind="mainProps"
                        />
                    </div>
                    <div v-if="menuList.appData.data.filter(x=>x.menu_category ==='S').length">
                        <MenuCategories 
                            v-bind="sideProps"
                        />
                    </div>
                    <div v-if="menuList.appData.data.filter(x=>x.menu_category ==='D').length">
                        <MenuCategories 
                            v-bind="dessertsProps"
                        />
                    </div>
                    <div v-if="menuList.appData.data.filter(x=>x.menu_category ==='B').length">
                        <MenuCategories 
                            v-bind="beveragesProps"
                        />
                    </div>
                </article>
                <aside class="cart-container">
                    <div class="cart-empty-container" v-if="!orderList.order_item.length">
                        <h1>Cart Empty</h1>
                        <div class="cart-empty-img">
                            <img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_480/Cart_empty_-_menu_2x_ejjkf2" alt="empty cart">
                        </div>
                        <p>Good food is always cooking! Go ahead, order some yummy items from the menu.</p>
                    </div>
                    <div class="cart-full-container" v-else-if="orderList.order_item.length">
                        <h1>Cart</h1>
                        <div class="cart-receipt-list">
                            <div class="cart-receipt-list-item" v-for="order in orderList.order_item" :key="order.order_menu_id">
                                <span class="cart-item-name">{{ order.order_item_name.menu_item }}</span>
                                <div class="cart-receipt-toggle-btns">
                                    <button class="cart-btn-decrease" @click="decreaseFromCart(order.order_item_name.menu_id)">-</button>
                                    <span>{{ order.order_item_quantity }}</span>
                                    <button class="cart-btn-add" @click="addToCart(order.order_item_name.menu_id)">+</button>
                                </div>
                                <span class="cart-item-cost">${{ order.order_item_quantity * order.order_item_name.menu_price }}</span>
                            </div>
                        </div>
                        <div class="cart-receipt-total">
                            <div class="cart-subtotal">
                                <div class="cart-subtotal-text">
                                    <span>Subtotal</span>
                                    <span>Extra charges may apply</span>
                                </div>
                                <div class="cart-subtotal-cost">${{ orderList.cart_cost }}</div>
                            </div>
                            <button class="cart-checkout-btn" @click="checkout">Checkout</button>
                        </div>
                    </div>
                </aside>
                <div class="view-btn-toggle">
                    <button v-if="!isToggled" @click="toggleView" class="menu-to-checkout">🧺</button>
                    <button v-if="isToggled" @click="toggleView" class="checkout-to-menu">X</button>
                </div>
            </section>
            <section class="menu-info-container">
                <div class="menu-info-top-row-container">
                    <div class="menu-address-container">
                        <h1>Address</h1>
                        <address>
                            <p>{{restaurantList.appData.data[0].restaurant_address_1}}</p>
                            <p>{{restaurantList.appData.data[0].restaurant_address_2}}</p>
                            <p>{{restaurantList.appData.data[0].restaurant_city}}</p>
                            <p>{{restaurantList.appData.data[0].restaurant_state}}</p>
                            <p>{{restaurantList.appData.data[0].restaurant_zip_code}}</p>
                        </address>
                    </div>
                    <div class="menu-cuisines-container">
                        <h1>Cuisines</h1>
                        <div class="cuisine-list">
                            {{restaurantList.appData.data[0].restaurant_cuisines.slice(0,2).join(", ")}}
                        </div>
                    </div>
                </div>
                <div class="menu-info-bottom-row-container">
                    <div class="footer-img-container">
                        <img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_162,h_80/fssai_final_edss9i" alt="cert img">
                    </div>
                    <p>Applied for license</p>
                </div>
            </section>
        </section>
        <section v-else-if="menuList.dataState == 'ERROR'">
            <Error message="Page not found" />
        </section>
    </section>
    <section v-else-if="restaurantList.dataState == 'ERROR'">
        <Error message="Page not found"/>
    </section>
</template>

<script lang="ts">
import { Discount, FetchResponse, Menu, Order, ResponseAppState, Restaurant } from '@/types/fetch-types';
import { computed, defineComponent, onMounted, onUnmounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router';
import MenuCategories from '../components/MenuCategories.vue'
import Error from '../components/Error.vue';
import Loading from '../components/Loading.vue';
import { useFetch } from '../utils/useFetch';
import { useStore } from 'vuex';

export default defineComponent({
    components:{
        MenuCategories,
        Error,
        Loading,
    },
    setup () {
        let isToggled = ref(false);
        let restaurantList = ref({} as ResponseAppState<FetchResponse<Restaurant<Discount>>>);
        let menuList = ref({} as ResponseAppState<FetchResponse<Menu>>);
        let menuArray = ref([] as Menu[]);
        let route = useRoute();
        let router = useRouter();
        let restaurant_id = ref(route.params.id);
        let userFilter = ref("");
        let store = useStore();

        // component functions/methods
        const toggleView = () => {
            let menuContainer = document.querySelector('.menu-items-container') as HTMLElement;
            let checkoutContainer = document.querySelector('.cart-container') as HTMLElement;

            if(!isToggled.value){
                isToggled.value = !isToggled.value;
                menuContainer.style.zIndex = "-10";
                checkoutContainer.style.zIndex = "4";
            } else {
                isToggled.value = !isToggled.value;
                menuContainer.style.zIndex = "4";
                checkoutContainer.style.zIndex = "-10";
            }
        }
        const userFilterInput = () => {
            let menu = document.querySelector('.menu-items-container') as HTMLDivElement;
            menu.scrollTo({
                behavior:'smooth',
                top:0
            })
        }
        const clearSearch = () => {
            let search = document.querySelector("#search") as HTMLInputElement;
            search.value = "";
            userFilter.value = "";
        }
        const decreaseFromCart = (id:string) => {
            menuArray.value = menuList.value.appData!.data;
            store.dispatch('cart/removeFromCartAction',{id,menuList:menuArray});
        }
        const addToCart = (id:string) => {
            menuArray.value = menuList.value.appData!.data;
            store.dispatch('cart/addToCartAction',{id,menuList:menuArray});
        }
        const categoryScroll = (e:any) => {
            e.preventDefault();
            let breakfast = document.querySelector('#breakfast') as HTMLDivElement;
            let main = document.querySelector('#main') as HTMLDivElement;
            let sides = document.querySelector('#sides') as HTMLDivElement;
            let desserts = document.querySelector('#desserts') as HTMLDivElement;
            let beverages = document.querySelector('#beverages') as HTMLDivElement;
            let menu = document.querySelector('.menu-items-container') as HTMLDivElement;

            switch (e.target.textContent) {
                case 'Search':
                    menu.scrollTo({
                        behavior:'smooth',
                        top:0
                    })
                    break;
                case 'Breakfast':
                    menu.scrollTo({
                        behavior:'smooth',
                        top:breakfast.offsetTop
                    })
                    break;
                case 'Main':
                    menu.scrollTo({
                        behavior:'smooth',
                        top:main.offsetTop
                    })                 
                    break;
                case 'Side':
                    menu.scrollTo({
                        top:sides.offsetTop,
                        behavior:'smooth'
                    })                    
                    break;
                case 'Desserts':
                    menu.scrollTo({
                        top:desserts.offsetTop,
                        behavior:'smooth'
                    })                                        
                    break;
                case 'Beverages':
                    menu.scrollTo({
                        top:beverages.offsetTop,
                        behavior:'smooth'
                    })                                        
                    break;
                default:
                    return;
            }
        }
        const checkout = () => {
            // check cart to see if all items are from the same restaurant
            const validator = orderList.value.order_item[0].order_item_name.restaurant;
            const validationTest = orderList.value.order_item.every(val=> val.order_item_name.restaurant === validator);
            if(validationTest){
                router.push({path:"/checkout"});
                window.scrollTo({top:0,behavior:'smooth'});
            } else {
                alert("Please make sure all cart items are from the same restaurant");
            }
        }
        const handleScroll = () => {
            console.log("width",window.innerWidth)
            let headerElement = document.querySelector('header') as HTMLElement;
            let bodyElement = document.querySelector('.restaurant-body') as HTMLDivElement;
            if(window.scrollY > 80 && window.innerWidth > 890){
                headerElement.classList.add('navbar-sticky');
                bodyElement.classList.add('restaurant-body-sticky');
            } else {
                headerElement.classList.remove('navbar-sticky');
                bodyElement.classList.remove('restaurant-body-sticky');
            }
            
        }

        // computed functions
        const filterDishes = computed(()=> 
            menuList.value.appData!.data.filter(x=>
                x.menu_item.toLowerCase().includes(userFilter.value.toLowerCase())
            ))
        const orderList = computed<Order>(()=> store.state.cart.order);
        const userLocation = computed(() => store.state.location.state.location);

        
        // fetches
        const getRestaurant = async() => {
            let { dataState, data, errorMsg } = await useFetch<FetchResponse<Restaurant<Discount>>>(`http://localhost:8000/api/v1/restaurants/${restaurant_id.value}/`);
            restaurantList.value.dataState = dataState.value;
            restaurantList.value.appData = data.value as FetchResponse<Restaurant<Discount>>;
            restaurantList.value.error = errorMsg.value;
        }
        const getMenu = async() => {
            let { dataState, data, errorMsg } = await useFetch<FetchResponse<Menu>>(`http://localhost:8000/api/v1/menu/restaurant/${restaurant_id.value}`);
            menuList.value.dataState = dataState.value;
            menuList.value.appData = data.value as FetchResponse<Menu>;
            menuList.value.error = errorMsg.value;
            store.dispatch('cart/setCartAction',menuList.value.appData.data);
        }


        // lifecycle hooks
        onMounted(()=>{
            getRestaurant();
            getMenu();
            store.dispatch('location/setLocationAction',"");
            if(!userLocation.value){
                router.push({name:"Home"});
            }
            window.addEventListener('scroll',()=>handleScroll());
        });

        onUnmounted(()=>{
            window.removeEventListener('scroll',()=>handleScroll());
        })

        

         // props
        const breakfastProps = {
            headerId:"breakfast",
            headerText:"Breakfast",
            menuCategory:"BR",
            menuList,
            orderList
        };
        const mainProps = {
            headerId:"main",
            headerText:"Main",
            menuCategory:"M",
            menuList,
            orderList
        };
        const sideProps = {
            headerId:"sides",
            headerText:"Side",
            menuCategory:"S",
            menuList,
            orderList
        };
        const dessertsProps = {
            headerId:"desserts",
            headerText:"Desserts",
            menuCategory:"D",
            menuList,
            orderList
        };
        const beveragesProps = {
            headerId:"beverages",
            headerText:"Beverages",
            menuCategory:"B",
            menuList,
            orderList
        };
        const searchProps = {
            headerId:"search",
            headerText:"Search",
            filterDishes:filterDishes,
            orderList
        };

        return {
            isToggled,
            restaurantList,
            menuList,
            userFilter,
            toggleView,
            userFilterInput,
            filterDishes,
            orderList,
            clearSearch,
            categoryScroll,
            breakfastProps,
            mainProps,
            sideProps,
            dessertsProps,
            beveragesProps,
            searchProps,
            checkout,
            addToCart,
            decreaseFromCart,
            handleScroll,
        }
    }
})
</script>

<style scoped>
header{
    height: fit-content;
    background-color: #fff;
    box-shadow: 0 2px 15px rgba(0, 0, 0, 0.15);
    margin:0 -5%;
    transition:500ms ease all;
    /* position:fixed;
    top:0;
    z-index: 50; */
}
.header-breadcrumb-container{
    height: 30px;
    font-size: 10px;
    color:#93959f;
    padding:0 5%;
    display: flex;
    align-items: center;
    background-color: #ebebeb;
    gap:5px;
}
.header-main-container{
    display: grid;
    grid-template-columns: 2fr 3fr 2fr ;
    grid-template-rows: 250px;
    background-color: #171a29;
}
.header-main-img-container{
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}
.header-main-img-container-wrap{
    height: 75%;
    width: 75%;
}
.header-main-img-container-wrap img{
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
}
.header-main-content{
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap:10px;
}
.header-main-content h1{
    color:#fff;
    font-weight: 300;
    font-size: 32px;
}
.header-main-content h2,
.header-main-content h3{
    color:#d8d8d8;
    text-overflow: ellipsis;
    overflow: hidden;
    font-size: 15px;
    font-weight: 300;
}
.header-main-info-container{
    display: flex;
    align-items: center;
    justify-content: start;
    margin-top: 10px;
    gap: 30px;
}
.header-main-info-rating-container,
.header-main-info-cost-container{
    display: flex;
    flex-direction: column;
    gap:5px;
}
.header-main-info-rating-container span:first-child,
.header-main-info-cost-container span:first-child{
    color:#fff;
    font-size: 14px;
    font-weight: 600;
}
.header-main-info-rating-container span:nth-child(2),
.header-main-info-cost-container span:nth-child(2){
    color:#d8d8d8;
    font-size: 12px;
    font-weight: 400;
}
.header-main-offers-container{
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}
.header-main-offers-container-wrapper{
    width: 85%;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border:2px solid #fff;
    border-radius: 5px;
}
.header-main-offers-container-wrapper-text{
    position:absolute;
    top:-20px;
    left:-10px;
    background-color: #171a29;
    padding:5px;
    display: flex;
    color:#fff;
    font-weight: 500;
    font-size: 20px;
}
.header-main-offers-inner-wrap-container{
    width: 100%;
    padding:25px 15px;
}
.header-main-offers-inner-wrap-container span{
    color:#fff;
    font-size: 14px;
    font-weight: 500;
}
.header-search-container{
    width: 100%;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin:10px 0;
}
.header-search-container .form-field{
    width: 50%;
    height: 100%;
    display: grid;
    grid-template-columns: auto 5fr 1fr;
    align-items: center;
    justify-content: space-between;
    gap:20px;
}
.form-field span{
    font-size: 20px;
}
.form-field input{
    outline:none;
    border:none;
    font-size: 24px;
}
.form-field button{
    background:transparent;
    outline: none;
    border: none;
    font-size: 26px;
    cursor: pointer;
}

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

.cart-container{
    max-height: 70vh;
    min-height: 500px;
    overflow: scroll;
}
.cart-empty-container{
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: space-between;
    gap:50px;
    overflow: scroll;
}
.cart-empty-container h1{
    font-size: 32px;
    color:#7e808c;
}
.cart-empty-img{
    width: 100%;
}
.cart-empty-img img{
    width: 100%;
}
.cart-empty-container p{
    color:#93959f;
    font-size: 16px;
    font-weight: 300;
}
.cart-full-container{
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 20px;
    padding-bottom:15px;
}
.cart-full-container h1{
    font-size: 32px;
    font-weight: 600;
}
.cart-full-container .cart-error-message p{
    font-size: 13px;
    font-weight: 500;
    color:#fa4a5b;
}
.cart-receipt-list{
    max-height: 280px;
    overflow: scroll;
    display: flex;
    flex-direction: column;
    gap: 10px;
    width: 100%;
}
.cart-receipt-list-item{
    display: grid;
    grid-template-columns: 2fr 1fr 1fr;
    align-items: center;
    justify-content: center;
    gap: 7px;
}
.cart-item-name{
    font-size: 14px;
    font-weight: 400;
}
.cart-receipt-toggle-btns{
    display: grid;
    grid-template-columns: repeat(3,1fr);
    align-items: center;
    justify-content: center;
    text-align: center;
    background-color: #fff;
    border:0.5px solid #ccc;
}
.cart-btn-decrease,
.cart-btn-add{
    background-color: transparent;
    outline:none;
    border: none;
    font-size: 18px;
    cursor: pointer;
}
.cart-receipt-toggle-btns span{
    font-size: 12px;
    font-weight: 500;
    color:#60b246;
}
.cart-btn-add{
    color:#60b246;
}
.cart-item-cost{
    font-size: 13px;
    color:#535665;
    text-align: right;
}
.cart-receipt-total{
    display: flex;
    flex-direction: column;
    gap:15px;
    width: 100%;
}
.cart-subtotal{
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.cart-subtotal-text{
    display: flex;
    flex-direction: column;
}
.cart-subtotal-text span:first-child{
    font-size: 15px;
    font-weight: 600;
    color:#3d4152;
}
.cart-subtotal-text span:last-child{
    font-size: 13px;
    font-weight: 300;
    color:#7e808c;
}
.cart-subtotal-cost{
    font-size: 15px;
    font-weight: 600;
    color:#3d4152;
}
.cart-checkout-btn{
    height: 50px;
    background-color: #60b246;
    outline:none;
    cursor: pointer;
    border:none;
    color:#fff;
    font-size: 16px;
    font-weight: 600;
    text-transform: uppercase;
}
.menu-info-container{
    display: flex;
    flex-direction: column;
    background-color: #e9e9eb;
    padding:70px 0;
    min-width: 100%;
    margin:0 -5%;
    gap: 25px;
}
.menu-info-top-row-container{
    display: grid;
    grid-template-columns: repeat(auto-fit,minmax(300px,1fr));
    grid-auto-rows: auto;
    align-items: center;
    justify-content: space-around;
    gap: 35px;
}
.menu-address-container,
.menu-cuisines-container{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: start;
    height: 100%;
    width: 100%;
}
.menu-address-container h1,
.menu-cuisines-container h1{
    font-size: 15px;
    text-transform: uppercase;
    font-weight: 600;
    border-bottom: 3px solid #000;
    padding:7px 0;
    margin-bottom: 14px;
}
.menu-address-container address{
    color:#686b78;
    font-size: 15px;
    display: flex;
    align-items: center;
    flex-direction: column;
    gap:3px;
    text-align: center;
}
.cuisine-list{
    font-size: 15px;
    width: 100%;
    text-align: center;
    height: fit-content;
    flex-wrap: wrap;
}
.menu-info-bottom-row-container{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 20px;
}
.footer-img-container{
    width: 80px;
    height: 40px;
}
.footer-img-container img{
    width: 100%;
}
.menu-info-bottom-row-container p{  
    font-size: 18px;
    font-weight: 500;
    color:#686b78
}


.view-btn-toggle{
    display: none;
    position:absolute;
    right:0px;
    bottom:15px;
    z-index: 15;
}
.view-btn-toggle button{
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background-color:#ee9c00;
    font-size: 20px;
    cursor: pointer;
    outline:none;
    border:none;
    color:#fff;
    font-weight: 500;
}

/* utility styles */
.navbar-sticky{
    position: fixed;
    top: 0;
    left:0;
    right:0;
    z-index: 5;
    transition:500ms ease all;
    padding:0 40px;
}
.restaurant-body-sticky{
    margin-top: 350px;
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
    .menu-card{
        grid-template-columns: 1fr;
        grid-template-rows: 70% 25%;
        gap:15px;
        align-items: flex-start;
        /* height: 100%; */
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