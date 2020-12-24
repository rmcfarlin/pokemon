<template>
  <Layout>

    <!-- Learn how to use images here: https://gridsome.org/docs/images -->
    <!-- <g-image alt="Example image" src="~/favicon.png" width="135" /> -->

    <div class="card text-white bg-dark mb-3" style="max-width: 18rem;" v-for="p in data" v-bind:key="p.name">
      <div class="card-body">
        <img :v-if="p.img != null" :src="p.img" class="card-img-top" alt="Pokemon" />
        <!-- <h5 class="card-title">{{p.img}}</h5> -->
        <h5 class="card-title">{{p.name}}</h5>
        <!-- <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p> -->
        <g-link :to="p.url" class="btn btn-info">See details</g-link>
      </div>
    </div>

    
  </Layout>
</template>

<script>
import axios from "axios"
const data = require('../../pokemon.json')

export default {
  metaInfo: {
    title: 'Pokemon'
  },
  data() {
    return {
      data: data
    }
  },
  // created: function() {
  //   axios.get("https://pokeapi.co/api/v2/pokemon?offset=0&limit=1200", {
  //     "method": "GET"
  //   }).then(res => {
  //     this.pokemon = res.data.results;
  //   });
  // }
}
</script>

<style>
.home-links a {
  margin-right: 1rem;
}
</style>
