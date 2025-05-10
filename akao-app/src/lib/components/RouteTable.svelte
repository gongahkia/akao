<script lang="ts">
  export let routes = [];

  let filters = {
    route_name: '',
    location: '',
    country: '',
    route_activity_type: '',
    route_terrain_type: ''
  };

  // Filter logic
  $: filteredRoutes = routes.filter(route =>
    (!filters.route_name || route.route_name.toLowerCase().includes(filters.route_name.toLowerCase())) &&
    (!filters.location || route.location.toLowerCase().includes(filters.location.toLowerCase())) &&
    (!filters.country || route.country.toLowerCase().includes(filters.country.toLowerCase())) &&
    (!filters.route_activity_type || route.route_activity_type === filters.route_activity_type) &&
    (!filters.route_terrain_type || route.route_terrain_type === filters.route_terrain_type)
  );
</script>

<div class="p-4 bg-pastelWhite rounded shadow">
  <div class="grid grid-cols-2 md:grid-cols-5 gap-2 mb-4">
    <input class="input input-bordered" placeholder="Route Name" bind:value={filters.route_name} />
    <input class="input input-bordered" placeholder="Location" bind:value={filters.location} />
    <input class="input input-bordered" placeholder="Country" bind:value={filters.country} />
    <select class="input input-bordered" bind:value={filters.route_activity_type}>
      <option value="">All Activities</option>
      <option value="Cycling">Cycling</option>
      <option value="Running">Running</option>
      <option value="Walking">Walking</option>
    </select>
    <select class="input input-bordered" bind:value={filters.route_terrain_type}>
      <option value="">All Terrains</option>
      <option value="Road">Road</option>
      <option value="Mixed">Mixed</option>
      <option value="Off-Road">Off-Road</option>
    </select>
  </div>
  <table class="min-w-full table-auto bg-pastelBlue rounded">
    <thead class="bg-pastelYellow">
      <tr>
        <th class="px-2 py-1">Name</th>
        <th class="px-2 py-1">Activity</th>
        <th class="px-2 py-1">Location</th>
        <th class="px-2 py-1">Distance (km)</th>
        <th class="px-2 py-1">Elevation (m)</th>
        <th class="px-2 py-1">Terrain</th>
        <th class="px-2 py-1">Views</th>
        <th class="px-2 py-1">Link</th>
      </tr>
    </thead>
    <tbody>
      {#each filteredRoutes as route}
        <tr class="hover:bg-pastelPink">
          <td class="px-2 py-1">{route.route_name}</td>
          <td class="px-2 py-1">{route.route_activity_type}</td>
          <td class="px-2 py-1">{route.location}</td>
          <td class="px-2 py-1">{route.route_distance}</td>
          <td class="px-2 py-1">{route.route_elevation_gain}</td>
          <td class="px-2 py-1">{route.route_terrain_type}</td>
          <td class="px-2 py-1">{route.route_number_views}</td>
          <td class="px-2 py-1">
            <a class="text-blue-600 underline" href={route.route_url} target="_blank">View</a>
          </td>
        </tr>
      {/each}
    </tbody>
  </table>
</div>