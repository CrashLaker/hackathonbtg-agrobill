<template>
  <div class="historicofinancing container" style="text-align:left;">
    <h5>
      Extrato financeiro
    </h5>
    <h5>
      Tipo
    </h5>
    <h5>
      Financiamento AGRO
    </h5>
    <p style="font-weight:bold; color:#66bb6a;">
      desconto BTG personalizado de 10%
    </p>
    <h5>
      Forma de pagamento
    </h5>
    <p>
      Débito em conta
    </p>
    <h5>
      Número de parcelas
    </h5>
    <p>
      12x R$ 799.408,00
    </p>

    <h5>
      Data da primeira parcela
    </h5>
    <p>
      27/10/2022
    </p>

    <h5>
      Taxa de custos mensal: 5,58%
    </h5>
    <a href="#!">Ver custos detalhados</a>
    
    <template v-if="!bought">
      <div class="row">
        <div class="col s12">
          <button class="btn bgblue0" style="margin:auto;float:right;"
            @click="confirm">
            Confirmar
          </button>
        </div>
      </div>
    </template>
    <template v-else>
      <div class="row" style="height:30px;">
        <div class="col s6" style="font-size:15px;">
          <!-- <div class="card-panel teal lighten-2"> -->
          <div class="card-panel bgwealth" style="color:white;cursor:pointer;"
          @click="(e) => {
            this.$router.push('/financing/historico')
            }">
            Visualizar 
          </div>
        </div>
        <div class="col s6" style="font-size:15px;">
          <div class="card-panel bgwealth" style="color:white;cursor:pointer;">
            Compartilhar Comprovante
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {
  },
  data(){
    return {
      bought: false,
    }
  },
  methods: {
    confirm(){
      this.$store.dispatch('togglebanner')
      setTimeout(() => {
        this.toast('Confirmando...')
        setTimeout(() => {
          this.toast('Finalizado', 'ok')
          setTimeout(() => {
            this.bought = true
          }, 100)
        }, 600)
      }, 100)
    }
  }
}
</script>

