<template>
    <section>
        <header>
            <div class="search-header-row-1">
                <div class="search-border">
                    <span>🔎</span>
                    <input type="text" v-model="searchInput" @input="handleSearchChange">
                    <button class="clear-search-btn" v-if="searchInput" @click="clearSearch">Clear</button>
                </div>
                <div class="search-exit-container">
                    <button class="exit-search-btn" @click="navigateToRestaurant">
                        <span>X</span>
                        <span>ESC</span>
                    </button>
                </div>  
            </div>
            <div class="search-results">
                <button class="search-result-container">
                    <img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_80,h_80,c_fill/Icons-Autosuggest/AS_Cuisine_3x" alt="list item image">
                    <h1>Asian</h1>
                    <p>Cuisine</p>
                </button>
                <button class="search-result-container">
                    <img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_80,h_80,c_fill/xpz1gheguayjozjsxthi" alt="list item image">
                    <h1>Cupcakes</h1>
                    <p>Dish</p>
                </button>
                <button class="search-result-container">
                    <img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_80,h_80,c_fill/mxdqyx3m09vesmpqctch" alt="list item image">
                    <h1>McDonald's</h1>
                    <p>Restaurant</p>
                </button>
                <button class="search-result-container">
                    <img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_80,h_80,c_fill/mxdqyx3m09vesmpqctch" alt="list item image">
                    <h1>McDonald's</h1>
                    <p>Restaurant</p>
                </button>
                <button class="search-result-container">
                    <img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_80,h_80,c_fill/mxdqyx3m09vesmpqctch" alt="list item image">
                    <h1>McDonald's</h1>
                    <p>Restaurant</p>
                </button>
                <button class="search-result-container">
                    <img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_80,h_80,c_fill/mxdqyx3m09vesmpqctch" alt="list item image">
                    <h1>McDonald's</h1>
                    <p>Restaurant</p>
                </button>
                <button class="search-result-container">
                    <img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_80,h_80,c_fill/mxdqyx3m09vesmpqctch" alt="list item image">
                    <h1>McDonald's</h1>
                    <p>Restaurant</p>
                </button>
                <button class="search-result-container">
                    <img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_80,h_80,c_fill/mxdqyx3m09vesmpqctch" alt="list item image">
                    <h1>McDonald's</h1>
                    <p>Restaurant</p>
                </button>
            </div>
        </header>
        <div class="search-list-container">
            <div class="search-list-header">
                <button class="search-toggle-btn restaurant-toggle-btn active" @click="toggleRestaurant">Restaurants</button>
                <button class="search-toggle-btn dishes-toggle-btn" @click="toggleDishes">Dishes</button>
                <select @change="handleSelectChange" v-model="sortInput">
                    <option value="null" disabled selected>Sort</option>
                    <option value="AZ">A-Z</option>
                    <option value="ZA">Z-A</option>
                    <option value="Price">Price</option>
                </select>
            </div>
            <div class="search-list-body restaurant-list" v-if="isShowingRestaurants && filteredRestaurantList.length">
                <div v-for="restaurant in filteredRestaurantList" :key="restaurant.restaurant_id" class="card">
                    <RestaurantItem 
                        :restaurant="restaurant"
                    />
                </div>
            </div>
            <div class="search-list-body restaurant-list" v-else-if="isShowingRestaurants && !filteredRestaurantList.length && searchInput">
                <Error 
                    message="No items matching search input. Please try again"
                    :showBtn=Boolean(false)
                />
            </div>

            <div class="search-list-body dishes-list" v-if="isShowingDishes && filteredMenuList.length">
                <div  v-for="menu in filteredMenuList" :key="menu.menu_id">
                    <router-link :to="`/restaurants/${menu.restaurant}`" class="menu-card">
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
                        </div>
                    </router-link>
                </div>
            </div>
            <div class="search-list-body dishes-list" v-if="isShowingDishes && !filteredMenuList.length && searchInput">
                <Error 
                    message="No items matching search input. Please try again"
                    :showBtn=Boolean(false)
                />
            </div>

        </div>
    </section>
</template>

<script lang="ts">
import { ResponseAppState, FetchResponse, Restaurant, Discount, Menu, Cuisine } from '@/types/fetch-types';
import { useFetch } from '@/utils/useFetch';
import { computed, defineComponent, onMounted, ref } from 'vue'
import RestaurantItem from '../components/RestaurantItem.vue';
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';
import Error from '../components/Error.vue';

