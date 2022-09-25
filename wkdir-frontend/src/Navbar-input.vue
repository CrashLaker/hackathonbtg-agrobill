<template>
  <div id="navbar-input">
    <nav class="indigo">
      <div class="nav-wrapper container">
        <ul id="nav-mobile" class="left hide-on-med-and-down" style="width:100%;">
          <li style="width:100%;">
            <div class="input-field inline row" style="width:100%;">
              <span class="col s1">Path:</span>
              <input
                type="text"
                id="autocomplete-input"
                @keyup.enter="changePath"
                @keyup="inputOnChange"
                autocomplete="off"
                ref="inputPath"
                class="col s11 autocomplete"
                style="color:white;margin-top:8px;"/>
            </div>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>


<script>
export default {
  name: "Navbar-input",
  data(){
    return {

    }
  },
  methods: {
    changePath(){

    },
    inputOnChange(){

    }
  }
};
</script>