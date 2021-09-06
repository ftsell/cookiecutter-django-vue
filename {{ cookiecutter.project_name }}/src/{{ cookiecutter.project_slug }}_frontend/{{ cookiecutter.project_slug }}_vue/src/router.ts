import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import NotFound from "@/views/404.vue";

Vue.use(VueRouter);

const routes: RouteConfig[] = [
        {
            path: "/",
            name: "Index",
            component: () =>
                import(
                    /* webpackChunkName: "chunk-index" */ "@/views/Index.vue"
                ),
        },
        {
            path: "*",
            component: NotFound,
        },
    ]


export default new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes,
});
