<template>
    <section v-if="!isCartFilled" class="cart-empty-container">
        <div class="cart-empty-subcontainer">
            <div class="cart-empty-img-wrapper">
                <img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto/2xempty_cart_yfxml0" alt="image for cart not filled">
            </div>
            <div class="cart-empty-text-wrapper">
                <h1>Your cart is empty</h1>
                <p>You can go to the home page to view restaurants</p>
            </div>
            <router-link class="cart-empty-btn" to="/">See Restaurants Near You</router-link>
        </div>
    </section>
    <section v-else-if="isCartFilled && !isPaymentModal" class="cart-fill-container ">
        <div class="account-container cart-container view-containers">
            <h1>Account</h1>
            <p class="login-class">To place your order now, log in to your existing account or sign up.</p>
            <button class="account-login account-btn"><span>Have an account?</span><span>Log In</span></button>
            <button class="account-signup account-btn"><span>New to Swiggy?</span><span>Sign Up</span></button>
            <div class="account-img-container">
                <img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_147,h_140/Image-login_btpq7r" alt="account picture">
                
            </div>
        </div>
        <div class="delivery-container cart-container view-containers">
            <h1>Delivery address</h1>
            <div class="delivery-address-container">
                <address>
                    123 Main St.
                </address>
                <address>
                    Apt 13
                </address>
                <address>
                    City, State Zip
                </address>
            </div>
            <div class="delivery-img-container">
                <img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto/empty-plate_fdc3wq" alt="delivery image">
            </div>
        </div>
        <div class="payment-container cart-container view-containers">
            <h1>Payment</h1>
            <button class="cc-btn" @click="goToPaymentModal"><span>Pay with</span><span>Credit Cart</span></button>
            <button class="paypal-btn" @click="goToPaymentModal"><span>Pay with</span><span>Paypal</span></button>
            <img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_90,h_90/marketing-dashboard/carousel/ftnsdmo6fotidtzobbm2" alt="payment image">
        </div>
        <div class="order-container view-containers">
            <div class="restaurant-info-container">
                <router-link :to="restaurantLink" class="restaurant-wrapper">
                    <img :src="restaurantImage" alt="restaurant image">
                    <h1>{{ restaurantName }}</h1>
                    <p>{{ restaurantLocation }}</p>
                </router-link>
            </div>
            <div class="order-item-container">
                <div class="order-item" v-for="item in cart.order_item" :key="item.order_id">
                    <span>{{ item.order_item_name.menu_item }}</span>
                    <div class="order-btn-container">
                        <button class="decrease-order" @click="decreaseOrder(item.order_item_name.menu_id)">-</button>
                        <span class="order-quantity">{{ item.order_item_quantity }}</span>
                        <button class="add-order" @click="addOrder(item.order_item_name.menu_id)">+</button>
                    </div>
                    <p class="order-cost">${{ item.order_item_quantity * item.order_item_name.menu_price }}</p>
                </div>
            </div>
            <div class="order-totals-container">
                <h2>Bill Details</h2>
                <div class="totals-row">
                    <p>Order total</p>
                    <p>${{ cart.cart_cost }}</p>
                </div>
                <div class="totals-row">
                    <p>Delivery Fee</p>
                    <p>$50</p>
                </div>
                <div class="totals-row">
                    <p>Taxes and Charges</p>
                    <p>${{ (cart.cart_cost * .07).toFixed(2) }}</p>
                </div>
                <div class="totals-row">
                    <p>To Pay</p>
                    <p>${{ (cart.cart_cost + (cart.cart_cost * 1.07 ) + 50).toFixed(2)}}</p>
                </div>
            </div>
        </div>
    </section>
    <section class="payment-modal" v-else-if="isCartFilled && isPaymentModal">
        <div class="pay-container" v-if="!isPaymentProcessing">
            <button class="close-payment-btn" @click="closePaymentModal">X</button>
            <div class="checkout-header">
                <h1>Checkout</h1>
                <h2>${{ paymentModalCost.toFixed(2) }}</h2>
            </div>
            <div class="checkout-body">
                <h3>Payment method</h3>
                <form @submit.prevent="makePayment" >
                    <div class="form-row">
                        <div class="form-field">
                            <label for="ccn">Account/Card Number:</label>
                            <input 
                                id="ccn" 
                                type="tel" 
                                inputmode="numeric" 
                                pattern="[0-9\s]{13,19}" 
                                autocomplete="cc-number" 
                                maxlength="19" 
                                placeholder="xxxx xxxx xxxx xxxx"
                                v-model="orderReceipt.number"
                            />
                        </div>
                    </div>
                    <div class="form-row">
                        <div class="form-field">
                            <label for="name">Name on Account/Card</label>
                            <input 
                                type="text" 
                                pattern="^[a-zA-Z]{2,15}[\s]{1}[a-zA-Z]{2,15}$" 
                                name="name" 
                                id="name" 
                                autocomplete="off" 
                                placeholder="Clark Kent"
                                v-model="orderReceipt.customer"
                            >
                        </div>
                    </div>
                    <div class="form-row">
                        <div class="form-field">
                            <label for="inputExpDate">Expiry Date</label>
                            <input 
                                type="text" 
                                id="inputExpDate" 
                                placeholder="MM/YY" 
                                pattern="[0-9]{2}/[0-9]{2}" 
                                maxlength='7'
                                v-model="orderReceipt.expiry"
                            />
                        </div>
                        <div class="form-field">
                            <label for="cvv">CVV</label>
                            <input 
                                type="password" 
                                name="cvv" 
                                pattern="[0-9]{3}" 
                                id="cvv" 
                                maxlength="3"
                                v-model="orderReceipt.cvv"
                            >
                        </div>
                    </div>
                    <div class="form-row">
                        <div class="form-field">
                            <button type="submit" class="payment-btn">Pay</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
        <div class="payment-confirmation" v-else-if="isPaymentProcessing">
            <h1>Payment is being processed</h1>
            <p>Please do not refresh or go to previous screen</p>
            <svg version="1.1" id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                viewBox="0 0 100 50" enable-background="new 0 0 0 0" xml:space="preserve">
                <circle fill="#fc8019" stroke="none" cx="0" cy="25" r="15">
                    <animate
                    attributeName="opacity"
                    dur="1s"
                    values="0;1;0"
                    repeatCount="indefinite"
                    begin="0.1"/>    
                </circle>
                <circle fill="#fc8019" stroke="none" cx="50" cy="25" r="15">
                    <animate
                    attributeName="opacity"
                    dur="1s"
                    values="0;1;0"
                    repeatCount="indefinite" 
                    begin="0.2"/>       
                </circle>
                <circle fill="#fc8019" stroke="none" cx="100" cy="25" r="15">
                    <animate
                    attributeName="opacity"
                    dur="1s"
                    values="0;1;0"
                    repeatCount="indefinite" 
                    begin="0.3"/>     
                </circle>
                </svg>
        </div>
    </section>

