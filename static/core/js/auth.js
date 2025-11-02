function togglePassword(inputId, toggleIcon) {
    const input = document.getElementById(inputId);
    const icon = toggleIcon.querySelector('i');

    if (input.type === "password") {
        input.type = "text";
        icon.classList.remove("fa-eye");
        icon.classList.add("fa-eye-slash");
    } else {
        input.type = "password";
        icon.classList.remove("fa-eye-slash");
        icon.classList.add("fa-eye");
    }
}


document.addEventListener("DOMContentLoaded", function () {
  const toggles = document.querySelectorAll(".toggle-password");

  toggles.forEach(toggle => {
    toggle.addEventListener("click", function () {
      const inputId = this.getAttribute("data-target");
      const input = document.getElementById(inputId);

      if (input) {
        const type = input.type === "password" ? "text" : "password";
        input.type = type;

        // Toggle the eye icon
        const icon = this.querySelector("i");
        if (icon) {
          icon.classList.toggle("fa-eye");
          icon.classList.toggle("fa-eye-slash");
        }
      }
    });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const roleSelect = document.getElementById("id_role");
  const tradeField = document.getElementById("trade-field");

  function toggleTradeField() {
    if (roleSelect && tradeField) {
      tradeField.style.display = roleSelect.value === "tradesman" ? "block" : "none";
    }
  }

  if (roleSelect) {
    toggleTradeField();
    roleSelect.addEventListener("change", toggleTradeField);
  }
});
