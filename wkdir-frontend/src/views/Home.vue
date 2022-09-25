<template>
  <div class="home">
    <div style="width:100%;height:100%;margin-top:-30px;overflow:hidden;position:relative;">
      <button v-show="$store.state.showbanner" class="btn amber darken-4" style="position:absolute;top:40px;left:50%;margin-left:-200px;z-index:20;"
        @click="() => {
          this.$router.push('/financing/assessoria')
        }"
      >
        <i class="material-icons">person</i> 
        <span style="display:inline-block; transform:translate(6px, -4px);">Você tem uma assessoria BTG disponível!</span>
      </button>

      <div style="position:absolute;z-index:10;width:500px; top:200px;text-align:left;left:80px;">
        <h4>
          Open Finance
        </h4>
        <p>
          O Open Finance foi criado para oferecer acesso a mais produtos e serviços financeiros que mais combinam com você, aumentando ainda mais as suas possibilidades. Entenda melhor como funciona essa iniciativa do Banco Central!
        </p>
      </div>
      <img src="../assets/banner-home.jpg" 
        style="transform:translate(-400px, 0px); height:560px;"/>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {
  },
  computed: {
    showbanner(){
      return this.$store.state.showbanner
    }
  },
  data(){
    return {
    }
  },
  mounted(){
  }
}
</script>
