$(document).ready(function () {
    const display = $('#time');
    const workSignal = $('#workSignal');
    const restSignal = $('#restSignal');
    const play_btn = $('.play');
    const pause_btn = $('.pause');
    const reset_btn = $('.reset');
    let work = true;
    let workDuration = 25 * 60;
    let restDuration = 5 * 60;
    let value = 0;
    let chip = 100 / workDuration;
    let isPaused = true;
    let isReseted = false;
    const resetProgress = function () {
        $('.progress-bar').css('width', '0%');
    };

    // timer function
    function startTimer(duration, display) {
        let timer = duration,
            minutes, seconds;
        const refresh = setInterval(function () {
            minutes = parseInt(timer / 60, 10);
            seconds = parseInt(timer % 60, 10);

            minutes = minutes < 10 ? "0" + minutes : minutes;
            seconds = seconds < 10 ? "0" + seconds : seconds;

            display.text(minutes + " : " + seconds);

            if (!isPaused && !isReseted) {
                value += chip;
                $('.progress-bar').css('width', value + '%');
                if (--timer < 0) {
                    clearInterval(refresh);
                    const music = $("#over_music")[0];
                    music.play();
                    if (work === true) {
                        display.text("Rest!");
                        resetProgress();
                        workSignal.css('background', '');
                        restSignal.css('background', 'orange');
                        value = 0;
                        chip = 100 / restDuration;
                        startTimer(restDuration, display);
                        work = false;
                    } else {
                        display.text("Work!");
                        resetProgress();
                        workSignal.css('background', 'orange');
                        restSignal.css('background', '');
                        value = 0;
                        chip = 100 / workDuration;
                        startTimer(workDuration, display);
                        work = true;
                    }

                }
            } else if (isReseted) {
                resetProgress();
                clearInterval(refresh);
            }
        }, 1000);
    }

    // start timer
    startTimer(workDuration, display);

    // adjust session duration
    $('#workMore').on('click', function () {
        workDuration = (parseInt($('#workTime').html(), 10) + 1) * 60;
        $('#workTime').html(workDuration / 60);
    });

    $('#workLess').on('click', function () {
        workDuration = (parseInt($('#workTime').html(), 10) - 1) * 60;
        $('#workTime').html(workDuration / 60);
    });

    $('#restMore').on('click', function () {
        restDuration = (parseInt($('#restTime').html(), 10) + 1) * 60;
        $('#restTime').html(restDuration / 60);
    });

    $('#restLess').on('click', function () {
        restDuration = (parseInt($('#restTime').html(), 10) - 1) * 60;
        $('#restTime').html(restDuration / 60);
    });

    play_btn.click(function () {
        play_btn.attr("disabled", "disabled")
        pause_btn.removeAttr("disabled");
        if (isPaused) {
            isPaused = false;
        }
        if (isReseted) {
            isReseted = false;
            resetProgress();
            value = 0;
            chip = 100 / workDuration;
            startTimer(workDuration, display);
        }
    });
    pause_btn.click(function () {
        pause_btn.attr("disabled", "disabled")
        play_btn.removeAttr("disabled");
        if (isPaused) {
            isPaused = false;
        } else if (isReseted) {
            isPaused = true;
            isReseted = false;
        } else {
            isPaused = true;
        }
    });
    reset_btn.click(function () {
        pause_btn.removeAttr("disabled");
        play_btn.removeAttr("disabled");
        isReseted = true;
        workSignal.css('background', 'orange');
        restSignal.css('background', '');
    });
})
