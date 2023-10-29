const colors = require('tailwindcss/colors');

module.exports = {
  content: ['./src/renderer/**/*.{js,jsx,ts,tsx,ejs}'],
  darkMode: 'class', // or 'media' or 'class'
  variants: {},
  plugins: [require('daisyui')],
  daisyui: {
    themes: ['cupcake','light', 'night', 'dark'],
  },
};
