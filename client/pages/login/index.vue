<template>
  <v-flex xs12 sm8 md4>
    <v-card class="elevation-12">
      <v-toolbar dark color="primary">
        <v-toolbar-title>Login</v-toolbar-title>
      </v-toolbar>
      <v-form novalidate @submit="login">
        <v-card-text>
          <p v-if="error" class="error">
            {{ error }}
          </p>
          <v-text-field v-model="form.email" prepend-icon="person" name="login" label="email" type="text" required />
          <v-text-field
            id="password"
            v-model="form.password"
            prepend-icon="lock"
            name="password"
            label="Password"
            type="password"
            required
          />
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn type="submit" color="primary">
            Login
          </v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-flex>
</template>

<script>
export default {
  middleware: 'auth',
  data: () => ({
    error: null,
    form: {
      email: '',
      password: ''
    }
  }),
  methods: {
    async login () {
      try {
        const config = {
        headers: { 'content-type': 'application/json' }
        }
        await this.$auth.login('local',{ data: this.form,config })
        if (this.$auth.hasScope('items')) {
          this.$nuxt.$router.push('/items')
        } else if (this.$auth.hasScope('inspire')) {
          this.$nuxt.$router.push('/inspire')
        }
      } catch (e) {
        this.error = 'Login failed.'
      }
    }
  }
}
</script>
