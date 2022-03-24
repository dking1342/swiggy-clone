import { ref } from "vue";


// types
export interface State {
    state:{
        location:string
    }
}

// initial state
const state = () => ref<State>({
    state:{
        location:''
    }
});

// actions
const actions = {
    setLocationAction:({commit}:any,userInput:string) => commit('setLocationMutation',userInput),
    removeLocationAction:({commit}:any) => commit('removeLocationMutation'),
}

// mutations
const mutations = {
    setLocationMutation:(state:State,userInput:string) => {
        if(localStorage.getItem('location') && userInput || userInput){
            // setting location from user
            state.state.location = userInput;
            localStorage.setItem('location',JSON.stringify(state.state.location));
        } else {
            // setting location from local storage
            state.state.location = JSON.parse(localStorage.getItem('location')!);
        }
    },
    removeLocationMutation:(state:State) => {
        state.state.location = "";
        localStorage.removeItem('location');
    }
}

export default {
    namespaced:true,
    state,
    mutations,
    actions,
}