import { defineConfig } from "vitepress";

import problem_items from "./problem_items.json";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "LeetCode Solutions",
  description: "Solutons For LeetCode Problems",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      {
        text: "Introduction",
        link: "/Introduction",
      },
      {
        text: "Problems",
        link: "/Problems_order1",
      },
    ],

    sidebar: [
      {
        text: "Summary",
        items: [
          {
            text: "Introduction",
            link: "/Introduction",
          },
          {
            text: "Problems",
            link: "/Problems_order1",
          },
        ],
      },
      {
        text: "Problems",
        items: problem_items,
      },
    ],

    socialLinks: [
      { icon: "github", link: "https://github.com/vuejs/vitepress" },
    ],

    search: {
      provider: "local",
    },
  },
  markdown: {
    lineNumbers: true,
    math: true,
  },
});
