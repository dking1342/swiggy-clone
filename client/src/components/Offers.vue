<template>
    <section v-if="discountsList.dataState == Datastate.loading">
        <Loading />
    </section>
    <section v-else-if="discountsList.dataState == Datastate.success">
        <header>
            <h1>Offers for you</h1>
            <p>Explore top deals and offers exclusively for you!</p>
            <img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto/KHu24Gqw_md3ham" alt="offers image">
        </header>
        <section class="offers-body">
            <h2>Available Coupons</h2>
            <div class="coupon-rows">
                <div class="coupon-card" v-for="discount in discountsList.appData?.data" :key="discount.discount_id">
                    <div class="coupon-header">
                        <div class="coupon-header-img">
                            <img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_40,h_40/rng/md/ads/production/erekfyr0fbegrttflbvw" alt="coupon image">
                        </div>
                        <div class="coupon-header-code">
                            {{ discount.discount_code }}
                        </div>
                    </div>
                    <div class="coupon-body">
                        <h3>{{ discount.discount_text }}</h3>
                        <p>Maximum discount up to ₹100 on orders above ₹400</p>
                    </div>
                </div>
            </div>
        </section>
    </section>
    <section v-else-if="discountsList.dataState == Datastate.error">
        <Error message="Page not found"/>
    </section>
</template>

<script lang="ts">
import { DATASTATE, Discount, FetchResponse, ResponseAppState } from '@/types/fetch-types'
import { useFetch } from '@/utils/useFetch'
import { defineComponent, onMounted, ref } from 'vue'
import Loading from '../components/Loading.vue';
import Error from '../components/Error.vue';

export default defineComponent({
    components:{
        Loading,
        Error
    },
    setup () {
        let discountsList = ref({} as ResponseAppState<FetchResponse<Discount>>);
        let Datastate = DATASTATE;


        // fetches
        const getOffers = async () => {
            let { dataState, data, errorMsg } = await useFetch<FetchResponse<Discount>>("http://localhost:8000/api/v1/discounts");
            discountsList.value.dataState = dataState.value;
            discountsList.value.appData = data.value as FetchResponse<Discount>;
            discountsList.value.error = errorMsg.value;
        }

        // lifecycle hooks
        onMounted(()=>{
            getOffers();
        })
        

        return {
            Datastate,
            discountsList,
        }
    }
})
</script>

<style scoped>
    header{
        height: 300px;
        display: grid;
        grid-template-columns: repeat(12,1fr);
        grid-template-rows: repeat(12,1fr);
        background-color: #005062;
        margin:0 -5%;
        align-items: flex-start;
        justify-content: center;
        margin-bottom: 50px;
        gap:15px;
    }
    header h1,
    header p{
        grid-column: 2/9;
        color:#fff;
    }
    header h1{
        grid-row: 4/7;
        font-size: 48px;
    }
    header p{
        grid-row:7/-1;
        font-size: 20px;
    }
    header img{
        width: 80%;
        grid-column: 9/-1;
        grid-row: 1/-1;
        align-self:center;
    }

    /* body styles */
    .offers-body{
        margin-bottom: 50px;
    }
    .offers-body h2{
        margin-bottom: 25px;
    }
    .coupon-rows{
        display: grid;
        grid-template-columns: repeat(auto-fill,minmax(300px,1fr));
        grid-auto-rows: minmax(100px,auto);
        gap:15px;
    }
    .coupon-card{
        border:1px solid #005062;
        padding:15px;
        display: flex;
        flex-direction: column;
        gap:10px;
        border-radius: 5px;
        align-items: flex-start;
        justify-content: center;
    }
    .coupon-header{
        display: flex;
        align-items: center;
        justify-content: space-around;
        gap:10px;
        padding:5px 10px;
        border-radius: 5px;
        border:1px solid #005062;
    }
    .coupon-header-img{
        display: flex;
        align-items: center;
    }
    .coupon-header-img img{
        width: 25px;
    }
    .coupon-header-code{
        font-size: 14px;
        font-weight: 600;
    }
    .coupon-body{
        display: flex;
        flex-direction: column;
        gap:5px;
    }
    .coupon-body h3{
        font-size: 16px;
    }
    .coupon-body p{
        font-size: 13px;
        color:#888;
    }

    @media (max-width:550px) {
        header h1{
            font-size: 30px;
        }
        header p{
            font-size: 16px;
        }
    }
</style>