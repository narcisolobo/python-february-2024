/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./marvel/templates/**/*.html"],
  theme: {
    extend: {},
    container: {
      center: true,
    },
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["synthwave"],
  },
};
