import { DATASTATE } from "@/types/fetch-types";
import { reactive, toRefs } from "vue"

interface State<T> {
    dataState:DATASTATE.loading | DATASTATE.success | DATASTATE.error
    errorMsg:string,
    data:T | {}
}

export const useFetch = async <T>(url:string) => {
    const state = reactive<State<T>>({
        dataState:DATASTATE.loading,
        errorMsg:'',
        data:{} as T
    });

    const fetchData = async () => {
        state.dataState = DATASTATE.loading;
        try {
            const response = await fetch(url);
            if(!response.ok){
                state.dataState = DATASTATE.error;
                state.errorMsg = response.statusText
            }
            state.dataState = DATASTATE.success;
            state.data = await response.json();
        } catch (error:unknown) {
            const typedError = error as Error;
            state.dataState = DATASTATE.error;
            state.errorMsg = typedError.message;
        } 
    }

    await fetchData();

    return {
        ...toRefs(state)
    };
}

export const useAPICall = async<T>(url:string,body:any,method:string) => {
    const state = reactive({
        dataState:DATASTATE.loading,
        errorMsg:'',
        data:{} as T
    })
    
    const fetchData = async () => {
        state.dataState = DATASTATE.loading;
        try {
            const response = await fetch(url,{
                method: `${method}`, 
                mode: 'cors', 
                cache: 'no-cache', 
                credentials: 'same-origin', 
                headers: {
                    'Content-Type': 'application/json'
                },
                redirect: 'follow',
                referrerPolicy: 'no-referrer',
                body: JSON.stringify(body)         
            });
            if(!response.ok){
                state.dataState = DATASTATE.error;
                state.errorMsg = response.statusText
            }
            state.dataState = DATASTATE.success;
            state.data = await response.json();
        } catch (error:unknown) {
            const typedError = error as Error;
            state.dataState = DATASTATE.error;
            state.errorMsg = typedError.message;
        } 
    }

    await fetchData();

    return {
        ...toRefs(state)
    }
}