document.querySelector('.add-poll').addEventListener('click', () => {
  const form = document.querySelector('.add-poll-form');
  if (form.style.display === 'block') {
    form.style.display = 'none';
  } else {
    form.style.display = 'block';
  }
});

document.querySelector('.on-email').addEventListener('click', () => {
  const ul = document.querySelector('.list-of-concerts');
  if (ul.style.display === 'flex') {
    ul.style.display = 'none';
    document.querySelector('.on-email').style.marginLeft = 'auto';
  } else {
    document.querySelector('.on-email').style.marginLeft = '0px';
    ul.style.marginLeft = 'auto';
    ul.style.display = 'flex';
  }
});
