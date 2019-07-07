class AnnouncementsObserver {
  constructor() {
    this._aList = document.getElementById('aList');
    this._config = {
      childList: true,
      subtree: true
    };
    this._itemCount = 0;

    this._callback = this._callback.bind(this);
  }

  _callback(mutationList, observer) {
    mutationList.forEach((changed) => {
      this._itemCount++;
      console.log(changed);
      if (this._itemCount == 5) {
        console.log('should stop listening');
      }
    });
  }

  createObsAndWatch() {
    this._obs = new MutationObserver(this._callback);
    this._obs.observe(this._aList, this._config);
  }
}
