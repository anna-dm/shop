<template>
  <q-page>
    <div class="row">
      <div class="col-8"></div>
      <div class="col-4 text-center">
        <div>
          Юбка из смесового хлопка с контрастными вставками {{ itemId }}
        </div>
        <div>Цена</div>
        <div>Цвет</div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "PageIndex",
  props: {
    itemId: {
      type: String,
      required: true,
    },
  },
});
</script>
