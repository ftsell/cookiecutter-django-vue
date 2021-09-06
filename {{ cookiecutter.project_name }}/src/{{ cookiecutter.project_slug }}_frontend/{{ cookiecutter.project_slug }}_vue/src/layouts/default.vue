<template>
  <v-app>
    <v-main>
      <v-container>
        <slot />
      </v-container>
    </v-main>
    <Footer />
  </v-app>
</template>

<script lang="ts">
import { Component, Vue, ProvideReactive } from "vue-property-decorator";
import Footer from "@/components/Footer.vue";

@Component({
  components: { Footer },
})
export default class DefaultLayout extends Vue {}
</script>
