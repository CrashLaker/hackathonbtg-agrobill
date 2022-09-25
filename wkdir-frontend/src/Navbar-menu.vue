<template>
  <div id="navbar-menu">
    <nav class="indigo" style="background-color:#195ab4 !important;">
      <div class="nav-wrapper container">
        <a href="#" class="brand-logo center">
          <!-- Cloud<i class="material-icons">cloud</i> -->
          <img src="./assets/btglogo.png" style="height:88px;transform:translate(0px, -13px);"/>
        </a>
        <a href="#modal-login" class="right">
          <i class="material-icons">login</i>
        </a>
        <ul id="nav-mobile" class="left hide-on-med-and-down">
          <li><router-link to="/">Home</router-link></li>
          <!-- <li><router-link to="/financing/historico">Histórico</router-link></li> -->
          <!-- <li><router-link to="/about">About</router-link></li> -->
          <li><router-link to="/financing/lead">Financing</router-link></li>
          <!-- <li><router-link to="/agrobill">AgroBill!</router-link></li> -->
        </ul>
      </div>
    </nav>
  </div>
</template>


<script>
export default {
  name: "Navbar-menu"
};
</script>