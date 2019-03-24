const reset = document.querySelector('.rese');
reset.addEventListener('click', () => {
  // alert('ok');
  document.querySelector('.sign-for-users').style.display = 'inline-block';
  document.querySelector('.sign-for-actors').style.display = 'inline-block';
  document.querySelector('.who-r-u').style.display = 'block';
  document.querySelector('.for-actors').style.display = 'none';
  document.querySelector('.sign-form').style.display = 'none';
  reset.style.display = 'none';
});

const user = document.querySelector('.sign-for-users');
user.addEventListener('click', () => {
  document.querySelector('.sign-for-actors').style.display = 'none';
  document.querySelector('.who-r-u').style.display = 'none';
  document.querySelector('.sign-form').style.display = 'flex';
  reset.style.display = 'inline-block';
  user.style.display = 'none';
});

const actor = document.querySelector('.sign-for-actors');
actor.addEventListener('click', () => {
  document.querySelector('.sign-for-users').style.display = 'none';
  document.querySelector('.who-r-u').style.display = 'none';
  document.querySelector('.for-actors').style.display = 'flex';
  reset.style.display = 'inline-block';
  actor.style.display = 'none';
});
