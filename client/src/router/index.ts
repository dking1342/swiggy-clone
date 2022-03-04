import { Route } from "@/types";
import { createRouter, createWebHistory } from "vue-router";
import Restaurants from '../components/Restaurants.vue'

const routes:Route[] = [
    {
        path:"/",
        name:"Restaurants",
        component:Restaurants
    }
]

const router = createRouter({
    history:createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;