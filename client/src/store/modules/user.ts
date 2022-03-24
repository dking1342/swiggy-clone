import { UserInfo } from "@/types/fetch-types"
import { ref } from "vue"

interface State {
    user:UserInfo,
    isLoggedIn:boolean
}

// initial state
const state = () => ref({
    user:{
        user_email: "",
        user_id: "",
        user_name: "",
        user_phone: ""    
    },
    isLoggedIn:false
});

// getters


// actions
const actions = {
    setUserInfoAction:({commit}:any,payload:UserInfo) => commit('setUserInfoMutation',payload),
    resetUserInfoAction:({commit}:any) => commit('resetUserInfoMutation'),
}

// mutations
const mutations = {
    setUserInfoMutation:(state:State,payload:UserInfo)=>{
        state.user = {
            ...state.user,
            user_email: payload.user_email,
            user_id: payload.user_id,
            user_name: payload.user_name,
            user_phone: payload.user_phone  
        };
        state.isLoggedIn = true;
        localStorage.setItem('user',JSON.stringify(payload));
    },
    resetUserInfoMutation:(state:State)=> {
        state.user = {
            user_email: "",
            user_id: "",
            user_name: "",
            user_phone: "" 
        };
        state.isLoggedIn = false;
        localStorage.removeItem('user');
    }
}



export default {
    namespaced: true,
    state,
    mutations,
    actions,
}