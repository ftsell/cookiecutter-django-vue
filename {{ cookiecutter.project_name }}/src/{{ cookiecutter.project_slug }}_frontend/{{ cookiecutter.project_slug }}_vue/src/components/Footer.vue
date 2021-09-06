{% raw -%}
<template>
  <div>
    <v-footer :absolute="true" app>
      <v-row justify="center" no-gutters>
        <div v-for="item of items" :key="item.text">
          <a v-if="item.link" :href="item.link" class="no-style">
            <v-btn rounded text>
              <v-icon>{{ item.icon }}</v-icon>
              <span>{{ item.text }}</span>
            </v-btn>
          </a>
        </div>
      </v-row>
    </v-footer>
  </div>
</template>
{% endraw -%}

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class Footer extends Vue {
  items = [
    {
      icon: "mdi-copyright",
      text: new Date().getFullYear(),
      link: "$TODO,
    },
    {
      icon: "mdi-github",
      text: "GitHub",
      link: "$TODO",
    },
  ];
}
</script>

<style scoped>
a.no-style,
a.no-style:link,
a.no-style:visited,
a.no-style:hover,
a.no-style:active {
  color: inherit;
  text-decoration: inherit;
  font-weight: inherit;
}
</style>
