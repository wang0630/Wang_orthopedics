/* Pagination btn functionality */
class Pagination {
  constructor(announcements, ac_per_page) {
    this._aList = document.getElementById("aList");
    this._ac_per_page = ac_per_page;
    this._announcements = announcements;
  }

  _createListItem(date, content) {
    return `<li class="announcement__list__item"> \
    <span class="announcement__list__item__date"> ${date} </span> \
    <p> ${content} </p> \
    </li>`;
  }

  _createListItems(currentPage) {
    let start = currentPage * this._ac_per_page;
    let end = start + this._ac_per_page > this._announcements.length ? this._announcements.length : start + this._ac_per_page;
    let listr = "";
    for (let i = start; i < end; i++) {
      // console.log(i);
      // console.log(announcements);
      listr = `${listr}${this._createListItem(this._announcements[i].date, this._announcements[i].content)}`;
    }
    return listr;
  }

  _renderOnePage(num) {
    const listr = this._createListItems(num);
    this._aList.innerHTML = listr;
  }

  renderInit() {
    window.addEventListener('load', () => {
      this._renderOnePage(0);
    });
  }

  addPagination() {
    const paginations = Array.from(document.querySelectorAll(".announcement__pagination__item"));
    /* 
      Use arrow function
      So this of this._renderOnePage will refer to the outer scope,
      which is the callback function inside forEach(),
      But the callback function inside forEach() is also an arrow function,
      so the this keyword will refer to the outer scope,
      which is addPagination(), and get the proper this binding
    */

    /* 
      paginations.forEach(function(p) {
        ......
      }, this);

      will also work since we pass this obj into forEach and bind the callback function to it
    */
    paginations.forEach((p) => {
      p.addEventListener("click", () => {
        this._renderOnePage(parseInt(p.innerHTML) - 1);
      })
    });
  }
}
