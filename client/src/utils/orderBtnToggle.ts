import { Order } from "../types/fetch-types";


const addOrder = (id:string,state:Order) => {
    const index = state.order_item.findIndex(x=>x.order_item_name.menu_id === id);
    const quantity = state.order_item[index].order_item_quantity + 1;
    state.order_item[index].order_item_quantity = quantity;
    state.cart_quantity = state.order_item.reduce((acc,val)=>acc + val.order_item_quantity,0);
    state.cart_cost = state.order_item.reduce((acc,val)=>acc + (val.order_item_quantity * val.order_item_name.menu_price),0);
    localStorage.setItem('cart',JSON.stringify(state));            
}

const decreaseOrder = (id:string,state:Order,isCartFilled:boolean) => {
    const index = state.order_item.findIndex(x=>x.order_item_name.menu_id === id);
    const quantity = state.order_item[index].order_item_quantity - 1;
    if(!quantity){
        state.order_item = state.order_item.filter(x=>x.order_item_name.menu_id !== id);
    } else {
        state.order_item[index].order_item_quantity = quantity;
    }
    state.cart_quantity = state.order_item.reduce((acc,val)=>acc + val.order_item_quantity,0);
    state.cart_cost = state.order_item.reduce((acc,val)=>acc + (val.order_item_quantity * val.order_item_name.menu_price),0);

    if(!state.order_item.length){
        localStorage.removeItem('cart');
        state = {} as Order;
        isCartFilled = false;
    } else {
        localStorage.setItem('cart',JSON.stringify(state));
    }

}

export {
    addOrder,
    decreaseOrder
}
