/* Pagination btn functionality */
class Pagination {
  constructor(ac_per_page) {
    this.aList = document.getElementById("aList");
    this.ac_per_page = ac_per_page;
  }

  createListItem(date, content) {
    return `<li class="announcement__list__item"> \
    <span class="announcement__list__item__date"> ${date} </span> \
    <p> ${content} </p> \
    </li>`;
  }

  createListItems(currentPage) {
    let start = currentPage * ac_per_page;
    let end = start + ac_per_page > announcements.length ? announcements.length : start + ac_per_page;
    let listr = "";
    console.log(end);
    for (let i = start; i < end; i++) {
    // console.log(i);
    // console.log(announcements);
    listr = `${listr}${createListItem(announcements[i].date, announcements[i].content)}`;
    }
    return listr;
  }

}


// Create one item
const createListItem = (date, content) => `<li class="announcement__list__item"> \
<span class="announcement__list__item__date"> ${date} </span> \
<p> ${content} </p> \
</li>`;
// Pass in the currently active page number to create the proper announcements
const createListItems = (currentPage) => {
let start = currentPage * ac_per_page;
let end = start + ac_per_page > announcements.length ? announcements.length : start + ac_per_page;
let listr = "";
console.log(end);
for (let i = start; i < end; i++) {
// console.log(i);
// console.log(announcements);
listr = `${listr}${createListItem(announcements[i].date, announcements[i].content)}`;
}
return listr;
}
// ------------ Load the first 4 announcements(if any) -------------
window.addEventListener("load", () => {
let aList = document.getElementById("aList");
let listr = createListItems(0);
// Insert the newly created element string
aList.innerHTML = listr;
});
// ----------------------------------------------------------


// ------- Add eventListener to every pagination btn ----------
let paginations = Array.from(document.querySelectorAll(".announcement__pagination__item"));
// console.log(paginations)
paginations.forEach((p, index) => {
p.addEventListener("click", () => {
let aList = document.getElementById("aList");
let listr = createListItems(parseInt(p.innerHTML) - 1);
// Insert the newly created element string
aList.innerHTML = listr;
});
})
// ------------------------------------------------------------
