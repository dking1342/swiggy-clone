<template>
    <footer>
        <div class="footer-row row-1">
            <FooterList :payload="companyList" />
            <FooterList :payload="contactList" />
            <FooterList :payload="legalList" />
            <div class="footer-col top-col-1">
                <img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_200,h_65/icon-AppStore_lg30tv" alt="apple store image">
                <img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_200,h_65/icon-GooglePlay_1_zixjxl" alt="android store image">
            </div>
        </div>
        <div class="footer-row row-2">
            <img class="logo-img" src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_284/Logo_f5xzza" alt="swiggy logo">
            <p>&copy; 2022 Swiggy</p>
            <div class="social-btns" >
                <button v-for="btn in socialBtns" :key="btn.src"><img :src="btn.src" :alt="btn.alt"></button>
            </div>
        </div>
    </footer>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import FooterList from './FooterList.vue';

export default defineComponent({
    components:{
        FooterList,
    },
    setup () {
        let companyList = ref({
            title:"Company",
            list:[
                {link:"About Us"},
                {link:"Team"},
                {link:"Careers"},
                {link:"Swiggy Blog"},
                {link:"Bug Bounty"},
                {link:"Swiggy One"},
                {link:"Swiggy Corporate"},
                {link:"Swiggy Instamart"}
            ]
        })
        let contactList = ref({
            title:"Contact",
            list:[
                {link:"Help & Support"},
                {link:"Parnter with us"},
                {link:"Ride with us"}
            ]
        })
        let legalList = ref({
            title:"Legal",
            list:[
                {link:"Terms & Conditions"},
                {link:"Refund & Cancellation"},
                {link:"Privacy Policy"},
                {link:"Cookie Policy"},
                {link:"Offer Team"},
                {link:"Phishing & Fraud"}
            ]
        })
        let socialBtns = ref([
            {src:"https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_48,h_48/icon-facebook_tfqsuc",alt:"facebook logo"},
            {src:"https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_48,h_48/icon-pinterest_kmz2wd",alt:"pinterest logo"},
            {src:"https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_48,h_48/icon-instagram_b7nubh",alt:"instagram logo"},
            {src:"https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_48,h_48/icon-twitter_gtq8dv",alt:"twitter logo"}
        ])


        return {
            companyList,
            contactList,
            legalList,
            socialBtns
        }
    }
})
</script>

<style scoped>
    footer{
        background-color: #282c3f;
        display: flex;
        flex-direction: column;
        padding:40px 60px;
        gap:40px;
    }
    .footer-row{
        display: grid;
        grid-template-columns: repeat(auto-fit,minmax(200px,1fr));
        grid-auto-rows: auto;
        gap:20px;
    }
    .row-2{
        align-items: center;
        gap:40px;
    }
    .logo-img{
        width: 175px;
    }
    .row-2 p{
        font-size: 20px;
        color:#fff;
    }
    .social-btns{
        display: grid;
        grid-template-columns: repeat(4,60px);
        grid-template-rows: 60px;
        gap:10px;
    }
    .social-btns button{
        width: 60px;
        height: 60px;
        outline:0;
        border:0;
        background-color: transparent;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .social-btns img{
        width: 50%;
        pointer-events: none;
    }
</style>