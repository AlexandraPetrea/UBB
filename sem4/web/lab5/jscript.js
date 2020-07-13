function swapTiles(cell1,cell2) {
  var temp = document.getElementById(cell1).className;
  document.getElementById(cell1).className = document.getElementById(cell2).className;
  document.getElementById(cell2).className = temp;
}

function shuffle() {
//Use nested loops to access each cell of the 3x3 grid
for (var row=1;row<=3;row++) { //For each row of the 3x3 grid
   for (var column=1;column<=3;column++) { //For each column in this row
  
    var row2=Math.floor(Math.random()*3 + 1); //Pick a random row from 1 to 3
    var column2=Math.floor(Math.random()*3 + 1); //Pick a random column from 1 to 3
     
    swapTiles("cell"+row+column,"cell"+row2+column2); //Swap the look & feel of both cells
  } 
} 
}

function check(){
    if(document.getElementById("cell"+1+(1)).className=="tile1"){
       if(document.getElementById("cell"+1+(2)).className=="tile2"){
         if(document.getElementById("cell"+1+(3)).className=="tile3"){
           if(document.getElementById("cell"+2+(1)).className=="tile4"){
             if(document.getElementById("cell"+2+(2)).className=="tile5"){
               if(document.getElementById("cell"+2+(3)).className=="tile6"){
                 if(document.getElementById("cell"+3+(1)).className=="tile7"){
                   if(document.getElementById("cell"+3+(2)).className=="tile8"){
                     if(document.getElementById("cell"+3+(3)).className=="tile9")
                          {return true;}
                   }
                 }
               }
             }
           }
         }
       }
       return false;
    }
}
function clickTile(row,column) {
  var cell = document.getElementById("cell"+row+column);
  var tile = cell.className;
  if(check() == true){
      alert("Well done!")
   
  }
  else{
  if (tile!="tile9") { 
       //Checking if white tile on the right
       if (column<3) {
         if ( document.getElementById("cell"+row+(column+1)).className=="tile9") {
           swapTiles("cell"+row+column,"cell"+row+(column+1));
           return;
         }
       }
       //Checking if white tile on the left
       if (column>1) {
         if ( document.getElementById("cell"+row+(column-1)).className=="tile9") {
           swapTiles("cell"+row+column,"cell"+row+(column-1));
           return;
         }
       }
         //Checking if white tile is above
       if (row>1) {
         if ( document.getElementById("cell"+(row-1)+column).className=="tile9") {
           swapTiles("cell"+row+column,"cell"+(row-1)+column);
           return;
         }
       }
       //Checking if white tile is below
       if (row<3) {
         if ( document.getElementById("cell"+(row+1)+column).className=="tile9") {
           swapTiles("cell"+row+column,"cell"+(row+1)+column);
           return;
         }
       } 
  }
  
  }
}
