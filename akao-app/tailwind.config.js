/** @type {import('tailwindcss').Config} */
export default {
  content: [],
  theme: {
    extend: {},
  },
  plugins: [],
}

module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        pastelBlue: '#ccdbfd',
        pastelYellow: '#ffee93',
        pastelPink: '#f9f6f2',
        pastelWhite: '#ffffff'
      }
    }
  },
  plugins: []
}