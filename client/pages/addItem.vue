<template>
<v-card
    light
    :loading="isUpdating"
  >
    <div id="app">
    <v-app id="inspire">
    <v-form @submit.prevent="submitItem">
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
           required
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
        商品を追加
      </v-btn>
    </v-card-actions>
        </v-row>
      </v-container>
    </v-form>
  </v-app>
</div>
</v-card>
</template>

<script>
export default {
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
      title: '商品追加',
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
    async submitItem () {
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
        const response = await this.$axios.$post('/items/add', formData, config)　// eslint-disable-line
        this.$router.push('/items')
      } catch (e) {
        console.log(e)
      }
    }
  }
}
</script>

