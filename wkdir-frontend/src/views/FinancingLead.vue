<template>
  <div class="financinglead container">
    <ul class="collection with-header">
      <li class="collection-item" v-for="(value, key) in opts" :key="key">
        <div
            @click="(e) => {
              $router.push('/financing/')
            }"
            style="cursor:pointer;">
          {{value}}
          <a href="#!" class="secondary-content">
            <i class="material-icons" style="color: #195ab4 !important;">send</i>
          </a>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Lead',
  components: {
  },
  data(){
    return {
      opts: [
        'Ciclos Produtivos',
        'Serviços',
        'Aquisição de maquinários',
        'Insumos',
      ]
    }
  },
  mounted(){
  }
}
</script>
