// document.write('Welcome to LD Notes');
// showNotes();
// var notes = document.getElementById('notes');
// var addTxt = document.getElementById('addText');
// let addBtn = document.getElementById('addBtn');
// console.log('this is addtxt', addTxt);

// let curNotes = localStorage.getItem('notes');

// console.log('this is curNotes.. ',curNotes)
// if (curNotes === null) {
//     var currentNotes = [];
//     console.log('null')
//     notes.innerHTML = `<h5 class='mx-5 pl-5'>Nothing to Show here !! Use Add Note Section above to Add Note.</h5>`;
// }
// else {
//     var currentNotes = JSON.parse(curNotes);
//     console.log('notnull');
// }


// addBtn.addEventListener('click', function () {
//     var c;
//     console.log('this is adtxt', addTxt)
//     var txt = addTxt.value;
//     console.log('Text = .', txt, '.');
//     if (txt === '') {
//         c = confirm(`Your Note is Empty !!
// Do You Still Want to Add It ???`);
//         if (c == true) {
//             currentNotes.push(txt);
//             console.log("CurrentNotes array going to localstorage: ", currentNotes);

//             localStorage.setItem('notes', JSON.stringify(currentNotes));

//             console.log("CurrentNotes array converted to str gone to localstorage: ", currentNotes);
//             showNotes();
//         }
//     }
//     else {
//         currentNotes.push(txt);
//         console.log("CurrentNotes array going to localstorage: ", currentNotes);

//         localStorage.setItem('notes', JSON.stringify(currentNotes));

//         console.log("CurrentNotes array converted to str gone to localstorage: ", currentNotes);
//         showNotes();
//     }
//     console.log("c= ", c);

// })

// function showNotes() {
//     console.log("This is showNotes")
//     console.log('this is currentNotes..',currentNotes)
//     if(currentNotes=='undefined'){
//         enterNotes.innerHTML += `<div class="spinner-grow" role="status">
//         <span class="sr-only">Loading...</span>
//       </div>
//       `
//     }
//     let command = ``;
//     for (let i in currentNotes) {

//         console.log(currentNotes[i]);
//         command += `
//         <div class="notecard card my-2 mx-2" >
// <div class="card-body">
//   <h4 class="card-title">Note ${Number(i) + 1}</h4> 
// <div class="container-fluid card_body">
//   <pre><p class="card-text my-3">${currentNotes[i]}</p></pre>
//   </div>
//   <button onclick='deleteNote(${Number(i)})' class="btn btn-primary my-2" id="delBtn">Delete Note</button>
// </div>
// </div>`;
//         notes.innerHTML = command;
//     }
// }

// function deleteNote(id) {
//     curNotes = localStorage.getItem('notes');
//     xyz=JSON.parse(curNotes);
//     console.log('Going to delete...');
//     console.log("this is curnotes json.parse..",xyz);
//     console.log("this is curnotes length ..", xyz.length);

//     if (xyz.length == 1) {
//         console.log('null');
//         currentNotes.splice(id, 1);
//         localStorage.removeItem('notes');
//         enterNotes = document.getElementById('enterNotes');
//         enterNotes.innerHTML += `<div class="spinner-grow" role="status">
//         <span class="sr-only">Loading...</span>
//       </div>
//       `
//         notes.innerHTML = `<h5 class='mx-5 pl-5'>Nothing to Show here !! Use Add Note Section above to Add Note.</h5>`;
//     }
//     else {
//         console.log('notnull');
//         console.log("this is id",id);
//         currentNotes.splice(id, 1);
//         localStorage.setItem('notes', JSON.stringify(currentNotes));
//     }
//     console.log("this is currentNotes..",currentNotes)
//     showNotes();
// }
// showNotes();