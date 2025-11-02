document.addEventListener('DOMContentLoaded', () => {
  const toggleIcons = document.querySelectorAll('.toggle-password');

  toggleIcons.forEach(icon => {
    icon.addEventListener('click', () => {
      const targetId = icon.getAttribute('data-target');
      const input = document.getElementById(targetId);
      const iconEl = icon.querySelector('i');

      if (input.type === 'password') {
        input.type = 'text';
        iconEl.classList.remove('fa-eye');
        iconEl.classList.add('fa-eye-slash');
      } else {
        input.type = 'password';
        iconEl.classList.remove('fa-eye-slash');
        iconEl.classList.add('fa-eye');
      }
    });
  });
});

document.addEventListener('DOMContentLoaded', function () {
  const roleField = document.getElementById('id_role');
  const tradeOptions = document.getElementById('trade-options');

  function toggleTradeOptions() {
    if (roleField.value === 'tradesman') {
      tradeOptions.style.display = 'block';
    } else {
      tradeOptions.style.display = 'none';
    }
  }

  // Run on load
  toggleTradeOptions();

  // Run on change
  roleField.addEventListener('change', toggleTradeOptions);
});
