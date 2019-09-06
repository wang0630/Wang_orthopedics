class LazyLoading {
  constructor() {
    this.images = Array.from(document.querySelectorAll('source,img'));
    this._config = {
      // If the image gets within 50px in the Y axis, start the download.
      // rootMargin: '50px 0px',
      threshold: 0.3
    };
    this._OnIntersecting = this._OnIntersecting.bind(this);
  }

  createObserver() {
    // If no support, load image immediately
    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver(this._OnIntersecting, this._config);
      this.images.forEach(img => observer.observe(img));
    } else {
      this.images.forEach(img => this._loadImage(img));
    }
  }

  _loadImage(entry) {
    if (entry.dataset && entry.dataset.src) {
      // Replace the src
      entry.src = entry.dataset.src;
    } else if(entry.dataset && entry.dataset.srcset) {
      // Replace the src
      entry.srcset = entry.dataset.srcset;
    }
  }

  _OnIntersecting(entries, observer) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        console.log(entry.target);
        // Stop observing the img
        // entry.target points to the real DOM element
        observer.unobserve(entry.target);
        // Load the image
        this._loadImage(entry.target);
      }
    });
  }
};
