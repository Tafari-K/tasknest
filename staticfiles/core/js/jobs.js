  document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.querySelector('#job-search');
  const jobCards = document.querySelectorAll('.job-card');

  searchInput.addEventListener('input', () => {
    const query = searchInput.value.toLowerCase();
    jobCards.forEach(card => {
      const title = card.querySelector('h4').textContent.toLowerCase();
      const desc = card.querySelector('p').textContent.toLowerCase();
      card.style.display = (title.includes(query) || desc.includes(query)) ? '' : 'none';
    });
  });
});
