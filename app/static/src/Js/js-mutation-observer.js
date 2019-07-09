class AnnouncementsObserver {
  constructor(deleteHandler) {
    this._aList = document.getElementById('aList');
    this._config = {
      childList: true,
      subtree: true
    };
    this._deleteHandler = deleteHandler;
    this._callback = this._callback.bind(this);
  }

  _callback(mutationList, observer) {
    mutationList.forEach((changed) => {
      // Put event listener to the delete buttons
      const closebtns = Array.from(document.querySelectorAll('.announcement__list__item__close'));
      closebtns.forEach((btn) => {
        btn.addEventListener('click', () => {
          // Get the index of the announcement by id
          const index = parseInt(btn.id[btn.id.length - 1]);
          console.log('index', index);
          this._deleteHandler(index);
        });
      });
    });
  }

  createObsAndWatch() {
    this._obs = new MutationObserver(this._callback);
    this._obs.observe(this._aList, this._config);
  }
}
