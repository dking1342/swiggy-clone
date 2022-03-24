import { createLogger, createStore } from 'vuex';
import user from './modules/user';
import cart from './modules/cart';
import location from './modules/location';

const debug = process.env.NODE_ENV !== 'production';

export default createStore({
    modules:{
        user,
        cart,
        location,
    },
    strict:debug,
    plugins: debug ? [createLogger()] : []
})