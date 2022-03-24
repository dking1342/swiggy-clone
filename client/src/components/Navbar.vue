<template>
  <nav>
    <div class="left-nav">
      <router-link to="/">
        <svg class="_8pSp-" viewBox="0 0 559 825" height="49" width="34" fill="#fc8019"><path fill-rule="evenodd" clip-rule="evenodd" d="M542.92 388.542C546.805 366.526 542.355 349.598 530.881 340.76C513.621 327.466 487.698 320.236 425.954 320.236C380.271 320.236 331.225 320.286 310.268 320.275C308.322 319.894 301.285 317.604 301.02 309.112L300.734 174.289C300.727 165.779 307.531 158.857 315.943 158.839C324.369 158.825 331.204 165.723 331.211 174.226C331.211 174.226 331.421 247.414 331.441 273.424C331.441 275.936 332.892 281.8 338.549 283.328C375.43 293.267 561.865 285.999 558.967 251.804C543.147 109.96 424.476 0 280.394 0C235.021 0 192.065 10.9162 154.026 30.2754C62.9934 77.5955 -1.65904 173.107 0.0324268 283.43C1.23215 361.622 52.2203 500.605 83.434 521.234C97.8202 530.749 116.765 527.228 201.484 527.228C239.903 527.228 275.679 527.355 293.26 527.436C295.087 527.782 304.671 530.001 304.671 538.907L304.894 641.393C304.915 649.907 298.104 656.826 289.678 656.829C281.266 656.843 274.434 649.953 274.42 641.446C274.42 641.446 275.17 600.322 275.17 584.985C275.17 581.435 275.424 575.339 265.178 570.727C231.432 555.553 121.849 564.712 115.701 581.457C113.347 587.899 125.599 612.801 144.459 644.731C170.102 685.624 211.889 747.245 245.601 792.625C261.047 813.417 268.77 823.813 280.467 824.101C292.165 824.389 300.514 814.236 317.213 793.928C383.012 713.909 516.552 537.663 542.92 388.542Z" fill="url(#paint0_linear_19447_66107)"></path><defs><linearGradient id="paint0_linear_19447_66107" x1="445.629" y1="63.8626" x2="160.773" y2="537.598" gradientUnits="userSpaceOnUse"><stop stop-color="#FF993A"></stop><stop offset="1" stop-color="#F15700"></stop></linearGradient></defs></svg>
      </router-link>
      <div class="left-nav-location" v-if="!isNavbarElementShowing">
        <p v-if="userLocation">{{ userLocation }}</p>
        <p v-if="!userLocation" class="no-location">location {{ userLocation }}</p>
        <button class="toggle-location-btn nav-header-btn" @click="toggleLocationView"><img src="https://www.svgrepo.com/show/124304/three-dots.svg" alt="more button icon"></button>
        <button class="remove-location-btn nav-header-btn" @click="clearLocation"><img src="https://img.icons8.com/external-kmg-design-detailed-outline-kmg-design/2x/external-eraser-back-to-school-kmg-design-detailed-outline-kmg-design.png" alt="delete location button icon"></button>
      </div>
      <div v-else-if="isNavbarElementShowing" class="left-nav-checkout">
        <h1>Secure Checkout</h1>
      </div>
    </div>
    <div class="right-nav">
        <router-link to="#" v-if="!isNavbarElementShowing && !isHomeView"><span data-before-content="Search" class="link-icon">🔎</span> <span class="link-text">Search</span></router-link>
        <router-link to="#" v-if="!isNavbarElementShowing"><span data-before-content="Offers" class="link-icon">%</span> <span class="link-text">Offers</span></router-link>
        <router-link to="#" ><span data-before-content="Help" class="link-icon">🙋🏻‍♂️</span> <span class="link-text">Help</span></router-link>
        <router-link to="#" v-if="!loginStatus" @click="toggleSignInView"><span data-before-content="Sign In" class="link-icon">✏️</span> <span class="link-text">Sign In</span></router-link>
        <router-link to="#" v-if="loginStatus" @click="logout"><span data-before-content="Logout" class="link-icon"></span> <span class="link-text">Logout</span></router-link>
        <router-link to="/checkout" v-if="!isNavbarElementShowing && !isHomeView" class="cart-link"><span data-before-content="Cart" class="link-icon">🧺</span> <span class="link-text">Cart</span><p v-if="cartQuantity > 0" class="cart-badge">{{ cartQuantity > 9 ? "9+" : cartQuantity }}</p></router-link>
    </div>
  </nav>
  <div class="modal-overlay" >
    <article class="login-modal modal">
      <div class="login-header modal-header">
          <button @click="toggleSignInView">X</button>
          <img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto/Image-login_btpq7r" alt="login image">
          <h1 v-if="isLogin">Login</h1>
          <h1 v-else-if="!isLogin">Register</h1>
          <p v-if="isLogin">or <button @click="isLogin = !isLogin">create an account</button></p>
          <p v-else-if="!isLogin">or <button @click="isLogin = !isLogin">login to your account</button></p>
      </div>
      <div class="login-body modal-body">
        <div class="form-section" v-if="isLogin">
          <form @submit.prevent="submitLogin" id="login-form">
            <div class="form-field" v-for="field in loginFields" :key="field.id">
              <input 
                autocomplete="off" 
                :type="field.type" 
                :maxlength="field.maxlength" 
                :name="field.name"
                :id="field.elementid"
                :pattern="field.pattern"
                @input="userInputLogin"
                @focus="focusInput" 
                @blur="blurInput"
              >
              <span>{{ field.label }}</span>
              {{ field.value }}
            </div>
            <div class="form-field form-field-submit">
              <p class="register-warning" v-if="responseLoginRef.dataState == 'ERROR'">{{ responseLoginRef.error }}</p>
              <input type="submit" value="Login">
              <p>By clicking on Login, I accept the Terms & Conditions & Privacy Policy</p>
            </div>
          </form>
        </div>
        <div class="form-section" v-else-if="!isLogin">
          <form @submit.prevent="submitRegister" id="register-form">
            <div class="form-field" v-for="field in registerFields" :key="field.id">
              <input 
                autocomplete="off" 
                :type="field.type" 
                :maxlength="field.maxlength" 
                :name="field.name" 
                :id="field.elementid" 
                :pattern="field.pattern"
                @change="userInputRegister" 
                @focus="focusInput" 
                @blur="blurInput"
              >
              <span>{{ field.label }}</span>
            </div>
            <div class="form-field form-field-submit">
              <p class="register-warning" v-if="responseRegisterRef.dataState == 'ERROR'">{{ responseRegisterRef.error }}</p>
              <input type="submit" value="Register">
              <p>By creating an account, I accept the Terms & Conditions & Privacy Policy</p>
            </div>
          </form>
        </div>
      </div>
    </article>
    <article class="location-modal modal">
      <div class="location-header modal-header">
        <button @click="toggleLocationView">X</button>
        <img src="https://www.svgrepo.com/show/49239/road-sign.svg" alt="location image">
        <h1>Location</h1>
        <p>Select a location to get started</p>
      </div>
      <div class="login-body modal-body">
        <div class="form-section modal-form">
          <form @submit.prevent="submitLocation" id="location-form">
            <div class="form-field" >
              <select name="location" id="location-select" @change="e=> selectedLocation = e.target.value">
                <option value="null" disabled selected>Select Location</option>
                <option value="Mumbai">Mumbai</option>
                <option value="Delhi">Delhi</option>
              </select>
            </div>
            <div class="form-field form-field-submit">
              <input type="submit" value="Select">
            </div>
          </form>
        </div>
      </div>

    </article>
  </div>

