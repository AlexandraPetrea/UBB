$(document).ready(function() {
    var playing = false;
    var score = 0;
    var fruits = ['apple', 'banana', 'cherries', 'grapes',
        'mango', 'orange', 'peach', 'pear', 'watermelon'];
    
    $("#startreset").click(function() {
//        console.log("1");
       if (playing == true) {
           location.reload();
       } else {
           playing = true;
           score = 0;
           $("#scorevalue").html(score);
           $("#gameOver").hide();
           $("#startreset").html("Restart");
           startAction();
//           checkIfGameOver();
       }
    });
    
    $("#fruit1").click(function() {
        score += 1;
        console.log(score);
//        alert(1);
        $("#scorevalue").html(score);
		$("#fruit1").hide();
        if (!checkIfGameOver()) {
            setTimeout(startAction, 1000 + Math.round(4000 * Math.random()));
        }
    });
    
    function checkIfGameOver() {
        if (score == 10) {
           playing = false;
           $("#startreset").show();
           $("#gameOver").show();
           $("#gameOver").html('<p>You win!</p> Your score is ' + score + '.</p>');
           $("#fruit1").hide();
           return true;
        }
        return false;
    }
    
    function chooseImage() {
        $("#fruit1").attr('src', 'img/' + fruits[Math.round(8 * Math.random())] + '.png');
    }
    
    function choosePosition() {
        $("#fruit1").css({
            'left': Math.round(550 * Math.random()),
            'top': Math.round(300 * Math.random())
        });
    }
    
    function startAction() {
        $("#fruit1").show();
        chooseImage();
        choosePosition();
        if (!checkIfGameOver()) {
            setTimeout(function() {
                $("#fruit1").hide();
                setTimeout(startAction, 1000 + Math.round(4000 * Math.random()));
            }, 1000 + Math.round(4000 * Math.random()));
        }
    }
});