<template>
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
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useRouter } from 'vue-router';

export default defineComponent({
    props:['restaurant'],
    setup () {
        const router = useRouter();

        // component functions/methods
        const navigateUser = (id:string) => {
            router.push({
                name:"Restaurant",
                params:{
                    id
                }
            })
        }


        return {
            navigateUser,
        }
    }
})
</script>

<style scoped>
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
</style>