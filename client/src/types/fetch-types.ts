
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
    status_code:number,
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
    restaurant_created?:Date | string
}

export interface Discount {
    discount_id:string,
    discount_code:string,
    discount_text:string,
    discount_amount:number,
    discount_created?:Date | string
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
    menu_orderQuantity?:number
}

export interface OrderItem {
    order_item_id:string,
    order_item_name:Menu,
    order_item_quantity:number,
    order_reference:string,
    order_restaurant:string | null
}

export interface OrderConfirmationItem {
    order_item_id:string,
    order_item_name:string,
    order_item_price:number,
    order_item_quantity:number,
    order_item_cost:number,
    order_reference:string,
    order_restaurant:string,
}

export interface Order {
    order_id:string,
    order_item:OrderItem[],
    cart_quantity:number,
    cart_cost:number
}

export interface OrderReceipt {
    number:string,
    customer:string,
    expiry:string,
    cvv:string,
}

export interface Rating {
    rating_id:string,
    rating_rate:number,
    rating_order_reference:string,
    rating_restaurant:string
}

export interface UserInfo {
    user_id:string,
    user_name:string,
    user_phone:string,
    user_email:string,
    token?:string,
}

