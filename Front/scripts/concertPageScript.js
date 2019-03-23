document.querySelector('.add-poll').addEventListener('click', () => {
  const form = document.querySelector('.add-poll-form');
  if (form.style.display === 'block') {
    form.style.display = 'none';
  } else {
    form.style.display = 'block';
  }
});