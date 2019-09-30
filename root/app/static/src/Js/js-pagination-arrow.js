const rightArrow = document.querySelector('#next');
const leftArrow = document.querySelector('#previous');
console.log(leftArrow)
function movePageFactory(offset) {
  const currentURL = new URL(window.location.pathname, window.location.protocol + window.location.host);
  const params = new URLSearchParams(window.location.search);
  const page = params.get('page') ? parseInt(params.get('page')) : 1;

  return () => {
    targetPage = page + offset <= 0 ? 1 : page + offset;
    console.log(targetPage);
    window.location = `${currentURL.href}?page=${targetPage}`;
  }
}

rightArrow.addEventListener('click', movePageFactory(1));
leftArrow.addEventListener('click', movePageFactory(-1));
