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
