<template>
  <main class="container mt-5">
    <v-flex class="text-center">
        <div class="row">
          <div class="col-12 text-right mb-4">
            <div class="d-flex justify-content-between">
            <v-btn class="d-flex ma-2" to="/addItem" nuxt>
              商品を追加する
            </v-btn>
          <v-col class="d-flex ma-2" cols="12" sm="3">
          <v-select
            :category="category"
            label="カテゴリー"
            dense
            solo
          ></v-select>
          </v-col>
          <v-col cols="12" sm="6" md="4">
          <v-text-field
            append-icon="mdi-magnify"
            placeholder="検索"
            filled
            rounded
            dense
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="2" md="1">
        <v-btn class="search-btn">
          検索
        </v-btn>
        </v-col>
          </div>
      </div>
      <template v-for="item in items">
        <div :key="item.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
          <item-card :on-delete="deleteitem" :item="item" />
        </div>
      </template>
    </div>
    <div class="text-center">
      <v-pagination
        :length="4"
        prev-icon="mdi-menu-left"
        next-icon="mdi-menu-right"
      ></v-pagination>
    </div>
        </footer>
      </blockquote>
    </v-flex>
  </main>
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
      items: [],
      category: ['飲料','お花','本']
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
      title: '商品一覧',
      }
  }
}
</script>