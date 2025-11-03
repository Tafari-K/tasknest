
document.getElementById('jobSearch').addEventListener('keyup', function () {
    const term = this.value.toLowerCase();
    const cards = document.querySelectorAll('.job-card');

    cards.forEach(card => {
      const text = card.textContent.toLowerCase();
      card.style.display = text.includes(term) ? 'block' : 'none';
    });
  });
