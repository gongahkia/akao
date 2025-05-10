<script lang="ts">
  import { onMount } from 'svelte';
  import RouteTable from '$lib/components/RouteTable.svelte';
  let routes = [];

  // Fetch JSON data on mount
  onMount(async () => {
    const res = await fetch('/routes.json');
    routes = await res.json();
  });
</script>

<main class="min-h-screen bg-pastelBlue flex flex-col">
  <h1 class="text-3xl font-bold text-center my-8 text-blue-900">Akao Routes</h1>
  <RouteTable {routes} />
  <footer class="mt-auto py-4 text-center bg-pastelYellow text-gray-700">
    Made with <span aria-label="heart" role="img">❤️</span> by <a class="underline text-blue-700" href="https://gabrielongzm.com" target="_blank" rel="noopener">Gabriel Ong</a>.
  </footer>
</main>