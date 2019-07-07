class AnnouncementsObserver {
  constructor() {
    this._aList = document.getElementById('aList');
    this._config = {
      childList: true,
      subtree: true
    };
    this._callback = this._callback.bind(this);
  }

  _callback(mutationList, observer) {
    mutationList.forEach((changed) => {
      console.log(changed);
    });
  }

  createObsAndWatch() {
    this._obs = new MutationObserver(this._callback);
    this._obs.observe(this._aList, this._config);
  }
}
