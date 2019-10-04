class Panel {
  constructor(msg) {
    this._msg = msg;
    // Get all inputs and buttons
    this._inputs = document.querySelectorAll('input');
    this._btns = document.querySelectorAll('button');
  }

  _toggleAttribute(attr) {
    return (element) => {
      element.toggleAttribute(attr);
    }
  }

  showPanel() {
    const body = document.querySelector('body');
    const articles = document.querySelectorAll('article')
    body.style.position = 'relative';
    // Disable article editing and inputs
    this._inputs.forEach(this._toggleAttribute('disabled'));
    this._btns.forEach(this._toggleAttribute('disabled'));
    articles.forEach(this._toggleAttribute('contentEditable'));
    // Show warning panel
    const panel = document.createElement('div');
    panel.id = 'warning-panel';
    const b = document.createElement('button');
    b.type = 'button';
    b.appendChild(document.createTextNode('確定'));
    b.classList.add(...['button', 'button--submit']);
    // Add event listener to the button
    b.addEventListener('click', this._hidePanel.bind(this));
    panel.appendChild(document.createTextNode(this._msg));
    panel.appendChild(b);
    panel.classList.add('warning-panel');
    body.appendChild(panel);
  }


  _hidePanel() {
    const panel = document.getElementById('warning-panel');
    const body = document.querySelector('body');
    const notEditableArticles = document.querySelectorAll('article')
    // Enable all functionalities
    this._inputs.forEach(this._toggleAttribute('disabled'));
    this._btns.forEach(this._toggleAttribute('disabled'));
    notEditableArticles.forEach(this._toggleAttribute('contentEditable'));
    body.removeChild(panel);
  }
}
