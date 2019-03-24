document.querySelector('.add-poll').addEventListener('click', () => {
  const form = document.querySelector('.add-poll-form');
  if (form.style.display === 'block') {
    form.style.display = 'none';
  } else {
    form.style.display = 'block';
  }
});

// document.querySelector('.on-email').addEventListener('click', () => {
//   const ul = document.querySelector('.list-of-concerts');
//   if (ul.style.display === 'flex') {
//     ul.style.display = 'none';
//     document.querySelector('.on-email').style.marginLeft = 'auto';
//   } else {
//     document.querySelector('.on-email').style.marginLeft = '0px';
//     ul.style.marginLeft = 'auto';tes
//     ul.style.display = 'flex';
//   }
// });

document.querySelector('.subscribe').addEventListener('click', () => {
    let res = prompt('Согласны ли вы на отправку вам сообщений во время концерта, которые будут уведомлять о флешмобах?', 79999999999);
    if (res !== null) {
      let form = document.querySelector('.subsForm');
      form.querySelector('input[type="text"]').value = res;
      form.submit();

    }
});

document.querySelector('.join').addEventListener('click', () => {
  let res = prompt('Введите код доступа', '12345abc');
    if (res !== null) {
      let form = document.querySelector('.joinForm');
      form.querySelector('input[type="text"]').value = res;
      form.submit();

    }
});