</template>

<script lang="ts">
import { Discount, Order, OrderReceipt, Restaurant } from '@/types/fetch-types';
import { computed, defineComponent, onMounted, ref } from 'vue'
import { useRouter } from 'vue-router';

export default defineComponent({
    setup () {
        let isCartFilled = ref(false);
        let cart = ref({} as Order);
        let restaurant = ref({} as Restaurant<Discount>)
        let orderReceipt = ref({} as OrderReceipt);
        let isPaymentProcessing = ref(false);
        let isPaymentModal = ref(false);
        let router = useRouter();



        // component functions/methods
        const getLocalStorage = () => {
            let localState = localStorage.getItem('cart');
            if(localState){
                isCartFilled.value = true;
                cart.value = JSON.parse(localState);
                let id = cart.value.order_item[0].order_item_name.restaurant;
                getRestaurant(id)
            }
        }
        const addOrder = (id:string) => {
            let index = cart.value.order_item.findIndex(x=>x.order_item_name.menu_id === id);
            let quantity = cart.value.order_item[index].order_item_quantity + 1;
            cart.value.order_item[index].order_item_quantity = quantity;
            cart.value.cart_quantity = cart.value.order_item.reduce((acc,val)=>acc + val.order_item_quantity,0);
            cart.value.cart_cost = cart.value.order_item.reduce((acc,val)=>acc + (val.order_item_quantity * val.order_item_name.menu_price),0);
            localStorage.setItem('cart',JSON.stringify(cart.value));            
        }
        const decreaseOrder = (id:string) => {
            let index = cart.value.order_item.findIndex(x=>x.order_item_name.menu_id === id);
            let quantity = cart.value.order_item[index].order_item_quantity - 1;
            if(!quantity){
                cart.value.order_item = cart.value.order_item.filter(x=>x.order_item_name.menu_id !== id);
            } else {
                cart.value.order_item[index].order_item_quantity = quantity;
            }
            cart.value.cart_quantity = cart.value.order_item.reduce((acc,val)=>acc + val.order_item_quantity,0);
            cart.value.cart_cost = cart.value.order_item.reduce((acc,val)=>acc + (val.order_item_quantity * val.order_item_name.menu_price),0);

            if(!cart.value.order_item.length){
                localStorage.removeItem('cart');
                cart.value = {} as Order;
                isCartFilled.value = false;
            } else {
                localStorage.setItem('cart',JSON.stringify(cart.value));
            }

        }
        const goToPaymentModal = () => {
            isPaymentModal.value = true;
        }
        const closePaymentModal = () => {
            isPaymentModal.value = false;

        }
        const makePayment = () => {
            if(Object.values(orderReceipt.value).length === 4){
                createOrder(cart.value);
            } else {
                alert("Please provide and input for all fields")
            }
        }

        // computed
        const restaurantName = computed(()=> restaurant.value.restaurant_name);
        const restaurantLocation = computed(()=> restaurant.value.restaurant_city);
        const restaurantImage = computed(()=> restaurant.value.restaurant_main_img);
        const restaurantLink = computed(()=> `/restaurants/${restaurant.value.restaurant_id}`);
        const paymentModalCost = computed(()=> cart.value.cart_cost + (cart.value.cart_cost * 1.07 ) + 50)

        // fetches
        const getRestaurant = async(id:any) => {
            try {
                const response = await fetch(`http://localhost:8000/api/v1/restaurants/${id}`);
                const data = await response.json();
                restaurant.value = data.data[0];
            } catch (error) {
                console.log(error);
            }
        }
        const createOrder = async(order:any) => {
            try {
                const response = await fetch('http://localhost:8000/api/v1/cart/create/',{
                    method: 'POST', 
                    mode: 'cors', 
                    cache: 'no-cache', 
                    credentials: 'same-origin', 
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    redirect: 'follow',
                    referrerPolicy: 'no-referrer',
                    body: JSON.stringify(order) 
                });
                const data = await response.json();
                
                if(+data.status_code === 200){
                    isPaymentProcessing.value = true;

                    // remove cart from local storage
                    localStorage.removeItem('cart');

                    // success to confirmation view
                    setTimeout(()=>{
                        router.push({name:"Restaurants"})
                        router.push({name:"Confirmation",params:{id:data.data[0].order_reference}})
                    },3000);
                }
            } catch (error) {
                console.log(error)
            }
        }

        // lifecycle hooks
        onMounted(()=>{
            getLocalStorage();
        })

        return {
            isCartFilled,
            isPaymentProcessing,
            isPaymentModal,
            cart,
            restaurantName,
            restaurantLocation,
            restaurantLink,
            restaurantImage,
            addOrder,
            decreaseOrder,
            makePayment,
            goToPaymentModal,
            closePaymentModal,
            orderReceipt,
            paymentModalCost
        }
    }
})
</script>

