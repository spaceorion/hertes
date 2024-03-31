const toggleSwitch = document.getElementById('toggle');
const currentTheme = localStorage.getItem('theme');

if (currentTheme) {
  if (currentTheme === 'dark') {
    toggleSwitch.checked = true;
    document.body.classList.add('dark');
  }
}

function switchTheme(e) {
  if (e.target.checked) {
    localStorage.setItem('theme', 'dark');
    document.body.classList.add('dark');
  } else {
    localStorage.setItem('theme', 'light');
    document.body.classList.remove('dark');
  }    
}

toggleSwitch.addEventListener('change', switchTheme, false);