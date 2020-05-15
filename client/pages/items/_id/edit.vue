<template>
<v-card
    light
    :loading="isUpdating"
  >
    <div id="app">
    <v-app id="inspire">
    <v-container>
    <div class="col-12 text-center my-3">
        <h3 class="mb-3 display-4 text-uppercase">
          {{ item.name }}
        </h3>
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
          <h4>値段</h4>
          <p>{{ item.price }}</p>
          <h4>説明</h4>
          <p>{{ item.description }}</p>
          </div>
          </div>
          </v-container>
    <v-form @submit.prevent="editItem">
      <v-container>
        <v-row>
          <v-col
            cols="12"
            md="4"
          >
            <v-text-field
              v-model="item.name"
              label="商品名"
              required
            ></v-text-field>
          </v-col>
  
          <v-col
            cols="12"
            md="4"
          >
            <v-text-field
              v-model="item.category"
              :counter="10"
              label="カテゴリー"
              required
            ></v-text-field>
          </v-col>
  
          <v-col
            cols="12"
            md="4"
          >
            <v-text-field
              v-model="item.price"
              label="値段"
              required
            ></v-text-field>
          </v-col>
          
          <v-col
            cols="12"
            md="4"
          >
            <v-text-field
              v-model="item.description"
              label="商品説明"
              required
            ></v-text-field>
          </v-col>
          <v-col
            cols="12"
            md="4"
          >
           <v-file-input
           v-model="item.image"
           label="商品画像"
           filled
           prepend-icon="mdi-camera"
           ></v-file-input>
          </v-col>
          <v-card-actions>
      <v-spacer />
      <v-btn
        class="btn-primary"
        :loading="isUpdating"
        color="primary"
        depressed
        @click="isUpdating = true"
        type="submit"
      >
        <v-icon left>
          mdi-post
        </v-icon>
        商品を更新
      </v-btn>
    </v-card-actions>
        </v-row>
      </v-container>
    </v-form>
    <v-form @submit.prevent="deleteItem">
    <button class="btn btn-sm btn-danger">
          削除
    </button>
    </v-form>
  </v-app>
</div>
</v-card>
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
        name: '',
        category: '',
        image: '',
        price: '',
        description: '',
      },
      preview: '',
      autoUpdate: true,
      isUpdating: false,
      title: '商品編集',
  }
  },
  watch: {
    isUpdating (val) {
      if (val) {
        setTimeout(() => (this.isUpdating = false), 3000)
      }
    }
  },
  methods: {
    createImage (file) {
      const reader = new FileReader()
      const vm = this
      reader.onload = (e) => {
        vm.preview = e.target.result
      }
      reader.readAsDataURL(file)
    },
    async deleteItem () { // eslint-disable-line
      try {
        const deleteditem = this.item
        await this.$axios.$delete(`/items/${deleteditem.id}/edit`) // eslint-disable-line
        const newItems = await this.$axios.$get('/items/')
        this.items = newItems
        this.$router.push('/items')
      } catch (e) {
        console.log(e)
      }
    },
    async editItem () {
      const editeditem = this.item
       //if (editeditem.image.includes('http://)') !== -1) {
        //delete editeditem.image
      //}
      const config = {
        headers: { 'content-type': 'multipart/form-data' }
      }
      const formData = new FormData()
      for (const data in editeditem) {
        formData.append(data, editeditem[data])
      }
      try {
        const response = await this.$axios.$patch(`/items/${editeditem.id}/edit`, formData, config)　// eslint-disable-line
        this.$router.push('/items')
      } catch (e) {
        console.log(e)
      }
    }
  }
}
</script>