export default defineComponent({
    components:{
        RestaurantItem,
        Error,
    },
    setup () {
        const router = useRouter();
        let restaurantList = ref({} as ResponseAppState<FetchResponse<Restaurant<Discount>>>);
        let menuList = ref({} as ResponseAppState<FetchResponse<Menu>>);
        let cuisineList = ref({} as ResponseAppState<FetchResponse<Cuisine>>);
        let searchInput = ref("");
        let sortInput = ref<string | null>(null);
        let filteredRestaurantList = ref([] as Restaurant<Discount>[]);
        let filteredMenuList = ref([] as Menu[]);
        let isShowingRestaurants = ref(true);
        let isShowingDishes = ref(false);
        let store = useStore();

        

        // component functions/methods
        const navigateToRestaurant = () => {
            router.push({name:"Restaurants"});
        }
        const clearSearch = () => {
            searchInput.value = "";
            filteredRestaurantList.value = [];
            filteredMenuList.value = [];
            sortInput.value = null;
        }
        const handleSearchChange = () => {
            if(searchInput.value){
                filteredRestaurantList.value = [];
                filteredMenuList.value = [];
                filteredRestaurantList.value = restaurantList.value.appData!.data
                    .filter(item=>item.restaurant_name.toLowerCase().includes(searchInput.value.toLowerCase()))
                    .filter(restaurant=>restaurant.restaurant_city.includes(userLocation.value));
                filteredMenuList.value = menuList.value.appData!.data
                    .filter(item=>item.menu_item.toLowerCase().includes(searchInput.value.toLowerCase()))
                    .filter(menu=> filteredRestaurantList.value.map(rest=>rest.restaurant_id === String(menu.restaurant)));
            } else {
                filteredRestaurantList.value = [];
                filteredMenuList.value = [];
            }
        }
        const handleSelectChange = () => {
            if(isShowingRestaurants.value){
                switch (sortInput.value) {
                    case null:
                        break;
                    case "AZ":
                        filteredRestaurantList.value.sort((a,b)=>a.restaurant_name.localeCompare(b.restaurant_name));
                        break;
                    case "ZA":
                        filteredRestaurantList.value.sort((a,b)=>b.restaurant_name.localeCompare(a.restaurant_name));
                        break;
                    case "Price":
                        filteredRestaurantList.value.sort((a,b)=>a.restaurant_cost - b.restaurant_cost);
                        break;
                    default:
                        break;
                }
            }
            if(isShowingDishes.value){
                switch (sortInput.value) {
                    case null:
                        break;
                    case "AZ":
                        filteredMenuList.value.sort((a,b)=>a.menu_item.localeCompare(b.menu_item));
                        break;
                    case "ZA":
                        filteredMenuList.value.sort((a,b)=>b.menu_item.localeCompare(a.menu_item));
                        break;
                    case "Price":
                        filteredMenuList.value.sort((a,b)=>a.menu_price - b.menu_price);
                        break;
                    default:
                        break;
                }
            }
        }
        const toggleRestaurant = () => {
            isShowingRestaurants.value = true;
            isShowingDishes.value = false;
            sortInput.value = null;

            let restaurantToggleBtn = document.querySelector('.restaurant-toggle-btn') as HTMLButtonElement;
            let dishesToggleBtn = document.querySelector('.dishes-toggle-btn') as HTMLButtonElement;

            restaurantToggleBtn.classList.add('active');
            if(dishesToggleBtn.classList.contains('active')){
                dishesToggleBtn.classList.remove('active');
            }
            handleSearchChange();
        }
        const toggleDishes = () => {
            isShowingRestaurants.value = false;
            isShowingDishes.value = true;
            sortInput.value = null;

            let restaurantToggleBtn = document.querySelector('.restaurant-toggle-btn') as HTMLButtonElement;
            let dishesToggleBtn = document.querySelector('.dishes-toggle-btn') as HTMLButtonElement;

            dishesToggleBtn.classList.add('active');
            if(restaurantToggleBtn.classList.contains('active')){
                restaurantToggleBtn.classList.remove('active');
            }
            handleSearchChange();
        }

        // computed
        const userLocation = computed(() => store.state.location.state.location);

        


        // fetch
        const getRestaurants = async() => {
            let { dataState, data, errorMsg } = await useFetch<FetchResponse<Restaurant<Discount>>>("http://localhost:8000/api/v1/restaurants");
            restaurantList.value.appData = data.value as FetchResponse<Restaurant<Discount>>;
            restaurantList.value.dataState = dataState.value;
            restaurantList.value.error = errorMsg.value;
        };
        const getMenus = async() => {
            let { dataState, data, errorMsg } = await useFetch<FetchResponse<Menu>>("http://localhost:8000/api/v1/menu")
            menuList.value.dataState = dataState.value;
            menuList.value.appData = data.value as FetchResponse<Menu>;
            menuList.value.error = errorMsg.value;
        };
        const getCuisines = async() => {
            let { dataState, data, errorMsg } = await useFetch<FetchResponse<Cuisine>>("http://localhost:8000/api/v1/cuisines");
            cuisineList.value.dataState = dataState.value;
            cuisineList.value.appData = data.value as FetchResponse<Cuisine>;
            cuisineList.value.error = errorMsg.value;
        }
        
        onMounted(()=>{
            getRestaurants();
            getMenus();
            getCuisines();
        })


        return {
            restaurantList,
            filteredRestaurantList,
            filteredMenuList,
            menuList,
            searchInput,
            isShowingRestaurants,
            isShowingDishes,
            sortInput,
            navigateToRestaurant,
            clearSearch,
            handleSearchChange,
            handleSelectChange,
            toggleRestaurant,
            toggleDishes,

        }
    }
})
</script>

