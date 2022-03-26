import { Route } from "@/types/route";
import { createRouter, createWebHistory } from "vue-router";
import Restaurants from '../components/Restaurants.vue'
import Restaurant from '../components/Restaurant.vue'
import Home from '../components/Home.vue';
import Checkout from '../components/Checkout.vue';
import Confirmation from '../components/Confirmation.vue';
import Search from '../components/Search.vue';

const routes:Route[] = [
    {
        path:"/",
        name:"Home",
        component:Home
    },
    {
        path:"/restaurants",
        name:"Restaurants",
        component:Restaurants
    },
    {
        path:"/restaurants/:id",
        name:"Restaurant",
        component:Restaurant
    },
    {
        path:"/checkout",
        name:"Checkout",
        component:Checkout
    },
    {
        path:"/confirmation/:id",
        name:"Confirmation",
        component:Confirmation
    },
    {
        path:"/search",
        name:"Search",
        component:Search
    }
]

const router = createRouter({
    history:createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;