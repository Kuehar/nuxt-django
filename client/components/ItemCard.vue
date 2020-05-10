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
      <div class="action-buttons">
        <nuxt-link :to="`/items/${item.id}/`" class="btn btn-sm btn-primary">
          詳細
        </nuxt-link>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: ['item', 'onDelete']
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