<style scoped>
    section{
        display: grid;
        grid-template-columns: 1fr;
        gap:30px;
        margin: 80px 0;
    }
    header{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: fit-content;
        gap:20px;
    }

    /* search bar */
    .search-header-row-1{
        width: 85%;
        height: 60px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap:15px;
    }
    .search-border{
        height: 100%;
        width: 100%;
        border:1px solid #555;
        padding:10px;
        display: flex;
        align-items: center;
        /* justify-content: space-between; */
        border-radius: 2px;
        gap:10px;
    }
    .search-border input{
        width: 90%;
        height: 100%;
        outline:0;
        border:0;
        font-size: 18px;
    }
    .clear-search-btn{
        outline: 0;
        border: 0;
        background-color: transparent;
        font-size: 16px;
        font-weight: 800;
        text-transform: uppercase;
        color:orange;
    }
    .search-exit-container{
        height: 100%;
    }
    .exit-search-btn{
        width: 100%;
        height: 100%;
        border:0;
        outline:0;
        background-color: transparent;
        display: flex;
        flex-direction: column;
        gap:2px;
        align-items: center;
        justify-content: center;
    }
    .exit-search-btn span:first-child{
        font-size: 28px;
    }
    .exit-search-btn span:last-child{
        font-size: 12px;
        color: #777;
    }

    /* init search result */
    .search-results{
        width: 85%;
        /* background-color: #f9f9f9; */
        border-radius: 2px;
        display: flex;
        flex-direction: column;
        border:0;
        max-height: 0px;
        overflow: hidden;

        /* border:1px solid #d9d9d9; */
        /* max-height: 350px; */
        /* overflow: scroll; */
    }
    .search-result-container{
        display: grid;
        grid-template-columns: repeat(12,1fr);
        grid-template-rows: repeat(6,1fr);
        padding:10px;
        gap:10px;
        align-items: center;
        border:0;
        outline:0;
        background-color: transparent;
        text-align: left;
        /* border-bottom:1px solid #d9d9d9; */
    }
    .search-result-container:hover{
        background-color: #f9f9f9;
        transition: 250ms background-color ease;
    }
    .search-result-container img{
        grid-column: 1/3;
        grid-row: 1/-1;
        width: 50px;
        height: 50px;
        justify-self:center;
    }
    .search-result-container h1{
        grid-column: 3/-1;
        font-size: 14px;
        font-weight: 400;
        grid-row: 1/5;
    }
    .search-result-container p{
        grid-column: 3/-1;
        font-size: 14px;
        color:#666;
        grid-row: 4/-1;
    }

    /* search result output */
    /* search result output header */
    .search-list-container{
        display: flex;
        width: 85%;
        margin:0 auto;
        flex-direction: column;
        gap:15px;
    }
    .search-list-header{
        display: grid;
        grid-template-columns: minmax(70px,100px) minmax(70px,100px) auto minmax(70px,100px);
        grid-template-rows: 1fr;
        height: 45px;
        gap:10px;
        background:#f9f9f9;
    }
    .search-list-header button,
    .search-list-header select{
        background:transparent;
        outline:0;
        border:0;
        font-size: 16px;
        font-weight: 600;
    }
    .search-list-header button:first-child{
        grid-column: 1/2;
        grid-row: 1/-1;
    }
    .search-list-header button:last-child{
        grid-column: 2/3;
        grid-row: 1/-1;
    }
    .search-list-header select{
        grid-column: 4/5;
        grid-row: 1/-1;
        color:orange;
    }

    /* restaurant list */
    .search-list-body{
        display: grid;
        grid-template-columns: repeat(auto-fit,minmax(300px,1fr));
        grid-template-rows:auto; 
        gap:5px; 
    }
    .card{
        padding:20px 20px 37px;
        border:1px solid #fff;
        contain:content;
        background-color: #fff;
        max-width: fit-content;
    }
    .card:hover{
        border:1px solid #d4d4d4;
        box-shadow: 0 7px 15px rgba(218, 220, 230, 0.4);
        transform:scale(1.00);
        transition: all 0.5s ease-in-out;
    }

    /* menu list */
    .dishes-list{
        gap:25px;
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

    /* utility styles */
    .active{
        color:orange;
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