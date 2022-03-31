<template>
    <div class="content-body">
        <h1>{{ titleText }}</h1>
        <div class="content-row" v-for="partner in helpList" :key="partner.header">
            <div class="content-btn-container">
                <button class="content-btn" @click="handleTextShow">{{ partner.header }}</button><span>⌄</span>
            </div>
            <div class="content-text">
                <p>{{ partner.text }}</p>
            </div>
        </div>
    </div>

</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    props:{
        titleText:String,
        helpList:Object,
    },
    setup () {

        const handleTextShow = (e:any) => {
            let siblingElement = e.target.parentElement.nextSibling as HTMLElement;
            let siblingHeight = getComputedStyle(siblingElement).maxHeight;
            let parentElement = e.target.parentElement.parentElement as HTMLElement;

            if(siblingHeight === "0px"){
                siblingElement.style.maxHeight="500px";
                parentElement.style.paddingBottom="15px";
            } else {
                siblingElement.style.maxHeight="0px";
                parentElement.style.paddingBottom="0px";
            }
        }
        

        return {
            handleTextShow
        }
    }
})
</script>

<style scoped>
    .content-body{
        margin-top:25px;
    }
    .content-body h1{
        font-size: 24px;
        margin-bottom: 24px;
    }
    .content-row{
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap:10px;
        border-bottom: 1px solid #37718e;
        margin-bottom: 15px;
        transition:500ms ease all;
    }
    .content-btn-container{
        display: flex;
        align-content: center;
        justify-content: space-between;
        width: 100%;
        padding:0 50px 0 0;
    }
    .content-btn{
        width: 100%;
        border:0;
        outline:0;
        text-align: left;
        background:transparent;
        font-size: 16px;
        padding:0 50px 0 0;
        color:inherit;
        transition:all ease 250ms;
    }
    .content-btn:hover{
        color:orange;
        transition:ease all 250ms;
    }
    .content-text{
        padding:10px 50px 0 0;
        text-align: justify;
        font-size: 12px;
        color:#999;
        max-height: 0;
        overflow: hidden;
        transition:ease 500ms all;
    }
</style>