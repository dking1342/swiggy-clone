<template>
    <section v-if="responseStatus == 'LOADING'">
        <Loading />
    </section>
    <section v-else-if="responseStatus == 'SUCCESS'">
        <div class="order-confirmation-container" >
            <section class="order-confirmation">
                <header>
                    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQabJmScE6MDseLYTjfRIgsN2hXmFqDeik0Daoj93Z_OVeG-yki5tm8xBubspsQ4Js-nBk&usqp=CAU" alt="delivery person">
                    <h1>Order Confirmed</h1>
                    <p>Sit back and relax. Your delicious order will arrive momentarily.</p>
                </header>
                <div class="order-confirmation-body">
                    <div class="order-confirmation-review">
                        <div class="order-confirmation-info">
                            <div class="order-confirmation-info-header">
                                <h1>Order Details</h1>
                                <p>{{ orderId }}</p>
                            </div>
                            <button class="order-view-details-btn" @click="toggleOrderView">
                                <img src="data:image/png;base64,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" alt="search">
                            </button>
                        </div>
                        <div class="order-confirmation-details">
                            <div class="order-item" v-for="order in orderList" :key="order.order_item_name">
                                <h1>{{ order.order_item_name }}</h1>
                                <p>{{ order.order_item_quantity }}</p>
                                <p>${{ order.order_item_cost }}</p>
                            </div>
                        </div>
                    </div>
                    <div class="order-confirmation-rating">
                        <header>
                            <h1>Help Us</h1>
                            <p>Rate your experience with this restaurant</p>
                        </header>
                        <div class="order-rating-container" v-if="!hasRated">
                            <div class="rating-btns" v-for="btn in ratingBtnArray" :key="btn">
                                <button class="rating-btn" @click="rateRestaurant(btn)">
                                    <img src="https://pixlok.com/wp-content/uploads/2021/10/Star_SVG_icon_9jomrsks.png" alt="rating star">
                                </button>
                            </div>
                        </div>
                        <h1 class="has-rated-heading" v-else-if="hasRated">Thank you for giving your rating!</h1>
                    </div>
                </div>
            </section>
            <section class="order-tracking">
                <header>
                    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIXbOHL7q5xIX6Su5DpK8N4yi7Wx-LGILFj8FKCuAuLdsSgX7Gjqy3GWVwwOhYSy0tqKI&usqp=CAU" alt="delivery map">
                    <h1>Arriving soon</h1>
                    <p>Express Delivery</p>
                </header>
                <div class="order-tracking-dashboard">
                    <div class="order-tracking-ordered order-tracking-status">
                        <img src="https://cdns.iconmonstr.com/wp-content/assets/preview/2012/240/iconmonstr-check-mark-1.png" alt="ordered check">
                        <span>Ordered</span>
                    </div>
                    <div class="order-tracking-transit order-tracking-status">
                        <img src="data:image/png;base64,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" alt="transit">
                        <span>In transit</span>
                    </div>
                    <div class="order-tracking-delivered order-tracking-status">
                        <img src="https://cdns.iconmonstr.com/wp-content/assets/preview/2012/240/iconmonstr-check-mark-1.png" alt="delivered check">
                        <span>Delivered</span>
                    </div>
                </div>
                <div class="order-tracking-delivery-person">
                    <img src="data:image/png;base64,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" alt="delivery person">
                    <div class="delivery-person-info">
                        <h3>Joe Jackson</h3>
                        <p>E45W32</p>
                    </div>
                    <button class="call-delivery-btn">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Telephone_receiver.svg/2048px-Telephone_receiver.svg.png" alt="call delivery person">
                    </button>
                </div>
            </section>
        </div>
    </section>
    <section v-else-if="responseStatus == 'ERROR'">
        <Error message="Page not found" />
    </section>
</template>

