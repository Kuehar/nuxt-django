import firebase from 'firebase'


if (!firebase.apps.length) {
    firebase.initializeApp(
        {
            apiKey: "AIzaSyB783GXDEM8Z9DGkZyW6YeyFACFVF7WS2c",
            authDomain: "nuxt-django-34c06.firebaseapp.com",
            databaseURL: "https://nuxt-django-34c06.firebaseio.com",
            projectId: "nuxt-django-34c06",
            storageBucket: "nuxt-django-34c06.appspot.com",
            messagingSenderId: "357735890622",
            appId: "1:357735890622:web:2755ecadaff9d4fa8ea8ef",
        }
    )
}

export default firebase