<style scoped>
    .cart-empty-container{
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100vw;
        height: 80vh;
    }
    .cart-empty-subcontainer{
        width: 350px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-width: 350px;
    }
    .cart-empty-img-wrapper{
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .cart-empty-img-wrapper img{
        width: 100%;
        object-fit: contain;
        object-position: center;
    }
    .cart-empty-text-wrapper h1{
        margin-top: 24px;
        font-size: 20px;
        font-weight: 600;
        color:#535665;
        text-align: center;
    }
    .cart-empty-text-wrapper p{
        margin-top: 8px;
        color:#7e808c;
        text-align: center;
    }
    .cart-empty-btn{
        margin-top: 30px;
        padding:11px 20px;
        text-transform: uppercase;
        background-color: #fc8019;
        color:#fff;
        border:0;
        outline:0;
        font-size: 15px;
        text-align: center;
    }
    .cart-empty-btn:hover{
        box-shadow: 0 4px 14px #d4d5d9;
    }

    /* cart full */
    .cart-fill-container{
        width: 100vw;
        min-height: 100vh;
        max-height: fit-content;
        background-color: #e9ecee;
        margin:0 -5%;
        padding:5%;
        display: grid;
        grid-template-columns: repeat(12,1fr);
        grid-auto-rows:max-content;
        grid-gap: 20px;
        grid-template-areas: 
        'a a a a a a a a o o o o'
        'a a a a a a a a o o o o'
        'a a a a a a a a o o o o'
        'd d d d d d d d o o o o'
        'd d d d d d d d o o o o'
        'd d d d d d d d o o o o'
        'p p p p p p p p o o o o'
        'p p p p p p p p o o o o'
        'p p p p p p p p . . . .'
        '. . . . . . . . . . . .'
        '. . . . . . . . . . . .';
    }
    .view-containers{
        background-color: #fff;
        box-shadow: 0 4px 15px #d4d5d9;
        padding:15px 25px;
        display: grid;
        gap:10px
    }
    .cart-container{
        height: fit-content;
        grid-template-columns: repeat(12,1fr);
        grid-template-rows: repeat(4,1fr);
        min-width: 525px;
    }
    .cart-container button:hover{
        box-shadow: 0 4px 15px #d4d5d9;
        transition:all 0.3s ease;
    }

    /* account container */
    .account-container{
        grid-area: a;
        grid-template-areas: 
        'h h h h h h h h i i i i'
        'p p p p p p p p i i i i'
        'l l l l s s s s i i i i'
        'l l l l s s s s i i i i';
    }
    .account-container h1{
        grid-area: h;
        font-size: 32px;
    }
    .account-container p{
        grid-area: p;
        font-size: 14px;
        color:#7e808c;
    }
    .account-btn{
        max-height: 65px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        outline:0;
        max-width: 170px;
        border:0;
    }
    .account-btn span:first-child{
        font-size: 13px;
    }
    .account-btn span:last-child{
        font-size: 16px;
        font-weight: 600;
        text-transform: uppercase;
    }
    .account-login{
        grid-area: l;
        background-color: #fff;
        border:1px solid #60b246;
    }
    .account-login span:first-child,
    .account-login span:last-child{
        color:#60b246;
    }
    .account-signup{
        grid-area: s;
        background-color: #60b246;
    }
    .account-signup span:first-child,
    .account-signup span:last-child{
        color:#fff;
    }
    .account-img-container{
        grid-area: i;
        display: flex;
        align-items: center;
        justify-content: center;
    }


    /* delivery container */
    .delivery-container{
        grid-area: d;
    }
    .delivery-container h1{
        font-size: 32px;
        font-weight: 600;
        grid-column: 1/-1;
        grid-row: 1/-1;
    }
    .delivery-address-container{
        grid-column: 1/8;
        grid-row: 2/5;
        display: flex;
        align-items: flex-start;
        justify-content: center;
        flex-direction: column;
        width: 100%;
        height: 100%;
    }
    .delivery-img-container{
        grid-column: 8/13;
        grid-row: 1/5;
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .delivery-img-container img{
        width: 175px;
        object-fit: contain;
        object-position: center;
    }

    /* payment container */
    .payment-container{
        grid-area: p;
    }
    .payment-container h1{
        grid-column: 1/-1;
        grid-row: 1/3;
        font-size: 32px;
        font-weight: 600;
    }
    .payment-container button{
        height: 65px;
        outline:0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap:5px;
    }
    .payment-container button span:first-child{
        font-size: 12px;
    }
    .payment-container button span:last-child{
        font-size: 16px;
        font-weight: 600;
        text-transform: uppercase;
    }
    .cc-btn{
        grid-column: 1/5;
        grid-row: 3/5;
        background-color: #fff;
        border:1px solid #60b246;
        color:#60b246;
    }
    .cc-btn span:first-child{
        color:#60b246;
    }
    .cc-btn span:last-child{
        color:#60b246;
    }
    .paypal-btn{
        grid-column: 5/9;
        grid-row: 3/5;
        background-color: #60b246;
        border:0;
    }
    .paypal-btn span:first-child{
        color:#fff;
    }
    .paypal-btn span:last-child{
        color:#fff;
    }
    .payment-container img{
        grid-column: 9/13;
        grid-row: 1/-1;
        align-self: center;
        justify-self: center;
        width: 125px;
    }

    /* order container */
    .order-container{
        grid-area: o;
        min-width: 300px;
        display: grid;
        grid-template-rows: 15% auto auto;
        grid-template-columns: 1fr;
    }
    .restaurant-wrapper{
        width: 100%;
        height: 100%;
        display: grid;
        grid-template-columns: repeat(12,1fr);
        grid-template-rows: repeat(6,1fr);
    }
    .restaurant-wrapper img{
        grid-column: 1/4;
        grid-row: 1/-1;
        width: 50px;
        align-self: center;
        justify-self: center;
    }
    .restaurant-wrapper h1{
        grid-column: 4/-1;
        grid-row: 2/4;
        font-size: 17px;
        font-weight: 600;
        overflow: hidden;
    }
    .restaurant-wrapper p{
        grid-column: 4/-1;
        grid-row: 4/5;
        font-size: 13px;
        color:#7e808c;
    }
    .order-item-container{
        overflow: scroll;
        height: 250px;
        padding:5px;
        display: grid;
        grid-template-columns: 1fr;
        grid-auto-rows: 50px;
    }
    .order-item{
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .order-item span:first-child{
        font-size: 14px;
        font-weight: 600;
        width: 130px;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: start;
        flex-wrap: wrap;
    }
    .order-btn-container{
        display: grid;
        grid-template-columns: repeat(3,1fr);
        grid-auto-rows: 25px;
        width: 70px;
        align-items: center;
        justify-items: center;
        border:1px solid #60b246;
    }
    .order-btn-container button{
        width: 100%;
        background-color: #fff;
        outline:0;
        border:0;
        color:#60b246;
        font-size: 16px;
        font-weight: 600;
    }
    .order-quantity{
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 12px;
        color:#60b246;
    }
    .order-cost{
        font-size: 13px;
        color:#7e808c;
    }

    .order-totals-container{
        width: 100%;
        height: fit-content;
        display: flex;
        flex-direction: column;
    }
    .order-totals-container h2{
        font-size: 16px;
    }
    .totals-row{
        display: flex;
        align-items: center;
        justify-content: space-between;
        height: 35px;
        margin:3px 0;
    }
    .totals-row p{
        font-size: 13px;
        color:#7e808c;
    }
    .totals-row:nth-child(3){
        border-bottom: 1px solid #7e808c;
    }
    .totals-row:last-child{
        border-top: 2px solid #000;
        padding-top: 20px;
    }
    .totals-row:last-child p{
        font-size: 15px;
        font-weight: 600;
        text-transform: uppercase;
        color:#000;
    }


    /* payment modal */
    .payment-modal{
        width: 100vw;
        height: 100vh;
        position:absolute;
        z-index: 5;
        top:0;
        left:0;
        right:0;
        bottom:0;
        background-color: rgba(0, 0, 0, 0.5);
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .pay-container{
        background-color: #fff;
        width: 325px;
        height: fit-content;
        padding:20px;
        border-radius: 5px;
        position: relative;
        display: flex;
        flex-direction: column;
        gap:25px;
    }
    .close-payment-btn{
        position: absolute;
        top: 20px;
        right:20px;
        background-color: #fff;
        outline:0;
        border:0;
        font-size: 16px;
        font-weight: 600;
    }
    .checkout-header{
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .checkout-header h1{
        font-size: 18px;
    }
    .checkout-header h2{
        margin-right: 50px;
        font-size: 18px;
        color:orange;
    }
    .checkout-body{
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    .checkout-body h3{
        font-size: 14px;
        font-weight: 400;
    }
    form{
        border:1px solid orange;
        padding:20px;
        border-radius: 5px;
        display: flex;
        flex-direction: column;
        gap:15px;
    }
    .form-row{
        display: flex;
        align-items: center;
    }
    .form-field{
        display: flex;
        flex-direction: column;
        width: 100%;
        gap:5px;
        height: 100%;
    }
    .form-field label{
        font-size: 11px;
        color: #7e808c;
    }
    .form-field input{
        line-height: 30px;
        font-size: 18px;
        outline:none;
        border:1px solid orange;
        padding:5px;
        border-radius: 5px;
    }
    .form-row:nth-child(3){
        justify-content: center;
        gap: 25px;
    }
    .form-row:nth-child(3) .form-field:first-child{
        width: 50%;
    }
    .form-row:nth-child(3) .form-field:last-child{
        width: 25%;
    }
    .payment-btn{
        height: 45px;
        background-color: orange;
        color: #fff;
        font-size: 20px;
        font-weight: 600;
        outline:none;
        border:none;
        border-radius: 5px;
    }

    /* payment confirmation */
    .payment-confirmation{
        display: grid;
        grid-template-columns: 1fr;
        grid-template-rows: 35px 35px auto;
        height: fit-content;
        width: 350px;
        background-color: #fff;
        padding:25px;
        border-radius: 5px;
        gap:15px;
    }
    .payment-confirmation h1{
        font-size: 18px;
        font-weight: 600;
        text-align: center;
    }
    .payment-confirmation p{
        font-size: 13px;
        color:#535665;
        text-align: center;
    }
    .payment-confirmation svg{
        width: 100%;
        height: 100px;
    }


    @media (max-width:920px) {
        .cart-fill-container{
            grid-template-areas: 
            'o o o o o o o o o o o o'
            'o o o o o o o o o o o o'
            'o o o o o o o o o o o o'
            'a a a a a a a a a a a a'
            'a a a a a a a a a a a a'
            'a a a a a a a a a a a a'
            'd d d d d d d d d d d d'
            'd d d d d d d d d d d d'
            'd d d d d d d d d d d d'
            'p p p p p p p p p p p p'
            'p p p p p p p p p p p p'
            'p p p p p p p p p p p p';
        }
        .restaurant-wrapper img{
            grid-column: 1/2;
            justify-self: start;
            margin-right: 15px;
        }
        .restaurant-wrapper h1{
            grid-column: 2/-1;
        }
        .restaurant-wrapper p{
            grid-column: 2/-1;
        }
        .order-item span:first-child{
            width: 70%;
        }
        .order-btn-container{
            width: 85px;
            grid-auto-rows: 30px;
        }
    }

    @media (max-width:570px) {
        .cart-container{
            min-width: 100%;
        }
        .cart-container img{
            display: none;
        }
        .order-container{
            min-width: 100%;
        }
        .account-container{
            grid-template-areas: 
                'h h h h h h h h h h h h'
                'p p p p p p p p p p p p'
                'l l l l l l s s s s s s'
                'l l l l l l s s s s s s';
        }
        .cart-container h1{
            font-size: 24px;
        }   
        .delivery-address-container{
            height: 100px;
        }
        .paypal-btn{
            grid-column: 7/13;
        }
        .cc-btn{
            grid-column: 1/7;
        }



        .order-item span:first-child{
            width: fit-content;
        }

    }



</style>