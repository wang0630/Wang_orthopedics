// Add eventhandler to photoes and bold buttons
const photoes = document.querySelector('#photoes');
const bold = document.querySelector('#bold');
const submit = document.querySelector('#button-submit');
const article = document.querySelector('.editor__main');
const authorInput = document.querySelector('#author');

const queuedFiles = [];

photoes.addEventListener('change', (e) => {
  if (e.target.files.length > 0) {
    const file = e.target.files[0];
    if (file.size > 2000000) {
      console.log('larger than 2MB');
      return;
    }
    const reader = new FileReader();
    const figure = document.createElement('figure');
    const img = document.createElement('img');
    const figcation = document.createElement('figcaption');
    const text = document.createTextNode('圖片的說明文字');
    const div = document.createElement('div');
    div.style.height = '4rem';
    figcation.appendChild(text);
    figure.appendChild(img);
    figure.appendChild(figcation);
    figure.classList.add('editor__figure');
    img.classList.add('editor__inline-img');
    article.appendChild(figure);
    article.appendChild(div);
    
    reader.onload = (e) => {
      const fileInURL = e.target.result;
      // Push the file dataURL into array
      queuedFiles.push(fileInURL);
      // Change the img tag to the result read
      img.src = e.target.result;
      // Move caret to the div after creating
      makeCaretFocus();
    }
    reader.readAsDataURL(file);
  }
});

article.addEventListener('click', function (e) {
  if (e.target === this && e.target.childNodes[e.target.childNodes.length-1].tagName !== 'DIV') {
    // if there is no DIV element, add one
    const div = document.createElement('div');
    div.style.height = '4rem';
    this.appendChild(div);
    // Move caret to the div after creating
    makeCaretFocus();
  }
});


function makeCaretFocus () {
  // Create range and selection object in order to move caret to the next div
  const range = document.createRange();
  const selection = window.getSelection();
  // Start the range from the last child node(length - 1)
  // which is the 'div' tag inserted
  range.setStart(article, article.childNodes.length - 1);
  // Make the endpoint of the range the same as the starting point
  range.collapse(true);
  selection.removeAllRanges();
  // Move caret to the range, and the range now is a point pointed to the div tag
  selection.addRange(range);
}

function addSubmitHandler (ip, editorPostLimit) {
  // Make post request to create a post
  submit.addEventListener('click', async () => {
    try {
      // Check if the author name and article is empty
      if (authorInput && article.textContent.length > editorPostLimit) {
        const completeIp = `${ip}/columns`;
        // Remove dataURL from img src
        const parsedhtml = traverseRemoveImg();
        data = {
          author: authorInput.value,
          base64s: queuedFiles,
          content: parsedhtml, 
        };
        const res = await axios.post(completeIp, data);
        console.log(res);
      } else {
        // show error panel
      }
    } catch (e) {
      console.log(e);
    }
  });
}

function traverseRemoveImg() {
  const html = article.innerHTML;
  const re = /<img[^>]*>/gi;
  return html.replace(re, '<img>');
}
