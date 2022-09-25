<template>
  <div class="financing container">

    <div class="row">
      <div class="input-field col s12">
        <i class="material-icons prefix">search</i>
        <input v-model="keysearch" id="search" type="text" class="">
        <label class="" for="search">Escolha uma instituição financeira</label>
      </div>
    </div>

    <div v-if="follow.length == 0">
      <form>
      <table>
        <thead>
          <tr>
              <th>Banco</th>
              <th>Tax</th>
              <th style="width:180px;">Selecionar</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(value, key) in rsFilter" :key="key">
            <td>
              <img :src="value.icon" style="max-height:30px;"/>
              <span style="display:inline-block;transform:translate(11px, -8px);">{{ value.title }}</span>
            </td>
            <td>{{ value.tax }}</td>
            <td>
              <!-- <button class="btn bgblue0">Financiar</button> -->
              <!-- <p>
                <label>
                  <input type="radio" class="filled-in" checked="checked" />
                  <span>Filled in</span>
                </label>
              </p> -->
              <template v-if="value.title == 'Banco BTG'">
                <p style="margin:0;padding:0;">
                  <label>
                    <input type="radio" name="aaa" class="filled-in" checked="checked"
                      @click="(e) => shade(e, key)"/>
                    <span></span>
                  </label>
                </p>
              </template>
              <template v-else>
                <p style="margin:0;padding:0;">
                  <label>
                    <input type="radio" name="aaa" class="filled-in" 
                      @click="(e) => shade(e, key)"/>
                    <span></span>
                  </label>
                </p>
              </template>
            </td>
          </tr>
        </tbody>
      </table>
      </form>
    </div>

    <div class="row" style="height:30px;">
      <div class="col s6" style="font-size:15px;">
        <!-- <div class="card-panel teal lighten-2"> -->
        <div class="card-panel bgwealth" style="color:white;">
          Quantidade de parcelas: 60
        </div>
      </div>
      <div class="col s6" style="font-size:15px;">
        <div class="card-panel bgwealth" style="color:white;">
          Vencimento da primeira: 27/09/2022
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col s8" style="font-size:25px;">
        <b>Disponível</b>: R$ 5.000.000,00
      </div>
      <div class="col s4">
        <button class="btn bgblue0" @click="() => {
          this.$router.push('/financing/confirm')
        }">Continuar</button>
      </div>
    </div>

    <!-- <div class="row">
      <div class="col s12">
        <button class="btn bgblue1" @click="() => {
          this.$router.push('/financing/historico')
        }">Histórico</button>
      </div>
    </div> -->

  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Financing',
  components: {
  },
  computed: {
    rsFilter(){
      let ks = this.keysearch || ''
      if (ks == '') return this.rs
      ks = ks.toLowerCase()
      let ret = this.rs.filter(d => {
        return d.title.toLowerCase().includes(ks)
      })
      return ret
    }
  },
  data(){
    return {
      follow: [],
      d: '',
      rs: [
        { title: 'Banco Santander', tax: 5.94, icon: '/santander.svg'},
        { title: 'Banco Itaú', tax: 5.27, icon: '/itau-logo.webp'},
        { title: 'Banco BTG', tax: 5.18, icon: '/btg.svg'},
        { title: 'Banco Bradesco', tax: 5.02, icon: '/bradesco.svg'},
      ],
      keysearch: '',
    }
  },
  beforeMount(){
    console.log(this.$route)
    // fullPath: /financing/asdfasd/asdfsadf
    // params: {url: 'dadfsdf'}
    // path: /financing/asdfasd/asdfsadf
  },
  mounted(){
    setTimeout(() => {
      this.shade(null, 2)
    })
  },
  methods: {
    shade(e, idx){
      // console.log('click', e)
      this.$el.querySelectorAll('tbody > tr').forEach((d,idx2) => {
        if (idx != idx2){
          d.style.opacity = 0.6
        }else{
          d.style.opacity = 1
        }
      })
    }
  }
}
</script>

<style >
</style>
