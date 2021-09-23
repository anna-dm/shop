<template>
  <q-layout view="hHh Lpr lFf">
    <q-header elevated>
      <div class="bg-black text-white full-width text-center q-py-md">
        При первом заказе пижама в подарок
      </div>

      <q-toolbar class="bg-grey-4 text-black">
        <q-btn stretch flat label="Selena" type="a" :to="{ name: 'index' }" />
        <q-btn
          stretch
          flat
          label="НОВИНКИ"
          @mouseover="menu = 'new'"
          @mouseleave="menu = ''"
        />

        <q-btn
          stretch
          flat
          label="ХИТЫ ПРОДАЖ"
          @mouseover="menu = 'hit'"
          @mouseleave="menu = ''"
        />

        <q-btn
          stretch
          flat
          label="ОДЕЖДА"
          @mouseover="menu = 'clothes'"
          @mouseleave="menu = ''"
        />

        <q-btn
          stretch
          flat
          label="АКСЕССУАРЫ"
          @mouseover="menu = 'accessories'"
          @mouseleave="menu = ''"
        />

        <q-btn
          stretch
          flat
          label="РАСПРОДАЖА"
          color="red"
          @mouseover="menu = 'sale'"
          @mouseleave="menu = ''"
        />

        <q-space />
        <div>
          <q-btn
            stretch
            flat
            label="ПОКУПАТЕЛЯМ"
            type="a"
            :to="{ name: 'contact' }"
          />
        </div>
      </q-toolbar>
      <div class="full-width bg-grey-4 text-black" v-if="menu == 'new'">
        <ul>
          <li>Новая одежда</li>
          <li>Новые аксессуары</li>
          <li>Новые сумки</li>
        </ul>
      </div>
      <div class="full-width bg-grey-4 text-black" v-if="menu == 'hit'">
        <ul>
          <li>Новая одежда</li>
          <li>Новые аксессуары</li>
          <li>Новые сумки</li>
        </ul>
      </div>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
const linksList = [
  {
    title: "Каталог",
    icon: "school",
    to: { name: "index" },
  },
];

import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "MainLayout",

  setup() {
    let menu = ref("");
    return {
      essentialLinks: linksList,
      menu,
    };
  },
  methods: {
    onNew() {
      this.menu = this.menu == "" ? "new" : "";
    },
  },

  methods: {
    onHit() {
      this.menu = this.menu == "" ? "hit" : "";
    },
  },
});
</script>
