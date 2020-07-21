<template>
  <div class="card item-card">
    <img :src="item.image" class="card-img-top">
    <div class="card-body">
      <h5 class="card-title">
        {{ item.name }}
      </h5>
      <p class="card-text">
        <strong>カテゴリー</strong> {{ item.category }}
      </p>
      <p class="card-text">
        <strong>値段:</strong> {{ item.price }}
      </p>
      <div>
      <v-btn class="ma-2" text icon color="blue lighten-2">
        <v-icon>mdi-thumb-up</v-icon>
      </v-btn>
      <v-btn class="ma-2" text icon color="red lighten-2">
        <v-icon>mdi-thumb-down</v-icon>
      </v-btn>
      <v-btn class="ma-2" text icon color="green lighten-2" @click="onCopy(`http://localhost:3000/items/${item.id}/`)">
        <v-icon>mdi-share-variant</v-icon>
      </v-btn>
    </div>
      </v-col>
      <div class="action-buttons">
        <v-btn class="primary" :to="`/items/${item.id}/`" nuxt>
          詳細
        </v-btn>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: ['item', 'onDelete'],
  methods: {
    onCopy(url) {
        this.$copyText(url)
        this.$toast.success('URLがコピーされました!!')
      }
    }
  }
</script>
<style>
.item-card {
    box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
}
img.card-img-top{
    height:200px;
}
.action-buttons {
  text-align: right;
}
</style>
