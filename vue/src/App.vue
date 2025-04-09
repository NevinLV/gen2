<script setup lang="ts">
import "bootstrap";
import HeaderComponent from "./components/HeaderComponent.vue";
import TextAreaComponent from "./components/TextAreaComponent.vue";
import {nextTick, onMounted, ref} from "vue";
import axios from "axios";

import * as Prism from "prismjs"
import "prismjs/themes/prism-tomorrow.css";
import "prismjs/components/prism-python"; // Поддержка Python
const code = ref<string>("import random\n" +
    "\n" +
    "def generate_question_and_answer(operation):\n" +
    "    if operation == '+':\n" +
    "        num1 = random.randint(1, 10)\n" +
    "        num2 = random.randint(1, 10)\n" +
    "        return (f'2 {operation} {num2}', f'{num1 + num2}')\n" +
    "    elif operation == '-':\n" +
    "        num1 = random.randint(1, 10)\n" +
    "        num2 = random.randint(1, 10)\n" +
    "        return (f'2 {operation} {num2}', f'{num1 - num2}')\n" +
    "\n" +
    "results = []\n" +
    "for _ in range(10):\n" +
    "    result = generate_question_and_answer('+')\n" +
    "    results.append(result)\n" +
    "\n" +
    "for i, (question, answer) in enumerate(results, start=1):\n" +
    "    print(f\"Question {i}: {question}\")\n" +
    "    print(\"Answer:\", answer))");

onMounted(() => {
  Prism.highlightAll();

  if (preBox.value){
    preBox.value.style.backgroundColor = "rgba(0, 0, 0, 0.38)"
  }

});

const example_task_text = ref<string>("Сколько будет 2+2?");

function updateExample(value: string){
  example_task_text.value = value;
}


async function generate() {
  next()
  // axios.post('https://genedis.ru/api/generator/example/', {}, {
  //   params:{
  //     text: example_task_text.value
  //   }
  // })
  //     .then(async response => {
  //
  //       code.value = response.data;
  //       await nextTick();
  //       Prism.highlightAll();
  //       console.log('Ответ от сервера:', response.data);
  //     })
  //     .catch(error => {
  //       console.error('Ошибка запроса:', error);
  //     });
}

const section1 = ref<HTMLElement | null>(null);
const section2 = ref<HTMLElement | null>(null);
const codeBox = ref<HTMLElement | null>(null);
const preBox = ref<HTMLElement | null>(null);

function next(){

  if (section1.value !== null){
    section1.value.style.transition = "1000ms";
    section1.value.style.opacity = "0";
    section1.value.style.marginTop = "-100vh";
    section1.value.style.zIndex = "0";
  }

  if (section2.value !== null){
    section2.value.style.transition = "5000ms";
    section2.value.style.opacity = "1";
  }
}

function preview(){
  if (section1.value !== null){
    section1.value.style.transition = "1000ms";
    section1.value.style.opacity = "1";
    section1.value.style.marginTop = "0";
    section1.value.style.height = "100vh";
  }

  if (section2.value !== null){
    section2.value.style.transition = "5000ms";
    section2.value.style.opacity = "0";
  }
}
</script>

<template style="width: 100%;">
  <HeaderComponent/>
  <div class="container" style="margin-top: 10px">
    <section ref="section1" style="height: 100vh">
      <div class="row justify-content-center mb-4">
        <div class="col-6 d-flex justify-content-center align-items-center">
          <div class="text-center main-text" >

            <div style="font-size: 18px; text-transform: uppercase">
              Генерация задачи по примеру
            </div>

          </div>
        </div>
      </div>
      <div class="row justify-content-center">
        <div class="col-6 d-flex justify-content-center align-items-center">
          <TextAreaComponent :text="example_task_text" @change-value="updateExample"/>
        </div>
      </div>
      <div class="row justify-content-center mt-3">
        <div class="col-6 d-flex justify-content-center align-items-center">
          <button class="gen-btn" @click="generate">
            <svg style="margin-right: 7px; margin-bottom: 2px" fill="black" xmlns="http://www.w3.org/2000/svg" id="Layer_1" data-name="Layer 1" viewBox="0 0 24 24" width="16" height="16">
              <path d="M12.566,24H8.719l2-8H6.586a2.561,2.561,0,0,1-2.451-3.3L7.976,0h9.467l-3,8h4.023a2.533,2.533,0,0,1,2.11,3.932Z"/>
            </svg>Сгенерировать</button>
        </div>
      </div>
    </section>

    <section ref="section2" style="height: 100vh; opacity: 0">
      <div class="row">
        <div class="col-1">

          <button class="py-5 black-btn" @click="preview">
            <svg class="mb-2" fill="white" id="Layer_1" height="30" viewBox="0 0 24 24" width="30" xmlns="http://www.w3.org/2000/svg" data-name="Layer 1">
              <path d="m13 2.58a2.564 2.564 0 0 0 -2.087-2.546 2.5 2.5 0 0 0 -2.913 2.466v14.5h-2v-5.389l-3.121 3.025a3 3 0 0 0 -.828 2.682 3.129 3.129 0 0 0 .9 1.637l5.049 5.045h14v-13.806l-9-2.014z"/>
            </svg>
            Назад
          </button>
        </div>

        <div class="col">
          <div class="row">
            <div class="main-text" style="font-size: 30px; text-transform: uppercase">
              Задача:
            </div>
            <div class="sub-text">
              {{ example_task_text }}
            </div>
          </div>
        </div>

        <div class="col">
          <div class="row">
            <div class="main-text" style="font-size: 30px; text-transform: uppercase">
              Код:
            </div>
            <div v-if="code.length > 0">
              <pre class="code-theme" ref="preBox"><code ref="codeBox" class="language-python">{{ code }}</code></pre>
            </div>
          </div>
        </div>

      </div>
    </section>

  </div>
</template>

