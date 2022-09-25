<template>
  <div class="historicofinancing container" style="text-align:left;">
    <h5>
      Nova proposta de financiamento R$ 10.000.000,00<br>
      <button style="margin-top:8px;" class="btn bgblue0" @click="() => {
        this.$router.push('/financing/lead')
      }">Contratar</button>
    </h5>
    <p style="font-size:18px;" class="colorblue0">
      💹<span style="font-weight:bold;">100%</span> Retorno financeiro com base em faturamentos nas demais instituições.
    </p>

    <a href="#!">Ver detalhes</a>

    <h5>Sugestões</h5>

    <div style="width:300px;">
      <table>
        <tbody>
          <tr>
            <td>Seguros Agronegócio</td>
            <td>
              <p style="margin:0;padding:0;">
                <label>
                  <input type="checkbox" name="aaa" class="filled-in" checked="checked"/>
                  <span></span>
                </label>
              </p>
            </td>
          </tr>
          <tr>
            <td>Oferta de câmbio em dólar</td>
            <td>
              <p style="margin:0;padding:0;">
                <label>
                  <input type="checkbox" name="aaa" class="filled-in"/>
                  <span></span>
                </label>
              </p>
            </td>
          </tr>
          <tr>
            <td>Investimentos BTG</td>
            <td>
              <p style="margin:0;padding:0;">
                <label>
                  <input type="checkbox" name="aaa" class="filled-in" checked="checked"/>
                  <span></span>
                </label>
              </p>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <a href="#!">AGXY3</a><br>
    <a href="#!">BEEF3</a><br>
    <a href="#!">CAML3</a><br>
    <br>
    
    <div class="row">
      <div class="col s6">
        <button class="btn bgblue0" style="margin:auto;float:right;width:100%;">
         Sim 
        </button>
      </div>
      <div class="col s6">
        <button class="btn bgblue0" style="margin:auto;float:right;width:100%;">
         Fale com o BTG
        </button>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {
  }
}
</script>