</template>

<script lang="ts">
import { DATASTATE, FetchResponse, ResponseAppState, UserInfo } from '@/types/fetch-types';
import { computed, defineComponent, onMounted, ref, watch } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

export default defineComponent({
    setup () {
        let showSignInModal = ref(false);
        let showLocationModal = ref(false);
        let isNavbarElementShowing = ref(false);
        let isHomeView = ref(false);
        let isLogin = ref(true);
        let loginFields = [
          {
            id:1,
            type:"tel",
            name:"phone",
            elementid:"login-phone",
            maxlength:"12",
            label:"Phone Number",
            pattern:"^[0-9]{10,12}$"
          }
        ]
        let registerFields = [
          {
            id:1,
            type:"tel",
            name:"phone",
            elementid:"register-phone",
            maxlength:"12",
            label:"Phone Number",
            pattern:"^[0-9]{10,12}$"
          },
          {
            id:2,
            type:"text",
            name:"name",
            elementid:"register-name",
            maxlength:"20",
            label:"Name",
            // eslint-disable-next-line no-useless-escape
            pattern:"[a-zA-Z].*"
          },
          {
            id:3,
            type:"email",
            name:"email",
            elementid:"register-email",
            maxlength:"40",
            label:"Email",
            // eslint-disable-next-line no-useless-escape
            pattern:".*"
          },
          {
            id:4,
            type:"password",
            name:"password",
            elementid:"register-password",
            maxlength:"30",
            label:"Password",
            // eslint-disable-next-line no-useless-escape
            pattern:".*"
          }
        ]
        let loginValues = {
          phone:""
        }
        let registerValues = {
          id:"123",
          phone:"",
          name:"",
          email:"",
          password:""
        }
        const selectedLocation = ref("");
        let responseRegister = {} as ResponseAppState<FetchResponse<UserInfo>>;
        let responseRegisterRef = ref({} as ResponseAppState<FetchResponse<UserInfo>>);
        let responseLogin = {} as ResponseAppState<FetchResponse<UserInfo>>;
        let responseLoginRef = ref({} as ResponseAppState<FetchResponse<UserInfo>>);
        const store = useStore();
        const router = useRouter();
        let routePath = ref(router.currentRoute);
        

        // components functions/methods
        const toggleSignInView = () => {
          showSignInModal.value = !showSignInModal.value;
          let background = document.querySelector('.modal-overlay') as HTMLDivElement;
          let loginModal = document.querySelector('.login-modal') as HTMLDivElement;

          if(showSignInModal.value){
            // close to open
            isLogin.value = true;
            loginValues.phone = "";
            document.querySelectorAll('.form-field input').forEach(item=>{
              if(!item.nodeValue && item.nextElementSibling?.tagName === "SPAN"){
                let span = item.nextElementSibling as HTMLSpanElement;
                span.style.top = "50%";
                span.style.fontSize = "20px";
                span.style.fontWeight = "300";
                span.style.transition = "all .5s ease";

              }
            })
            
            // background style changes
            background.style.backgroundColor="rgba(0,0,0,0.5)";
            background.style.zIndex="50";
            background.style.transition="all 0s ease-in";

            // login modal style changes
            loginModal.style.transform="translateX(0px)";
            loginModal.style.opacity="1";
            loginModal.style.transition="all 1.25s ease-in";
          } else {
            // open to close
            // background style changes
            background.style.transition="all 1.25s ease-in";
            background.style.backgroundColor="transparent";

            // login modal style changes
            loginModal.style.transform="translateX(400px)";
            loginModal.style.opacity="1";
            loginModal.style.transition="all 1.25s ease-in";

            setTimeout(()=>{
                background.style.zIndex="-10";
            },1100)
          }
        }
        const toggleLocationView = () => {
          showLocationModal.value = !showLocationModal.value;
          let background = document.querySelector('.modal-overlay') as HTMLDivElement;
          let locationModal = document.querySelector('.location-modal') as HTMLDivElement;

          if(showLocationModal.value){
            // close to open
            // background style changes
            background.style.backgroundColor="rgba(0,0,0,0.5)";
            background.style.zIndex="50";
            background.style.transition="all 0s ease-in";

            // login modal style changes
            locationModal.style.transform="translateX(0px)";
            locationModal.style.opacity="1";
            locationModal.style.transition="all 1.25s ease-in";
          } else {
            // open to close
            // background style changes
            background.style.transition="all 1.25s ease-in";
            background.style.backgroundColor="transparent";

            // login modal style changes
            locationModal.style.transform="translateX(-400px)";
            locationModal.style.opacity="1";
            locationModal.style.transition="all 1.25s ease-in";

            setTimeout(()=>{
                background.style.zIndex="-10";
            },1100)
          }
        }
        const userInputLogin = (e:any) => {
          loginValues.phone = e.target.value;
        }
        const userInputRegister = (e:any) => {
          switch (e.target.name) {
            case "phone":
              registerValues.phone = e.target.value;
              break;
            case "name":
              registerValues.name = e.target.value;
              break;
            case "email":
              registerValues.email = e.target.value;
              break;
            case "password":
              registerValues.password = e.target.value;
              break;
            default:
              break;
          }
        }
        const submitLogin = async () => {
          if(!Object.values(loginValues).includes("")){
            responseLogin = {
              ...responseLogin,
              dataState:DATASTATE.loading
            }
            responseLoginRef.value = responseLogin;
            try {
              const response = await fetch(`http://localhost:8000/api/v1/userinfo/get/${loginValues.phone}/`);
              const data:FetchResponse<UserInfo> = await response.json();
              
              if(data.status_code === 200){
                store.dispatch('user/setUserInfoAction',data.data);
                let form = document.querySelector('#login-form') as HTMLFormElement;
                form.reset();
                toggleSignInView();
                responseLogin = {
                  ...responseLogin,
                  dataState:DATASTATE.success,
                  appData:data,
                  error:""
                }
                responseLoginRef.value = responseLogin;
              } else {
                responseLogin = {
                  ...responseLogin,
                  dataState:DATASTATE.error,
                  error:data.message
                }
                responseLoginRef.value = responseLogin;
              }
            } catch (error:any) {
              responseLogin = {
                ...responseLogin,
                dataState:DATASTATE.error,
                error
              }
              responseLoginRef.value = responseLogin
            }
          } else {
            alert("Please fill in each field to login");
          }
        }
        const submitLocation = () => {
          // validate output
          if(selectedLocation.value){
            store.dispatch('location/setLocationAction',selectedLocation.value);
            toggleLocationView();
            router.push({name:"Restaurants"});
            let selectElement = document.querySelector('#location-select') as HTMLSelectElement;
            selectElement.value = "";            

          } else {
            alert("Please select a location from the list");
          }
        }
        const submitRegister = async () => {
          if(!Object.values(registerValues).includes("")){
            // fetch to api to save user
            responseRegister = {
              ...responseRegister,
              dataState:DATASTATE.loading
            }
            try {
              const response = await fetch('http://localhost:8000/api/v1/userinfo/create/',{
                    method: 'POST', 
                    mode: 'cors', 
                    cache: 'no-cache', 
                    credentials: 'same-origin', 
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    redirect: 'follow',
                    referrerPolicy: 'no-referrer',
                    body: JSON.stringify(registerValues) 
                })
              const data:FetchResponse<UserInfo> = await response.json();

              if(data.status_code === 200){
                store.dispatch('user/setUserInfoAction',data.data);
                let form = document.querySelector('#login-form') as HTMLFormElement;
                form.reset();
                toggleSignInView();
                responseRegister = {
                  ...responseRegister,
                  dataState:DATASTATE.success,
                  appData:data,
                  error:""
                }
              } else {
                responseRegister = {
                  ...responseRegister,
                  dataState:DATASTATE.error,
                  error:data.message
                }
                responseRegisterRef.value = responseRegister;
              }
            } catch (error:any) {
              responseRegister = {
                ...responseRegister,
                dataState:DATASTATE.error,
                error:"Please try again"
              }
            }
          } else {
            alert("Please fill in each field to register");
          }          
        }
        const clearLocation = () => {
          store.dispatch('location/removeLocationAction');
          localStorage.removeItem('cart');
          router.push({name:"Home"})
        }
        const logout = () => {
          store.dispatch('user/resetUserInfoAction');
        }
        const focusInput = (e:any) => {
          let span = e.target.nextElementSibling as HTMLSpanElement;
          span.style.top = "7px";
          span.style.fontSize = "9px";
          span.style.fontWeight = "600";
          span.style.transition = "all .5s ease";
        }
        const blurInput = (e:any) => {
          let input = e.target.value as string;

          if(input === ""){
            let span = e.target.nextElementSibling as HTMLSpanElement;
            span.style.top = "50%";
            span.style.fontSize = "20px";
            span.style.fontWeight = "300";
            span.style.transition = "all .5s ease";
          }
        }


        // computed
        const loginStatus = computed(()=> store.state.user.isLoggedIn );
        const cartQuantity = computed(() => store.state.cart.order.cart_quantity);
        const userLocation = computed(() => store.state.location.state.location);

        // watch
        watch(routePath,()=>{
          if(routePath.value.path.split("/").includes("checkout") || routePath.value.path.split("/").includes("confirmation")){
            isNavbarElementShowing.value = true;
          } else {
            isNavbarElementShowing.value = false;
          }
          if(routePath.value.path === "/"){
            isHomeView.value = true;
          } else {
            isHomeView.value = false;
          }
        })

        // lifecycle hooks
        onMounted(()=>{
          let localUserState = JSON.parse(localStorage.getItem('user')!);

          if(localUserState){
            store.dispatch('user/setUserInfoAction',localUserState);
          } else {
            store.dispatch('user/resetUserInfoAction');
          }
          store.dispatch('location/setLocationAction',"")
        })

        return {
          toggleSignInView,
          toggleLocationView,
          submitLogin,
          focusInput,
          blurInput,
          loginFields,
          registerFields,
          isLogin,
          submitRegister,
          submitLocation,
          userInputLogin,
          userInputRegister,
          loginValues,
          logout,
          responseRegisterRef,
          responseLoginRef,
          loginStatus,
          cartQuantity,
          selectedLocation,
          userLocation,
          clearLocation,
          isNavbarElementShowing,
          isHomeView,
        }
    }
})
</script>

