<template>
  <v-layout>
    <v-flex class="text-center">
      <img
        src="/v.png"
        alt="Vuetify.js"
        class="mb-5"
      >
      <blockquote class="blockquote">
        &#8220;First, solve the problem. Then, write the code.&#8221;
        <footer>
          <small>
            <em>&mdash;John Johnson</em>
          </small>
        <div class="row">
        <div class="col-12 text-right mb-4">
        <div class="d-flex justify-content-between">
          <h3>商品一覧</h3>
          <!-- <nuxt-link to="/items/add" class="btn btn-info">
            商品を追加する
          </nuxt-link> -->
        </div>
      </div>
      <template v-for="item in items">
        <div :key="item.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
          <item-card :on-delete="deleteitem" :item="item" />
        </div>
      </template>
    </div>
        </footer>
      </blockquote>
    </v-flex>
  </v-layout>
</template>

<script>
import ItemCard from '~/components/ItemCard.vue'

export default {
  components: {
    ItemCard
  },
  async asyncData ({ $axios, params }) {
    try {
      const items = await $axios.$get('items/')
      return { items }
    } catch (e) {
      return { items: [] }
    }
  },
  data () {
    return {
      items: []
    }
  },
  methods: {
    async deleteitem (item_id) { //eslint-disable-line
      try {
        await this.$axios.$delete(`/items/${item_id}/`) //eslint-disable-line
        const newitems = await this.$axios.$get('/items/')
        this.items = newitems
      } catch (e) {
        console.log(e)
      }
    }
  },
  head () {
    return {
      title: '商品一覧'
    }
  }
}
</script>