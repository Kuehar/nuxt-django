<template>
  <v-flex xs12 sm8 md4>
    <v-card class="elevation-12">
      <v-toolbar dark color="primary">
        <v-toolbar-title>登録</v-toolbar-title>
      </v-toolbar>
      <v-form>
        <v-card-text>
          <p v-if="error" class="error">
            {{ error }}
          </p>
          <v-text-field class="email-field" v-model="form.email"  name="login" label="メールアドレス" type="email" required />
          <v-text-field class="email-field" v-model="form.username"  name="username" label="ユーザーネーム" type="email" required />
          <v-text-field class="password" v-model="form.password" name="password" label="パスワード" type="password" required/>
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn @click='login' type="submit" color="primary">
            登録
          </v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-flex>
</template>

<script>
export default {
  auth: false,
  data: () => ({
    form: {
      email: '',
      password: ''
    }
  }),
  methods: {
    async login () {
      try {
        await this.$auth.loginWith('local',{data:this.data})
        .then(() => this.$toast.success('ログインしました'))
      } catch (e) {
        this.error = 'Login failed.'
      }
    }
  }
}
</script>
