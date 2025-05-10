<script lang="ts">
  export let routes = [];

  let filters = {
    route_name: '',
    location: '',
    country: '',
    route_activity_type: '',
    route_terrain_type: ''
  };

  $: filteredRoutes = routes.filter(route =>
    (!filters.route_name || route.route_name.toLowerCase().includes(filters.route_name.toLowerCase())) &&
    (!filters.location || route.location.toLowerCase().includes(filters.location.toLowerCase())) &&
    (!filters.country || route.country.toLowerCase().includes(filters.country.toLowerCase())) &&
    (!filters.route_activity_type || route.route_activity_type === filters.route_activity_type) &&
    (!filters.route_terrain_type || route.route_terrain_type === filters.route_terrain_type)
  );
</script>

<div class="p-6 bg-white/90 rounded-2xl shadow-lg ring-1 ring-blue-100 max-w-full">
  <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-5 gap-3 mb-6">
    <input
      class="rounded-lg border border-blue-200 bg-[var(--pastel-purple)] px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-300 transition placeholder:text-gray-400"
      placeholder="Route Name"
      bind:value={filters.route_name}
    />
    <input
      class="rounded-lg border border-blue-200 bg-[var(--pastel-purple)] px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-300 transition placeholder:text-gray-400"
      placeholder="Location"
      bind:value={filters.location}
    />
    <input
      class="rounded-lg border border-blue-200 bg-[var(--pastel-purple)] px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-300 transition placeholder:text-gray-400"
      placeholder="Country"
      bind:value={filters.country}
    />
    <select
      class="rounded-lg border border-blue-200 bg-[var(--pastel-purple)] px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-300 transition"
      bind:value={filters.route_activity_type}
    >
      <option value="">All Activities</option>
      <option value="Cycling">Cycling</option>
      <option value="Running">Running</option>
      <option value="Walking">Walking</option>
    </select>
    <select
      class="rounded-lg border border-blue-200 bg-[var(--pastel-purple)] px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-300 transition"
      bind:value={filters.route_terrain_type}
    >
      <option value="">All Terrains</option>
      <option value="Road">Road</option>
      <option value="Mixed">Mixed</option>
      <option value="Off-Road">Off-Road</option>
    </select>
  </div>

  <div class="overflow-x-auto rounded-xl">
    <table class="min-w-full bg-[var(--pastel-blue)] rounded-xl shadow table-auto">
      <thead class="bg-[var(--pastel-yellow)] text-blue-900">
        <tr>
          <th class="px-3 py-2 font-semibold">Name</th>
          <th class="px-3 py-2 font-semibold">Activity</th>
          <th class="px-3 py-2 font-semibold">Location</th>
          <th class="px-3 py-2 font-semibold">Country</th>
          <th class="px-3 py-2 font-semibold">Distance (km)</th>
          <th class="px-3 py-2 font-semibold">Elevation (m)</th>
          <th class="px-3 py-2 font-semibold">Terrain</th>
          <th class="px-3 py-2 font-semibold">Views</th>
          <th class="px-3 py-2 font-semibold">Link</th>
        </tr>
      </thead>
      <tbody>
        {#each filteredRoutes as route, i}
          <tr class="transition-colors duration-200 hover:bg-[var(--pastel-pink)] {i % 2 === 0 ? 'bg-[var(--pastel-green)]' : ''}">
            <td class="px-3 py-2">{route.route_name}</td>
            <td class="px-3 py-2">{route.route_activity_type}</td>
            <td class="px-3 py-2">{route.location}</td>
            <td class="px-3 py-2">{route.country}</td>
            <td class="px-3 py-2">{route.route_distance}</td>
            <td class="px-3 py-2">{route.route_elevation_gain}</td>
            <td class="px-3 py-2">{route.route_terrain_type}</td>
            <td class="px-3 py-2">{route.route_number_views}</td>
            <td class="px-3 py-2">
              <a
                class="text-blue-700 underline hover:text-blue-900 transition"
                href={route.route_url}
                target="_blank"
                rel="noopener"
              >
                View
              </a>
            </td>
          </tr>
        {/each}
        {#if filteredRoutes.length === 0}
          <tr>
            <td class="px-3 py-6 text-center text-gray-400" colspan="9">
              No routes found.
            </td>
          </tr>
        {/if}
      </tbody>
    </table>
  </div>
</div>