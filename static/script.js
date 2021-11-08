//define variables
var upButton = $('.upButton');
var rightButton = $('.rightButton');
var downButton = $('.downButton');
var leftButton = $('.leftButton');
var stringUp = $('.upStringButton');
var stringDown = $('.downStringButton');

upButton.mousedown(function(){
    $.ajax({
        url: "/vertical_up",
        type: "post",
        success: function(response) {
            console.log(response);
        }
    });
});
downButton.mousedown(function(){
    $.ajax({
        url: "/vertical_down",
        type: "post",
        success: function(response) {
            console.log(response);
        }
    });
});
rightButton.mousedown(function(){
    $.ajax({
        url: "/horizontal_right",
        type: "post",
        success: function(response) {
            console.log(response);
        }
    });
});
leftButton.mousedown(function(){
    $.ajax({
        url: "/horizontal_left",
        type: "post",
        success: function(response) {
            console.log(response);
        }
    });
});
stringUp.mousedown(function(){
    $.ajax({
        url: "/string_up",
        type: "post",
        success: function(response) {
            console.log(response);
        }
    });
});
stringDown.mousedown(function(){
    $.ajax({
        url: "/string_down",
        type: "post",
        success: function(response) {
            console.log(response);
        }
    });
});

//===================Leaderboard stuff======================



//===================Timer Stuff============================
$('.startTimer').on('click', startTimer);

$('.oneMinute').on('click', function(){
    $('.timer').html("<span class = 'minutes'>0</span>:<span class = 'seconds'>12</span>");
    $('.timer').css('color', 'white');
})
$('.twoMinute').on('click', function(){
    $('.timer').html("<span class = 'minutes'>2</span>:<span class = 'seconds'>00</span>");;
    $('.timer').css('color', 'white');
})
$('.threeMinute').on('click', function(){
    $('.timer').html("<span class = 'minutes'>3</span>:<span class = 'seconds'>00</span>");
    $('.timer').css('color', 'white');
})

function startTimer(){
    //hide time change buttons
    $('.oneMinute').css('display', 'none');
    $('.twoMinute').css('display', 'none');
    $('.threeMinute').css('display', 'none');

    //get minute and second html values
    var minutes = $('.minutes').html();
    var seconds = $('.seconds').html();
    console.log("seconds "+seconds);
    console.log("minutes "+minutes);

    var fraction = 100/((minutes * 60)+(seconds * 1));

    //start countdown
    var countdown = setInterval(function() {

        if((minutes != 0 || seconds != 0) && seconds <= 60){
            if(seconds == 00 && minutes >0){
                minutes--;
                $('.seconds').html("60");
                seconds = $('.seconds').html();
            }
            //subtract a second
            seconds--;
            if(seconds <= 9){
                $('.minutes').html(minutes);
                $('.seconds').html("0"+seconds);
            }else{
                $('.minutes').html(minutes);
                $('.seconds').html(seconds);
            }
            if(seconds <= 10 && minutes == 0){
                $('.timer').css('color', 'orange');
            }
            if(seconds <= 5 && minutes == 0){
                $('.timer').css('color', 'red');
            }
        }
        else if (seconds <= 0 && minutes == 0){
            clearInterval(countdown);

            $('.oneMinute').css('display', 'block');
            $('.twoMinute').css('display', 'block');
            $('.threeMinute').css('display', 'block');
        }
        //get total seconds
        var secondsLeft = (minutes * 60) + (seconds * 1);
        //how high up the background color is
        //when it gets to top time is up
        var colorHeight = 100 - (fraction * secondsLeft);
        $('.timerColor').css('height', colorHeight + '%');

    }, 1000);
}
