<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">
          {{ item.name }}
        </h2>
      </div>
      <div class="col-md-6 mb-4">
        <img
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="item.image"
          alt
        >
      </div>
      <div class="col-md-6">
        <div class="item-details">
          <h4>カテゴリー</h4>
          <p>{{ item.category }}</p>
          <hr>
          <h4>値段</h4>
          <p>{{ item.price }}</p>
          <hr>
          <h4>説明</h4>
          <p>{{ item.description }}</p>
          <hr>
          <v-btn :to="`/items/${item.id}/edit`" class="btn primary" nuxt>
            商品を編集する
            </v-btn>
        </div>
      </div>
    </div>
  </main>
</template>
<script>
export default {
  async asyncData ({ $axios, params }) {
    try {
      const item = await $axios.$get(`/items/${params.id}`)
      return { item }
    } catch (e) {
      return { item: [] }
    }
  },
  data () {
    return {
      item: {
      id:'',
      name:'',
      category:'',
      image:'',
      price:'',
      description:'',
      }
      /*icons:{
        category:
      },*/
    }
  },
  head () {
    return {
      title: '商品詳細'
    }
  }
}
</script>
<style scoped>
</style>
