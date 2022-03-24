<template>
    <header>
        <div class="left-header">
            <h1 v-if="restaurantCount">{{ restaurantCount }} restaurants</h1>
            <h1 v-else>No restaurants</h1>
        </div>
        <div class="right-header" v-if="restaurantCount">
            <select name="links" class="link-dropdown" @change="sortRestaurantsDropdown">
                <option value="null" selected disabled>Sort Restaurants</option>
                <option value="Discounts">Discounts</option>
                <option value="Rating">Rating</option>
                <option value="Lowest cost">Lowest Cost</option>
                <option value="Highest cost">Highest Cost</option>
            </select>
            <span class="link-wrapper"><router-link to="#" class="header-search" @click="sortRestaurants">Discounts</router-link></span>
            <span class="link-wrapper"><router-link to="#" class="header-search" @click="sortRestaurants">Rating</router-link></span>
            <span class="link-wrapper"><router-link to="#" class="header-search" @click="sortRestaurants">Lowest Cost</router-link></span>
            <span class="link-wrapper"><router-link to="#" class="header-search" @click="sortRestaurants">Highest Cost</router-link></span>
            <button @click="toggleFilterModal">Filter 🎛</button>
        </div>
    </header>
    <section v-if="htmlOutput.dataState === 'LOADING'">
        <Loading />
    </section>
    <section v-else-if="htmlOutput.dataState === 'SUCCESS' && restaurantCount">
        <div v-for="restaurant in htmlOutput.appData.data" :key="restaurant.restaurant_id" class="card">
            <button @click="navigateUser(restaurant.restaurant_id)" class="card-button-link">
                <div class="card-img">
                    <img :src="restaurant.restaurant_main_img" :alt="restaurant.restaurant_name">
                </div>
                <div class="card-header">
                    <h1>{{ restaurant.restaurant_name }}</h1>
                    <h2>{{ restaurant.restaurant_cuisines.join(", ") }}</h2>
                </div>
                <div class="card-body">
                    <div v-if="Number(restaurant.restaurant_rating) === 0.0" :class="[restaurant.restaurant_rating < 4 ? 'card-body-low-rating' : 'card-body-high-rating']">⭐️ --</div>
                    <div v-else-if="Number(restaurant.restaurant_rating) !== 0" :class="[restaurant.restaurant_rating < 4 ? 'card-body-low-rating' : 'card-body-high-rating']">⭐️ {{ restaurant.restaurant_rating }}</div>
                    <div>₹{{ restaurant.restaurant_cost }} FOR TWO</div>
                </div>
                <div v-show="restaurant.discount_isValid" class="card-discounts">
                    <span>{{ restaurant.discounts.discount_text}}</span>
                </div>
            </button>
        </div>
    </section>
    <section v-else-if="htmlOutput.dataState === 'SUCCESS' && !restaurantCount">
        <Error message="No restaurants found in this location. Please check again soon to see if there are restaurants located near you" />
    </section>
    <section v-else-if="htmlOutput.dataState === 'ERROR'">
        <Error message="Page was not found" />
    </section>
    <div class="filter-overlay" v-if="cuisineList.dataState === 'SUCCESS' && cuisineList.appData.data.length">
        <aside class="filter-modal">
            <div class="filter-header">
                <button @click="toggleFilterModal">X</button>
                <h1>Filters</h1>
            </div>
            <div class="filter-body">
                <h1>Cuisines</h1>
                <div class="filter-form">
                    <div class="form-field" v-for="cuisine in cuisineList.appData.data" :key="cuisine.cuisine_id">
                        <input type="checkbox" :name="cuisine.cuisine_name">
                        <label :for="cuisine.cuisine_name">{{ cuisine.cuisine_name }}</label>
                    </div>
                </div>
            </div>
            <div class="filter-selection">
                <button @click="clearFilter">Clear</button>
                <button @click="filterCuisines">Show Restaurants</button>
            </div>
        </aside>
    </div>
</template>

<script lang="ts">
import { FetchResponse, ResponseAppState, Restaurant, Discount, Cuisine } from '../types/fetch-types';
import { computed, defineComponent, onMounted, ref, watch } from 'vue';
import { useRouter } from 'vue-router';
import { useFetch } from '../utils/useFetch';
import { useStore } from 'vuex';
import Error from '../components/Error.vue';
import Loading from '../components/Loading.vue';

