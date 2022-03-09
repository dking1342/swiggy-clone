
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
    timestamp:Date | string,
    status:string,
    status_code:string,
    message:string,
    data:T[]
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
    restaurant_created:Date | string
}

export interface Discount {
    discount_id:string,
    discount_code:string,
    discount_text:string,
    discount_amount:number,
    discount_created:Date | string
}

export interface Cuisine {
    cuisine_id:string,
    cuisine_name:string
}

export interface Menu {
    menu_id:string,
    menu_category:string,
    menu_item:string,
    menu_description:string,
    menu_price:number,
    menu_image:string,
    menu_hasOffer:boolean,
    menu_offer:Discount,
    menu_isBestseller:boolean,
    restaurant:Restaurant<Discount>,
    menu_created:Date | string,
    menu_orderQuantity:number
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

export const placeholderCuisineFetch:ResponseAppState<FetchResponse<Cuisine>> = {
    dataState:DATASTATE.loading,
    appData:{
        timestamp:new Date(),
        status:"",
        status_code:"",
        message:"",
        data:[{
            cuisine_id:"",
            cuisine_name:""
        }]
    },
    error:""
}

export const placeholderMenu:Menu[] = [
    {
        menu_id:"",
        menu_category:"",
        menu_item:"",
        menu_description:"",
        menu_price:0,
        menu_image:"",
        menu_hasOffer:false,
        menu_offer:{
            discount_id:"",
            discount_amount:0,
            discount_code:"",
            discount_text:"",
            discount_created:new Date()
        },
        menu_isBestseller:false,
        restaurant:{
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
        },
        menu_created:new Date(),
        menu_orderQuantity:0
    }
]

export const placeholderFetchMenu:FetchResponse<Menu> = {
    timestamp:new Date(),
    status:"",
    status_code:"",
    message:"",
    data:placeholderMenu
}

export const placeholderRestaurant:Restaurant<Discount>[] = [{
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

export const placeholderMenuFetch:ResponseAppState<FetchResponse<Menu>> = {
    dataState:DATASTATE.loading,
    appData:{
        timestamp:new Date(),
        status:"",
        status_code:"",
        message:"",
        data:placeholderMenu
    },
    error:""
}

