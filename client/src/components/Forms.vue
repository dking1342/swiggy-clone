<template>
    <h1 class="body-header" v-if="loginStatus">You are logged in</h1>
    <div v-else-if="!loginStatus">
      <div class="login-header">
          <h1 v-if="isLoginForm">Login</h1>
          <h1 v-else-if="!isLoginForm">Register</h1>
          <p v-if="isLoginForm">or <button @click="isLoginForm = !isLoginForm">create an account</button></p>
          <p v-else-if="!isLoginForm">or <button @click="isLoginForm = !isLoginForm">login to your account</button></p>
      </div>
      <div class="login-body">
          <p class="register-warning" v-if="Boolean(error)">{{ error }}</p>
          <div class="form-section" v-if="isLoginForm">
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
                  </div>
                  <div class="form-field form-field-submit">
                      <input type="submit" value="Login">
                      <p>By clicking on Login, I accept the Terms & Conditions & Privacy Policy</p>
                  </div>
              </form>
          </div>
          <div class="form-section" v-else-if="!isLoginForm">
              <p class="register-warning" v-if="Boolean(error)">{{ error }}</p>
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
                      <input type="submit" value="Register">
                      <p>By creating an account, I accept the Terms & Conditions & Privacy Policy</p>
                  </div>
              </form>
          </div>
      </div>
    </div>
</template>

<script lang="ts">
import { DATASTATE, FetchResponse, ResponseAppState, UserInfo } from '@/types/fetch-types';
import { computed, defineComponent, onMounted, ref } from 'vue'
import { useStore } from 'vuex';

export default defineComponent({
    setup () {
        let isLoginForm = ref(true);
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
        let responseRegister = {} as ResponseAppState<FetchResponse<UserInfo>>;
        let responseRegisterRef = ref({} as ResponseAppState<FetchResponse<UserInfo>>);
        let responseLogin = {} as ResponseAppState<FetchResponse<UserInfo>>;
        let responseLoginRef = ref({} as ResponseAppState<FetchResponse<UserInfo>>);
        let store = useStore();

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
                
                
                // set localstorage state and 
                store.dispatch('user/setUserInfoAction',data.data);

                // reset form state
                let form = document.querySelector('#login-form') as HTMLFormElement;
                form.reset();

                // set response state
                responseLogin = {
                  ...responseLogin,
                  dataState:DATASTATE.success,
                  appData:data,
                  error:""
                }
                responseLoginRef.value = responseLogin;
              } else {
                responseRegisterRef.value.error = data.message;
              }
            } catch (error:any) {
              responseLogin = {
                ...responseLogin,
                dataState:DATASTATE.error,
                error:"Please try again"
              }
              responseLoginRef.value = responseLogin
            }
          } else {
            alert("Please fill in each field to login");
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
                // sets localstorage state
                store.dispatch('setUserInfoAction',data.data);

                // resets form state
                let form = document.querySelector('#login-form') as HTMLFormElement;
                form.reset();

                // sets response state
                responseRegister = {
                  ...responseRegister,
                  dataState:DATASTATE.success,
                  appData:data,
                  error:""
                }
              } else {
                // sets error state
                responseRegisterRef.value.error = "Please try again";
              }
            } catch (error:any) {
              responseRegisterRef.value.error = "Please try again";
            }
          } else {
            alert("Please fill in each field to register");
          }          
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
        const loginStatus = computed(() => store.state.user.isLoggedIn);
        const error = computed(()=> responseRegisterRef.value.error);

        // lifecycle hooks
        onMounted(()=>{
        })

        return {
            isLoginForm,
            submitLogin,
            loginFields,
            registerFields,
            userInputRegister,
            submitRegister,
            focusInput,
            blurInput,
            userInputLogin,
            error,
            loginStatus,
        }
    }
})
</script>

<style scoped>
    .login-header{
        display: grid;
        grid-template-columns: repeat(12,1fr);
        grid-auto-rows: minmax(30px,1fr);
    }
    .login-header button{
        font-size: 24px;
        font-weight: 500;
        background-color: transparent;
        border:none;
        outline:none;
        cursor: pointer;
        text-align: left;
    }
    .login-header h1{
        grid-column: 1/-1;
        grid-row: 1/2;
    }
    .login-header p{
        grid-column: 1/-1;
        grid-row: 2/3;
        font-size: 14px;
    }
    .login-header p button{
        font-size: 14px;
        color:orange;
        font-weight: 600;
    }

    .login-body{
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: 15px;
        width: 350px;
        max-width: 100%;
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
    .form-field input{
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

    .register-warning{
      font-size:16px;
      color:red;
      font-weight: 600;
    }
</style>