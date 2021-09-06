<template>
  <app-layout>
    <p>{{ cookiecutter.project_name }} index page</p>
  </app-layout>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import AppLayout from "@/layouts/app.vue";

@Component({
  components: { AppLayout },
})
export default class Index extends Vue {}
</script>