export default defineComponent({
    components:{
        Error,
        Loading,
    },
    setup () {
        let isModalShowing = true;
        let fetchResult= ref({} as ResponseAppState<FetchResponse<Restaurant<Discount>>>);
        let htmlOutput = ref({} as ResponseAppState<FetchResponse<Restaurant<Discount>>>);
        let cuisineList = ref({} as ResponseAppState<FetchResponse<Cuisine>>);
        let restaurantCount = ref(0);
        const router = useRouter();
        const store = useStore();

        // component functions/methods
        const sortRestaurants = (e:any) => {
            let elementText = e.target.parentElement.textContent;
            let elementTextContent = e.target.parentElement.textContent.toLowerCase();
            sortHelper(elementText,elementTextContent);  
            
            // set select element index value
            let selectElement = document.querySelector('.link-dropdown') as HTMLSelectElement;
            selectElement.childNodes.forEach((element,i)=>{
                if(element.textContent === elementTextContent){
                    selectElement.selectedIndex = i;
                }
            })

        }
        const sortRestaurantsDropdown = (e:any) => {
            let elementText = e.target.value;
            let elementTextContent = e.target.value.toLowerCase();
            sortHelper(elementText,elementTextContent);
            window.scrollTo({top:0,behavior:'smooth'})
        }
        const toggleFilterModal = () => {
            let filterElement = document.querySelector('.filter-overlay') as HTMLDivElement;
            let filterModal = document.querySelector('.filter-modal') as HTMLDivElement;
            if(!isModalShowing){
                isModalShowing = !isModalShowing;
                filterElement.style.backgroundColor="transparent";
                filterElement.style.transition="all 1.25s ease-in";

                filterModal.style.transform="translateX(400px)";
                filterModal.style.opacity="0";
                filterModal.style.transition="all 1.25s ease-in";

                setTimeout(()=>{
                    filterElement.style.zIndex="-10";
                },1100)

            } else {
                isModalShowing = !isModalShowing;
                filterElement.style.backgroundColor="rgba(0,0,0,0.5)";
                filterElement.style.zIndex="10";
                filterElement.style.transition="all 0s ease-in";
                
                filterModal.style.transform="translateX(0px)";
                filterModal.style.opacity="1";
                filterModal.style.transition="all 1.25s ease-in";
            }
        }
        const navigateUser = (id:string) => {
            router.push({
                name:"Restaurant",
                params:{
                    id
                }
            })
        }
        const clearFilter = () => {
            // unchecks all inputs
            document.querySelectorAll('.form-field').forEach((item)=>{
                let inputElement = item.firstElementChild as HTMLInputElement;
                if(inputElement.checked){
                    inputElement.checked = false;
                }                
            });

            // resets the restaurant list
            htmlOutput.value = fetchResult.value;
            restaurantCount.value = htmlOutput.value.appData?.data.length!;
        }
        const filterCuisines = () => {
            // loops through all cuisine choices and filters checked inputs
            let inputArray:string[] = [...document.querySelectorAll('.form-field')].reduce((acc:string[],val)=>{
                let inputElement = val.firstElementChild as HTMLInputElement;
                if(inputElement.checked){
                    return [...acc,inputElement.name]
                } else {
                    return acc
                }
            },[]);

            // filtering out restaurant to include checked items
            let filteredArray = fetchResult.value.appData?.data.reduce((acc:Restaurant<Discount>[],val)=>{
                inputArray.forEach(input=>{
                    if(val.restaurant_cuisines.includes(input)){
                        // check to see if filterArray already has the restaurant
                        if(!acc.find(fil=>fil === val)){
                            acc = [...acc,val as Restaurant<Discount>];
                        } 
                    } 
                });
                return acc;
            },[]);

            // new object to populate the restaurant list
            if(filteredArray!.length){
                let newSearchResult = fetchResult.value;
                newSearchResult = {
                    ...newSearchResult,
                    appData:{
                        ...newSearchResult.appData!,
                        data:filteredArray!
                    }
                }
                // reset restaurant list and count
                htmlOutput.value = newSearchResult;
                restaurantCount.value = htmlOutput.value.appData?.data.length!;

                // close filter sidebar
                toggleFilterModal();
            } else {
                toggleFilterModal();
            }

        }

        // computed
        const userLocation = computed(() => store.state.location.state.location);

        // watch
        watch(userLocation,()=>{
            if(userLocation.value){
                getRestaurants();
            }
        })

        // fetch
        const getRestaurants = async() => {
            let { dataState, data, errorMsg } = await useFetch<FetchResponse<Restaurant<Discount>>>("http://localhost:8000/api/v1/restaurants");
            htmlOutput.value.appData = data.value as FetchResponse<Restaurant<Discount>>;
            htmlOutput.value.dataState = dataState.value;
            htmlOutput.value.error = errorMsg.value;
            let filteredRestaurants = htmlOutput.value.appData!.data.filter(item=>item.restaurant_city.includes(userLocation.value));
            restaurantCount.value = filteredRestaurants.length;
            htmlOutput.value.appData!.data = filteredRestaurants;
            fetchResult.value = htmlOutput.value;
        }
        const getCuisines = async() => {
            let { dataState, data, errorMsg } = await useFetch<FetchResponse<Cuisine>>("http://localhost:8000/api/v1/cuisines");
            cuisineList.value.dataState = dataState.value;
            cuisineList.value.appData = data.value as FetchResponse<Cuisine>;
            cuisineList.value.error = errorMsg.value;
        }


        // helper functions
        const sortHelper = (loopText:string,sortText:string) => {
            // setting styles for active selection
            document.querySelectorAll('.link-wrapper').forEach(item=>{
                let itemTextContent = item.textContent;
                if(loopText === itemTextContent){
                    item.classList.add("active");
                } else {
                    item.classList.remove("active");
                }
            });

            // sorting the restaurants list
            switch (sortText) {
                case "discounts":
                    htmlOutput.value.appData?.data.sort((a,b)=>Number(b.discount_isValid) - Number(a.discount_isValid));
                    break;
                case "rating":
                    htmlOutput.value.appData?.data.sort((a,b)=>b.restaurant_rating - a.restaurant_rating);
                    break;
                case "lowest cost":
                    htmlOutput.value.appData?.data.sort((a,b)=>a.restaurant_cost - b.restaurant_cost);
                    break;
                case "highest cost":
                    htmlOutput.value.appData?.data.sort((a,b)=>b.restaurant_cost - a.restaurant_cost);
                    break;
                default:
                    break;
            }
        }

        // lifecycle hooks
        onMounted(()=>{
            getRestaurants();
            getCuisines();
            store.dispatch('location/setLocationAction',"");
            if(!userLocation.value){
                router.push({name:"Home"});
            }
            store.dispatch('cart/setCartAction',[]);
        });

        return {
            sortRestaurants,
            sortRestaurantsDropdown,
            toggleFilterModal,
            fetchResult,
            htmlOutput,
            navigateUser,
            restaurantCount,
            cuisineList,
            clearFilter,
            filterCuisines,
        }
    }
})
</script>

