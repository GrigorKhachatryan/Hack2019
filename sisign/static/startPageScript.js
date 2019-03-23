const user = document.querySelector('.sign-for-users');
user.addEventListener('click', () => {
  document.querySelector('.sign-for-actors').style.display = 'none';
  document.querySelector('.who-r-u').style.display = 'none';
  document.querySelector('.sign-form').style.display = 'flex';
  user.style.display = 'none';
});

const actor = document.querySelector('.sign-for-actors');
actor.addEventListener('click', () => {
  document.querySelector('.sign-for-users').style.display = 'none';
  document.querySelector('.who-r-u').style.display = 'none';
  document.querySelector('.for-actors').style.display = 'flex';
  actor.style.display = 'none';
});