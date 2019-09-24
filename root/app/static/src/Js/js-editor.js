// Add eventhandler to photoes and bold buttons
const photoes = document.querySelector('#photoes');
const bold = document.querySelector('#bold');
const article = document.querySelector('.editor__main');

const queuedFiles = [];

photoes.addEventListener('change', (e) => {
  if (e.target.files.length > 0) {
    const file = e.target.files[0];
    if (file.size > 200000) {
      console.log('larger than 2MB');
      return;
    }
    const reader = new FileReader();
    const figure = document.createElement('figure');
    const img = document.createElement('img');
    const figcation = document.createElement('figcaption');
    const text = document.createTextNode('圖片的說明文字');
    const p = document.createElement('p');
    p.style.height = '4rem';
    figcation.appendChild(text);
    figure.appendChild(img);
    figure.appendChild(figcation);
    figure.classList.add('editor__figure');
    article.appendChild(figure);
    article.appendChild(p);
    
    reader.onload = (e) => {
      const fileInURL = e.target.result;
      // Push the file dataURL into array
      queuedFiles.push(fileInURL);
      // Change the img tag to the result read
      img.src = e.target.result;
      
      // Create range and selection object in order to move caret to the next p
      const range = document.createRange();
      const selection = window.getSelection();
      // Start the range from the last child node(length - 1)
      // which is the 'p' tag inserted
      range.setStart(article, article.childNodes.length - 1);
      // Make the endpoint of the range the same as the starting point
      range.collapse(true);
      selection.removeAllRanges();
      // Move caret to the range, and the range now is a point pointed to the p tag
      selection.addRange(range);
    }
    reader.readAsDataURL(file);
  }
});