<style scoped>
header{
    position:fixed;
    top:80px;
    left: 5%;
    background-color: #fff;
    height: 75px;
    width: 90%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid #e4e4e4;
    padding:-20px 0;
    z-index: 10;
    box-shadow: 0 5px 7px rgba(210, 220, 230, 0.6);
}
.left-header h1{
    font-size: 28px;
    text-align: center;
    margin-left: 10px;
}
.right-header{
    height: 100%;
    font-size: 14px;
    display: flex;
    align-items: end;
    justify-content: center;
    gap: 15px;
    margin:0 5px;
}
.right-header .link-dropdown{
    display:none;
}
.right-header span{
    height: 100%;
    display: flex;
    align-items: end;
    text-align: center;
}
.right-header span.active{
    border-bottom: 1px solid #333;
}
.header-search{
    margin-bottom: 10px;
}
.right-header button{
    margin-left: 10px;
    margin-bottom: 10px;
    background-color: #fff;
    outline: none;
    border: 0;
    cursor: pointer;
    padding: 5px 10px;
    font-weight: 700;
    font-size: 15px;
}
.right-header button:hover{
    color:#fc8019;
}

section{
    margin-top: 75px;
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
.card-button-link{
    background-color: transparent;
    outline: none;
    border:none;
    cursor: pointer;
}
.card-img img{
    width: 100%;
    height: 100%;
    object-fit: contain;
    object-position: center;
}
.card-header{
    margin-top: 14px;
}
.card-header h1{
    font-size: 17px;
    font-weight: 500;
    word-break: break-word;
    text-align: left;
}
.card-header h2{
    font-size: 13px;
    color:#686b78;
    margin-top: 4px;
    font-weight: 100;
    text-align: left;
}
.card-body{
    display: flex;
    align-items: center;
    margin-top: 18px;
    font-size: 12px;
    justify-content: space-between;
    color:#535665;
}
.card-body div:first-child{
    display: flex;
    align-items: center;
    justify-content: center;
    color:#fff;
    width: 43px;
    height: 20px;
    font-weight: 400;
}
.card-body-low-rating{
    background-color: #b1500f;;
}
.card-body-high-rating{
    background-color: #48c479;
}
.card-discounts{
    border-top: 1px solid #e9e9e9;
    padding-top: 14px;
    margin-top: 14px;
    display: flex;
    align-items: center;
    font-weight: 500;
    font-size: 14px;
}
.card-discounts span{
    color:#8a584b;
}

.filter-overlay{
    width: 100vw;
    height: 100vh;
    background-color: transparent;
    position:fixed;
    top:0;
    left:0;
    right:0;
    bottom:0;
    z-index: -10;
}
.filter-modal{
    width: 400px;
    height: 100vh;
    position: absolute;
    top:0;
    bottom:0;
    right:0px;
    opacity:0;
    transform: translateX(400px);
    background-color: #fff;
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: 10vh 75vh 10vh;
    gap:2.5vh;
}
.filter-header{
    padding:0 50px;
    display: flex;
    align-items: center;
    justify-content: start;
    gap: 15px;
    box-shadow: 0 5px 7px rgba(0, 0, 0, 0.1);
}
.filter-header button{
    font-size: 18px;
    font-weight: 500;
    background-color: transparent;
    border:none;
    outline:none;
    cursor: pointer;
}
.filter-body{
    padding:0 50px;
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 15px;
}
.filter-body h1{
    width: 100%;
    grid-row: 1/2;
    grid-column: 1/-1;
    font-size: 18px;
}
.filter-form{
    width: 100%;
    height:inherit;
    display: grid;
    grid-template-columns: repeat(2,1fr);
    grid-auto-rows: 35px;
    align-items: center;
    overflow-y: scroll;
    background-color: rgba(238, 238, 238,0.3);
    padding:0 10px;
}
.form-field{
    width: 100%;
    height: 25px;
    display: flex;
    align-items: center;
    gap: 7px;
    font-size: 14px;
}
.filter-selection{
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-columns: 30% 70%;
    align-items: center;
    justify-items: center;
}
.filter-selection button{
    height: 75%;
    width: 85%;
}
.filter-selection button:nth-child(1){
    color:#8e9096;
    background-color: transparent;
    border:1px solid #696b79;
    cursor: pointer;
    font-size: 14px;
    text-transform: uppercase;
    font-weight: 600;
    outline:none;
}
.filter-selection button:nth-child(2){
    background-color: #fc8019;
    color:#fff;
    border:none;
    outline:none;
    font-size: 14px;
    text-transform: uppercase;
    font-weight: 600;
    cursor: pointer;
}




@media (max-width:821px) {
    header{
        flex-direction: column;
        height:fit-content;
        background-color: #fff;
    }
}
@media (max-width:580px) {
    .right-header{
        flex-direction: column;
        margin-top: 10px;
        width: 100%;
        align-items: center;
    }
    .right-header span{
        display: none;
    }
    .right-header .link-dropdown{
        display:block;
        width: fit-content;
        outline:none;
        border:none;
        font-size: 16px;
    }

    section{
        margin-top: 130px;
    }
}

</style>