<style scoped>
nav{
  position: fixed;
  top: 0;
  left:0;
  right: 0;
  z-index: 5;
  background-color: #fff;
  height:80px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 1px 5px 15px rgba(117, 117, 117, 0.15);
  padding:0 5%;
}
.left-nav,
.left-nav-location{
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 25px;
    margin-right: 20px;
    font-size: 14px;
}
.left-nav-checkout h1{
  font-size: 14px;
}
.left-nav svg:hover{
  transform:scale(1.07);
  transition:all 0.5s linear;
}
.right-nav{
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 20px;
}
.cart-link{
  position:relative;
}
.no-location{
  color: #888;
}
.nav-header-btn{
  cursor: pointer;
  outline:0;
  border:0;
  background-color: transparent;
  display: flex;
  align-content: center;
  justify-content: center;
}
.nav-header-btn img{
  width: 20px;
  pointer-events: none;
}
.toggle-location-btn,
.remove-location-btn{
  position:relative;
}
.nav-header-btn::after{
  background-color: #333;
  color:#fff;
  position:absolute;
  bottom:-30px;
  right:0;
  border-radius: 5px;
  padding:3px 7px;
}
.toggle-location-btn:hover::after{
  content:"Select";
}
.remove-location-btn:hover::after{
  content:"Reset";
}
/* badge */
.cart-badge{
  position:absolute;
  top: -15px;
  right:-20px;
  background-color: red;
  color:#fff;
  border-radius: 50%;
  font-size: 13px;
  width: 20px;
  height: 20px;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* sign in modal */
.modal-overlay{
  width: 100vw;
  height: 100vh;
  /* background-color: rgba(0, 0, 0, 0.5); */
  background-color: transparent;
  position:fixed;
  top:0;
  left:0;
  right:0;
  bottom:0;
  z-index: -10;
  /* z-index: 20; */
}
.modal{
  width: 400px;
  height: 100vh;
  position: absolute;
  top:0;
  bottom:0;
  opacity:1;
  background-color: #fff;
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 150px auto;
  gap:2.5vh;
  padding:20px;
}
.login-modal{
  right:0;
  transform: translateX(400px);
}
.location-modal{
  left:0;
  transform:translateX(-400px);
}
.modal-header{
  display: grid;
  grid-template-columns: repeat(12,1fr);
  grid-template-rows: repeat(6,1fr);
}
.modal-header button{
  font-size: 24px;
  font-weight: 500;
  background-color: transparent;
  border:none;
  outline:none;
  cursor: pointer;
  grid-column: 2/3;
  grid-row: 1/2;
  text-align: left;
}
.modal-header img{
  width: 100px;
  grid-column: 9/-1;
  grid-row: 2/-1;
}
.location-header img{
  width: 60px;
}
.modal-header h1{
  grid-column: 2/9;
  grid-row: 3/4;
}
.modal-header p{
  grid-column: 2/9;
  grid-row: 4/5;
  font-size: 14px;
  padding-bottom: 15px;
  border-bottom: 1px solid #ccc;
}

.login-header p button{
  font-size: 14px;
  color:orange;
  font-weight: 600;
}

.modal-body{
  padding:0 50px;
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 15px;

}
.login-body{
  padding:15px;
}
.form-section{
  height: 100%;
}
.form-section form{
  height: 100%;
  display: flex;
  flex-direction: column;
  gap:10px;
}
.form-field{
  height: 50px;
  position: relative;
}
.form-field input,
.form-field select{
  width: 100%;
  height: 100%;
  border-radius: 5px;
  outline:0;
  border:1px solid #ccc;
  padding:10px;
  font-size: 16px;
}
.form-field span{
  height: fit-content;
  width: fit-content;
  position:absolute;
  top:50%;
  left:0;
  right:0;
  bottom:0;
  transform:translate(15px, -50%);
  font-size: 20px;
  pointer-events: none;
}



.form-field input[type=submit]{
  height: 40px;
  background-color: orange;
  color:#fff;
  font-size: 18px;
  text-transform: uppercase;
  font-weight: 600;
  letter-spacing: 1px;
  outline:0;
  border:0;
  border-radius: 5px;
  cursor: pointer;
}
.form-field p{
  font-size: 11px;
  margin-top: 10px;
  color:#555;
}

.form-field p.register-warning{
  color:red;
  font-size:16px;
  padding-bottom:20px;
  font-weight: 600;
}



@media (max-width:769px) {
    nav{
        padding:0 2.5%;
        overflow-x: auto;
    }
    .link-text{
        display:none;
    }
    .link-icon{
        padding:5px;
        position:relative;
        font-size: 20px;
    }
    .link-icon:hover::before{
        content:attr(data-before-content);
        position: absolute;
        bottom:-23px;
        right:0;
        width:50px;
        text-align: center;
        font-size: 14px;
        padding:5px 5px;
        background-color: #333;
        color:#fff;
        border-radius: 4px;
        transition: all ease-in .3s;
        z-index: 10;
    }
    .cart-badge{
      right:-10px;
    }
}
</style>