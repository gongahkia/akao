<script lang="ts">
  import { onMount } from 'svelte';
  import RouteTable from '$lib/components/RouteTable.svelte';
  let routes = [];
  let randomRoute = null;

  onMount(async () => {
    const res = await fetch('/routes.json');
    routes = await res.json();
  });

  function findRandomRoute() {
    if (routes.length > 0) {
      const randomIndex = Math.floor(Math.random() * routes.length);
      randomRoute = routes[randomIndex];
      alert(`Random Route: ${randomRoute.name}`);
    }
  }
</script>

<main class="min-h-screen bg-pastelBlue flex flex-col p-4">
  <h1 class="text-3xl font-bold text-center my-8 text-blue-900">Akao</h1>
  <p class="text-center mb-4">Find routes in Singapore</p>
  <div class="flex justify-center mb-6">
    <button 
      class="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded shadow transition duration-300"
      on:click={findRandomRoute}
    >
      Find Random Route
    </button>
  </div>
  <RouteTable {routes} />
  <footer class="mt-auto py-4 text-center bg-pastelYellow text-gray-700">
    Made with <span aria-label="heart" role="img">❤️</span> by <a class="underline text-blue-700" href="https://gabrielongzm.com" target="_blank" rel="noopener">Gabriel Ong</a>.
  </footer>
</main>