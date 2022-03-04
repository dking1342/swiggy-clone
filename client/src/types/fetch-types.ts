
export enum DATASTATE {
    loading = "LOADING",
    error = "ERROR",
    success = "SUCCESS"
}


export interface ResponseAppState<T> {
    dataState:DATASTATE,
    appData?:T,
    error:string    
}

export interface FetchResponse<T> {
    timestamp:Date,
    status:string,
    status_code:string,
    message:string,
    data:[T]
}

export interface Restaurant<T> {
    restaurant_id:string,
    restaurant_name:string,
    restaurant_address_1:string,
    restaurant_address_2:string,
    restaurant_city:string,
    restaurant_zip_code:string,
    restaurant_state:string,
    restaurant_cuisines:string[],
    restaurant_main_img:string,
    discount_isValid:boolean,
    discounts:T,
    restaurant_cost:number,
    restaurant_rating:number,
    restaurant_created:Date
}

export interface Discount {
    discount_id:string,
    discount_code:string,
    discount_text:string,
    discount_amount:number,
    discount_created:Date
}



export const placeholderFetch:ResponseAppState<FetchResponse<Restaurant<Discount>>> = {
    dataState:DATASTATE.loading,
    appData:{
        timestamp:new Date(),
        status:"",
        status_code:"",
        message:"",
        data:[{
            restaurant_id:"",
            restaurant_name:"",
            restaurant_address_1:"",
            restaurant_address_2:"",
            restaurant_city:"",
            restaurant_zip_code:"",
            restaurant_state:"",
            restaurant_cuisines:[""],
            restaurant_main_img:"",
            discount_isValid:false,
            discounts:{
                discount_id:"",
                discount_code:"",
                discount_text:"",
                discount_amount:0,
                discount_created:new Date()
            },
            restaurant_cost:0,
            restaurant_rating:0.0,
            restaurant_created:new Date()
        }]
    },
    error:""
}

