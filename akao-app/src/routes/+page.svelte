<script lang="ts">
  import { onMount } from 'svelte';
  import '../app.css';
  import RouteTable from '$lib/components/RouteTable.svelte';
  let routes = [];
  onMount(async () => {
    const res = await fetch('/routes.json');
    routes = await res.json();
  });
</script>
<main class="min-h-screen bg-pastelBlue flex flex-col">
  <h1 class="text-3xl font-bold text-center my-8 text-blue-900">Akao</h1>
  <figure class="mb-8 flex flex-col items-center">
    <blockquote class="text-xl italic font-medium text-center text-gray-800 bg-white/70 rounded-lg px-6 py-4 border-l-4 border-blue-300 shadow max-w-2xl mx-auto">
      History isn’t just in books; it’s in the trails we tread and the stories we tell.
    </blockquote>
    <figcaption class="mt-4 text-center text-gray-600">
      &mdash; <span class="font-semibold">Beau Miles</span>
    </figcaption>
  </figure>
  <div class="mb-8 text-center bg-pastelYellow text-gray-700 py-4 rounded-lg shadow max-w-xl mx-auto mx-16">
    Made with <span aria-label="heart" role="img">❤️</span> by 
    <a class="underline text-blue-700" href="https://gabrielongzm.com" target="_blank" rel="noopener">Gabriel Ong</a>.
    <br>
    Source code <a class="underline text-blue-700" href="https://github.com/gongahkia/akao" target="_blank" rel="noopener">here</a>.
  </div>
  <RouteTable {routes} />
</main>