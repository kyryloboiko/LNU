document.addEventListener('DOMContentLoaded', function() {
    const nightModeCheckbox = document.getElementById('night-mode-checkbox');
    const sunIcon = document.querySelector('.fa-sun');
    const moonIcon = document.querySelector('.fa-moon');
  
    function applyNightMode() {
      const isNightMode = localStorage.getItem('nightMode');
      if (isNightMode === 'enabled') {
        document.body.classList.add('night-mode');
        nightModeCheckbox.checked = true;
        toggleIcons();
      }
    }
  
    function toggleNightMode() {
      if (nightModeCheckbox.checked) {
        document.body.classList.add('night-mode');
        localStorage.setItem('nightMode', 'enabled');
      } else {
        document.body.classList.remove('night-mode');
        localStorage.removeItem('nightMode');
      }
      toggleIcons(); // Перемістили виклик зміни іконок звідси
    }
  
    function toggleIcons() {
      sunIcon.classList.toggle('hidden');
      moonIcon.classList.toggle('hidden');
    }
  
    nightModeCheckbox.addEventListener('change', toggleNightMode);
    applyNightMode();
  });
  