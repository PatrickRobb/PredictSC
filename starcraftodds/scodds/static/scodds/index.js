//const pastRows = document.querySelectorAll(".content-table").getElementsByTagName("tbody").getElementsByTagName("tr");
//const pastRows = document.getElementsByTagName("tbody").getElementsByTagName('tr');

// var rows = document.getElementsByTagName("tr") ;
// for (var i=0; i<rows.length; i++) {
//     rows[i].style.backgroundColor = "red";
// }

lightGreen = "#A7F1A7"
lightRed = "#FFCCCB"


document.querySelectorAll('table').forEach(table =>{
    rows = table.rows;
    for (let i=1; i<rows.length; i++){
        if (parseFloat(rows[i].lastElementChild.textContent) > 0){
            rows[i].style.backgroundColor = lightGreen;
        }
        else {rows[i].style.backgroundColor = lightRed;}
    }
})

// const pastRows = document.querySelector('.past').rows;

// for (let i=1; i<pastRows.length; i++){
//     if (parseFloat(pastRows[i].lastElementChild.textContent) > 0){
//         pastRows[i].style.backgroundColor = lightGreen;
//     }
//     else {pastRows[i].style.backgroundColor = lightRed;}
// }

// function colorTable(table){
//     for (let i=1; i<pastRows.length; i++){
//         if (parseFloat(pastRows[i].lastElementChild.textContent) > 0){
//             pastRows[i].style.backgroundColor = lightGreen;
//         }
//         else {pastRows[i].style.backgroundColor = lightRed;}
//     }
// }

// pastRows.forEach(row =>{
//     row.style.backgroundColor='green';
//     console.log("heyo");
// })


// pastRows.forEach(row =>{
//     var col_val = $(this).find("td:eq(1)").text();
//     if (col_val > 0){
//         row.style.backgroundColor='green';
//         console.log("Green");
//     }
//     else row.style.backgroundColor='red';
//     console.log("heyo");
// })