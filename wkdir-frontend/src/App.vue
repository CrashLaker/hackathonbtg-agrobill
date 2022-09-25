<template>
  <div id="app">
    <Navbar/>
    <div class="container" style="height:30px;">
    </div>
    <router-view/>
  </div>
</template>

<script>
import Navbar from '@/Navbar-menu.vue'
// import Navbar from '@/Navbar-input.vue'
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  components: {
    Navbar,
  },
  mounted(){

  }
}
</script>

<style>
.bgwealth{
  background: linear-gradient(213.86deg,#49647C 0%,#233446 100%) !important;
}
.colorblue0{
  color: #195ab4 !important;
}
.bgblue0{
  background-color: #195ab4 !important;
}
[type="radio"]:checked+span:after, [type="radio"].with-gap:checked+span:after{
  background-color: #195ab4 !important;
  border-color: #195ab4 !important;
}
[type="checkbox"].filled-in:checked+span:not(.lever):after {
  background-color: #195ab4 !important;
  border-color: #195ab4 !important;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
    
.input-field input[type=text]:focus {
    border-bottom: 1px solid #003a8c !important;
    box-shadow: 0 1px 0 0 #002766 !important;
}    

input[type=text]:not(.browser-default):focus:not([readonly])+label{
    color: #003a8c;
}
    
.progress {
    background-color: #597ef7;
}  
.progress .determinate {
    background-color: #10239e;    
}
.progress .indeterminate {
    background-color: #10239e;
}
</style>