<script lang="ts">
import { DATASTATE, FetchResponse, Order, OrderConfirmationItem, Rating, ResponseAppState } from '@/types/fetch-types';
import { computed, defineComponent, onMounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router';
import Error from '../components/Error.vue';
import Loading from '../components/Loading.vue';
import { useAPICall, useFetch } from '../utils/useFetch';

export default defineComponent({
    components:{
        Error,
        Loading,
    },
    setup () {
        const route = useRoute();
        let hasRated = ref(false);
        let toggleViewOrder = ref(false);
        let ratingBtnArray = ref([1,2,3,4,5]);
        let orderResponseRef = ref({} as ResponseAppState<FetchResponse<OrderConfirmationItem>>)
        let ratingResponseRef = ref({} as ResponseAppState<FetchResponse<Rating>>);
        let ratingCheckResponse = {} as ResponseAppState<FetchResponse<Rating>>;
        let ratingCheckResponseRef = ref({} as ResponseAppState<FetchResponse<Rating>>);
        
        
        // component functions/methods
        const toggleOrderView = () => {
            toggleViewOrder.value = !toggleViewOrder.value
            let orders = document.querySelector('.order-confirmation-details') as HTMLDivElement;

            if(toggleViewOrder.value){
                orders.classList.add('drawer-open');
            } else {
                orders.classList.remove('drawer-open');
            }
        }

        // computed
        const responseStatus = computed(()=> orderResponseRef.value.dataState);
        const orderList = computed(()=> orderResponseRef.value.appData?.data);
        const orderId = computed(()=> orderResponseRef.value.appData?.data[0].order_reference);
        const orderRestaurant = computed(()=> orderResponseRef.value.appData?.data[0].order_restaurant);

        // watch
        watch(orderId, ()=>{
            checkRating();
        },{
            flush: 'post'
        })

        // fetches
        const getOrder = async () => {
            const confirmation_id = route.params.id as string;
            let { dataState, data, errorMsg } = await useFetch<FetchResponse<Order>>(`http://localhost:8000/api/v1/cart/get/${confirmation_id}`);
            orderResponseRef.value.dataState = dataState.value;
            orderResponseRef.value.appData = data.value as FetchResponse<OrderConfirmationItem>;
            orderResponseRef.value.error = errorMsg.value;
        }
        const checkRating = async () => {
            let { dataState, data, errorMsg } = await useFetch<FetchResponse<Rating>>(`http://localhost:8000/api/v1/rating/get/${orderId.value}/`);
            ratingCheckResponseRef.value.dataState = dataState.value;
            ratingCheckResponseRef.value.error = errorMsg.value;
            ratingCheckResponseRef.value.appData = data.value as FetchResponse<Rating>;

            if(ratingCheckResponseRef.value.appData.data.length){
                hasRated.value = true;
                ratingCheckResponseRef.value = ratingCheckResponse;
            } else {
                hasRated.value = false;
            }
        }
        const rateRestaurant = async (rating:number) => {
            let payload:Rating = {
                rating_id:"",
                rating_rate:rating,
                rating_order_reference:orderId.value!,
                rating_restaurant:orderRestaurant.value!
            }

            let { dataState, data, errorMsg } = await useAPICall<FetchResponse<Rating>>('http://localhost:8000/api/v1/rating/create/',payload,"POST");
            ratingResponseRef.value.dataState = dataState.value;
            ratingResponseRef.value.error = errorMsg.value;
            ratingResponseRef.value.appData = data.value as FetchResponse<Rating>;
            
            if(dataState.value === DATASTATE.success){
                hasRated.value = true;
            }
        }

        // lifecycle hooks
        onMounted(()=>{
            getOrder();
        });
        


        return {
            hasRated,
            toggleOrderView,
            rateRestaurant,
            ratingBtnArray,
            responseStatus,
            orderList,
            orderId,
        }
    }
})
</script>

<style scoped>
    .order-confirmation-container{
        display: grid;
        grid-template-columns: repeat(auto-fit,minmax(310px,1fr));
        gap:25px;
        padding:25px
    }
    .order-confirmation-container section{
        background-color: #fff;
        box-shadow: 0 20px 20px rgba(0, 0, 0, 0.15);
        padding:25px;
        display: flex;
        flex-direction: column;
        gap:25px;
        height: fit-content;
    }

    /* section headers */
    .order-confirmation header,
    .order-tracking header{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .order-confirmation header img,
    .order-tracking header img{
        width: 200px;
        object-fit: cover;
        object-position: center;
        margin-bottom: 30px;
    }
    .order-confirmation header h1,
    .order-tracking header h1{
        font-size: 22px;
        margin-bottom: 10px;
        text-align: center;
    }
    .order-confirmation header p,
    .order-tracking header p{
        font-size: 14px;
        color:#555;
        text-align: center;
    }


    /* order body content  */
    .order-confirmation-body{
        display: flex;
        flex-direction: column;
        gap:25px;
    }

    /* review */
    .order-confirmation-review{
        height: fit-content;
        display: flex;
        flex-direction: column;
        gap:25px;
    }
    .order-confirmation-info{
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 1px solid #ccc;
        padding-bottom: 20px;
    }
    .order-confirmation-review h1{
        font-size: 18px;
        margin-bottom: 5px;
    }
    .order-confirmation-review p{
        font-size: 13px;
        color:#555;
    }
    .order-confirmation-review button{
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #fff;
        outline:none;
        border:none;
        position: relative;
    }
    .order-confirmation-review button:hover::after{
        content:'View Details';
        background-color: #555;
        font-size: 12px;
        border-radius: 5px;
        color:#fff;
        width: 70px;
        padding:7px;
        position: absolute;
        top:-100%;
        right:0;
    }
    .order-confirmation-review button img{
        width: 35px;
        height: 35px;
    }
    .order-confirmation-details{
        max-height: 0;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        gap:15px;
        justify-content: center;
        transition:max-height 1s ease;
    }
    .drawer-open{
        max-height:1000px;
        transition:max-height 2s ease;
    }
    .order-item{
        display: grid;
        grid-template-columns: 60% 15% 15%;
        grid-auto-rows: minmax(35px,auto);
        text-align: center;
        justify-content: space-between;
    }
    .order-item h1{
        text-align: left;
    }

    /* rating */
    .order-confirmation-rating{
        display: flex;
        flex-direction: column;
        gap:25px;
    }
    .order-rating-container{
        width: 300px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin:0 auto;
    }
    .rating-btns{
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
    }
    .rating-btns button{
        background-color: #fff;
        outline:0;
        border:0;
        display: flex;
        align-items: center;
    }
    .rating-btns button img{
        width: 40px;
        height: 40px;
    }
    .has-rated-heading{
        font-size: 18px;
        text-align: center;
    }


    /* tracking section */
    .order-tracking-dashboard{
        display: flex;
        align-items: center;
        justify-content: space-around;
    }
    .order-tracking-status{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 7px;
    }
    .order-tracking-status img{
        width: 30px;
    }

    /* delivery person */
    .order-tracking-delivery-person{
        display: flex;
        align-content: center;
        justify-content: space-between;
    }
    .order-tracking-delivery-person img{
        width: 40px;
    }
    .delivery-person-info{
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .call-delivery-btn{
        background-color: #fff;
        outline:0;
        border:0;
    }
    .call-delivery-btn img{
        width: 40px;
    }

</style>