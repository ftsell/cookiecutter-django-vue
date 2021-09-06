<template>
  <default-layout>
    <h1>Page not found</h1>
  </default-layout>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import DefaultLayout from "@/layouts/default.vue";

@Component({
  components: { DefaultLayout },
})
export default class NotFound extends Vue {}
</script>
