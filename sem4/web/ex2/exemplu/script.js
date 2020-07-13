$(document).ready(function(){
  $("button").click(function(){
     $('#charNum').text($("mydiv").length);
  });
});

/*
function countChar(val) {
$(function() {
    val = $('.mytable');
 var len = val.value.length;
 var odd = 0, even = 0;
var evenS="", oddS=" ", nou = "";
     for(let i=0; i < len; ++i){
     	if(i % 2 ==0)
          {even++;
          evenS += val.value[i];

        //  evenS = val.value[i];
          }
      	else
 			{odd++;
 			oddS += val.value[i];
 		}
 	}

// $('#even').append(nou);
//  $('#charNum').append(even);
 $('#charNum').text(even);
 //	document.getElementById("charNum").innerHTML = even; 
 	document.getElementById("charOdd").innerHTML = odd; 
 	document.getElementById("odd1").innerHTML = oddS;
 	document.getElementById("even1").innerHTML = evenS;

};

*/
