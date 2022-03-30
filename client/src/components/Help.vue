<template>
    <div class="header-filler"></div>
    <header class="header sticky">
        <h1>Help & Support</h1>
        <h2>Let's take a step ahead and help you better</h2>
    </header>
    <section id="section">
        <article>
            <nav>
                <button @click="handleTitleTextChange">Partner Onboarding</button>
                <button @click="handleTitleTextChange">Legal</button>
                <button @click="handleTitleTextChange">FAQs</button>
            </nav>
            <HelpList 
                :titleText="titleText"
                :helpList="helpList"
            />
        </article>
    </section>
</template>

<script lang="ts">
import { HELPOPTIONS } from '@/types/fetch-types';
import { defineComponent, ref } from 'vue';
import HelpList from './HelpList.vue';

interface List {
    header:string,
    text:string,
}

export default defineComponent({
    components:{
        HelpList
    },
    setup () {
        let titleText = ref<HELPOPTIONS.partner | HELPOPTIONS.legal | HELPOPTIONS.faqs>(HELPOPTIONS.partner);
        const partnerOnboardingList = ref<List[]>([{
                header:"After I submit all documents, how long will it take for my restaurant to go live on Swiggy?",
                text:"After all mandatory documents have been received and verified it takes upto 7-10 working days for the onboarding to be completed and make your restaurant live on the platform."
            },{
                header:"What is this one time Onboarding fees? Do I have to pay for it while registering?",
                text:"This is a one-time fee charged towards the system & admin costs incurred during the onboarding process. It is deducted from the weekly payouts after you start receiving orders from Swiggy."
            },{
                header:"How much commission will I be charged by Swiggy?",
                text:"The commission charges vary for different cities. You will be able to see the commission applicable for you once the preliminary onboarding details have been filled."
            },{
                header:"I don’t have an FSSAI licence for my restaurant. Can it still be onboarded?",
                text:"FSSAI licence is a mandatory requirement according to the government’s policies. However, if you are yet to receive the licence at the time of onboarding, you can proceed with the acknowledgement number which you will have received from FSSAI for your registration."
            }
        ]);
        const legalList = ref<List[]>([{
            header:"Terms of Use",
            text:"These terms of use (the \"Terms of Use\") govern your use of our website www.swiggy.in (the \"Website\") and our \"Swiggy\" application for mobile and handheld devices (the \"App\"). The Website and the App are jointly referred to as the \"Services\"). Please read these Terms of Use carefully before you download, install or use the Services. If you do not agree to these Terms of Use, you may not install, download or use the Services. By installing, downloading or using the Services, you signify your acceptance to the Terms of Use and Privacy Policy (being hereby incorporated by reference herein) which takes effect on the date on which you download, install or use the Services, and create a legally binding arrangement to abide by the same."
        },{
            header:"Privacy Policy",
            text:"We ( Bundl Technologies Private Limited, alias \"Swiggy\" ) are fully committed to respecting your privacy and shall ensure that your personal information is safe with us. This privacy policy sets out the information practices of www.swiggy.com (\"Website\") including the type of information is collected, how the information is collected, how the information is used and with whom it is shared. Reference to \"you\" in this Privacy Policy refers to the users of this Website whether or not you access the services available on the Website or consummate a transaction on the Website. By using or accessing this Website, you agree to the terms and conditions of this Privacy Policy. You also expressly consent to our use and disclosure of your Personal Information (as defined below) in any manner as described in this Privacy Policy and further signify your agreement to this Privacy Policy and the Terms of Use (being incorporated by reference herein). If you do not agree with the terms and conditions of this Privacy Policy, please do not proceed further or use or access this Website. "
        },{
            header:"Cancellations and Refunds",
            text:"a) As a general rule you shall not be entitled to cancel your order once placed. You may choose to cancel your order only within one-minute of the order being placed by you. However, subject to your previous cancellation history, Swiggy reserves the right to deny any refund to you pursuant to a cancellation initiated by you even if the same is within one-minute.  b)If you cancel your order after one minute of placing it, Swiggy shall have a right to charge you 100% of the order amount as the cancellation fee , with a right to either not to refund the order value in case your order is prepaid or recover from your subsequent order in case your order is postpaid, to compensate our restaurant/merchants and delivery partners. c)Swiggy reserves the right to charge you cancellation fee for the orders constrained to be cancelled by Swiggy for reasons not attributable to Swiggy, including but not limited to: i)in the event if the address provided by you is either wrong or falls outside the delivery zone; ii) failure to contact you by phone or email at the time of delivering the order booking; iii) failure to deliver your order due to lack of information, direction or authorization from you at the time of delivery; or iv) unavailability of all the items ordered by you at the time of booking the order. However, in the unlikely event of an item on your order being unavailable, Swiggy will contact you on the phone number provided to us at the time of placing the order and inform you of such unavailability. In such an event you will be entitled to cancel the entire order and shall be entitled to a refund to an amount upto 100% of the order value. d)In case of cancellations for the reasons attributable to Swiggy or the restaurant partner or delivery partners, Swiggy shall not charge you any cancellation fee."
        },{
            header:"Terms of Use for Swiggy ON-TIME / Assured",
            text:"These terms of use (the \"Terms of Use\") that govern your use of our service Swiggy ON-TIME / Assured  (\"ON-TIME\" / \"Assured\") on our website www.swiggy.in (the \"Website\") and our Swiggy application for mobile and handheld devices (the \"App\"). The services on ON-TIME / Assured  available on our Website and the App are jointly referred to as the \"On-Time Delivery\". Please read these Terms of Use carefully before you use the Services. If you do not agree to these Terms of Use, you may not use the Services. By using the Services, you signify your acceptance to the Terms of Use and Privacy Policy (incorporated by reference herein) and creates a legally binding arrangement to abide by the same. "
        }]);
        const faqsList = ref<List[]>([{
            header:"What is Swiggy Customer Care Number?",
            text:"We value our customer’s time and hence moved away from a single customer care number to a comprehensive chat-based support system for quick and easy resolution. You no longer have to go through the maze of an IVRS call support. Just search for your issue in the help section on this page and initiate a chat with us. A customer care executive will be assigned to you shortly. You can also email us your issue on support@swiggy.in \n Note: We value your privacy and your information is safe with us. Please do not reveal any personal information, bank account number, OTP etc. to another person. A Swiggy representative will never ask you for these details. Please do not reveal these details to fraudsters and imposters claiming to be calling on our behalf. Be vigilant and do not entertain phishing calls or emails."
        },{
            header:"Can I edit my order?",
            text:"Your order can be edited before it reaches the restaurant. You could contact customer support team via chat or call to do so. Once order is placed and restaurant starts preparing your food, you may not edit its contents"
        },{
            header:"I want to cancel my order",
            text:"We will do our best to accommodate your request if the order is not placed to the restaurant (Customer service number:  080-67466729). Please note that we will have a right to charge a cancellation fee up to full order value to compensate our restaurant and delivery partners if your order has been confirmed."
        },{
            header:"Will Swiggy be accountable for quality/quantity?",
            text:"Quantity and quality of the food is the restaurants' responsibility. However in case of issues with the quality or quantity, kindly submit your feedback and we will pass it on to the restaurant."
        },{
            header:"Is there a minimum order value?",
            text:"We have no minimum order value and you can order for any amount. "
        },{
            header:"Do you charge for delivery?",
            text:"Delivery fee varies from city to city and is applicable if order value is below a certain amount. Additionally, certain restaurants might have fixed delivery fees. Delivery fee (if any) is specified on the 'Review Order' page. "
        },{
            header:"How long do you take to deliver?",
            text:"Standard delivery times vary by the location selected and prevailing conditions. Once you select your location, an estimated delivery time is mentioned for each restaurant."
        },{
            header:"What are your delivery hours?",
            text:"Our delivery hours vary for different locations and depends on availability of supply from restaurant partners."
        },{
            header:"Can I order from any location?",
            text:"We will deliver from any restaurant listed on the search results for your location. We recommend enabling your GPS location finder and letting the app auto-detect your location."
        },{
            header:"Is single order from many restaurants possible?",
            text:"We currently do not support this functionality. However, you can place orders for individual items from different restaurants."
        },{
            header:"Do you support bulk orders?",
            text:"In order to provide all customers with a great selection and to ensure on time delivery of your meal, we reserve the right to limit the quantities depending on supply."
        },{
            header:"Can I order in advance?",
            text:"We currently do not support this functionality. All our orders are placed and executed on-demand."
        },{
            header:"Can I change the address / number?",
            text:"Any major change in delivery address is not possible after you have placed an order with us. However, slight modifications like changing the flat number, street name, landmark etc. are allowed. If you have received delivery executive details, you can directly call him, else you could contact our customer service team."
        },{
            header:"Did not receive OTP?",
            text:"Please check if your app is due for an update. If not, please share the details via support@swiggy.in"
        },{
            header:"Did not receive referral coupon?",
            text:"Referral coupon is given upon the first successful transaction of the referred person. If you still have not received it, kindly send us your details at support@swiggy.in. We will contact you within 48 hours."
        },{
            header:"Deactivate my account",
            text:"Please write to us at support@swiggy.in in the event that you want to deactivate your account."
        },{
            header:"Unable to view the details in my profile",
            text:"Please check if your app is due for an update. If not, please share the details via support@swiggy.in"
        },{
            header:"What is Swiggy Money?",
            text:"Swiggy Money is a secure digital wallet where you can store digital currency and use it for faster check outs. It prevents payment failures and gives you seamless refunds when necessary."
        },{
            header:"Do you accept Sodexo, Ticket Restaurant etc.?",
            text:"We do not accept Sodexo vouchers but we do accept Sodexo card. You can select the Sodexo card option while selecting payment options at the time of order"
        }]);
        let helpList = ref<List[]>(partnerOnboardingList.value);

        // components functions/methods
        const handleTitleTextChange = (e:any) => {
            let userChoice = e.target.textContent;
            switch (userChoice) {
                case HELPOPTIONS.partner:
                    titleText.value = HELPOPTIONS.partner;
                    helpList.value = partnerOnboardingList.value;
                    break;
                case HELPOPTIONS.legal:
                    titleText.value = HELPOPTIONS.legal;
                    helpList.value = legalList.value;
                    break;
                case HELPOPTIONS.faqs:
                    titleText.value = HELPOPTIONS.faqs;
                    helpList.value = faqsList.value;
                    break;            
                default:
                    break;
            }
            window.scrollTo({behavior:"smooth",top:0})
        }


        return {
            titleText,
            handleTitleTextChange,
            helpList,
            scrollY
        }
    }
})
</script>

<style>
    #section{
        height: 100%;
        width: 100vw;
        margin:0 -5.5%;
        padding: 0 5% 40px 5%;
        background-color: #37718e;
    }
    .header-filler{
        height: 100px;
        background-color: #37718e;
        margin:0 -5.5%;
    }
    .header{
        position:-webkit-sticky;
        position:sticky;
        top:0px;
        z-index: 5;
    }
    .sticky{
        padding:20px 5%;
        margin:0 -5.5%;
        background-color: #37718e;
    }
    .sticky h1{
        font-size: 28px;
        color:#fff;
    }
    .sticky h2{
        font-size: 16px;
        font-weight: 400;
        color:#fff;
        margin-top: 5px;
    }
    article{
        background-color: #fff;
        padding:15px;
        height: 100%;
    }
    nav{
        display: flex;
        gap:10px;
        height: 60px;
        position:sticky;
        top:105px;
        background-color: #fff;
    }
    nav button{
        background-color: transparent;
        border:0;
        outline:0;
        display: flex;
        align-items: center;
        font-size: 14px;
        font-weight: 600;
        transition: 250ms ease color;
    }
    nav button:hover{
        color:orange;
        transition:250ms ease color;
    }
    nav button:focus{
        color:orange;
    }


</style>