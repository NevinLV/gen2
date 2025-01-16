<script setup lang="ts">
import "bootstrap";

const numStars = 75; // Количество звёзд
const body = document.body;

for (let i = 0; i < numStars; i++) {
  const star = document.createElement('div');
  star.classList.add('star');
  const size = Math.random() * 3 + 1; // Размер звезды
  star.style.width = `${size}px`;
  star.style.height = `${size}px`;
  star.style.top = `${Math.random() * 100}vh`;
  star.style.left = `${Math.random() * 100}vw`;
  star.style.animationDuration = `${Math.random() * 1.5 + 0.5}s`; // Случайная скорость мерцания
  body.appendChild(star);
}
</script>

<template>
  <div class="gen2"><img style="width: 300px" src="../public/GENe.png"/></div>
</template>

