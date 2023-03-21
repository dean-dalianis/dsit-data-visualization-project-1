$(document).ready(function () {
    let timeRemaining = 30;
    let score = 0;
    let gameTimer;
    let shapeInterval;

    $('#start-button').click(function () {
        if (gameTimer) {
            clearInterval(gameTimer);
            gameTimer = null;
        }
        if (shapeInterval) {
            clearInterval(shapeInterval);
            shapeInterval = null;
        }
        $('.game-shape').remove();
        startGame();
    });

    function startGame() {
        timeRemaining = 30;
        score = 0;
        $('#score').text(score);
        $('#time-remaining').text(timeRemaining);

        // Start the game timer
        gameTimer = setInterval(function () {
            timeRemaining--;
            $('#time-remaining').text(timeRemaining);
            if (timeRemaining === 0) {
                clearInterval(gameTimer);
                gameTimer = null;
                clearInterval(shapeInterval);
                shapeInterval = null;
                $('.game-shape').remove();
            }
        }, 1000);

        shapeInterval = setInterval(function () {
            const shapeTypes = ['circle', 'square', 'triangle'];
            const shapeType = shapeTypes[Math.floor(Math.random() * shapeTypes.length)];
            const shapeColors = ['#008080', '#FFD700', '#FF1493', '#32CD32', '#1E90FF', '#FF00FF'];
            const shapeColor = shapeColors[Math.floor(Math.random() * shapeColors.length)];
            const shapeSizes = [50, 80, 100, 35, 40, 45, 55, 65, 120];
            const shapeSize = shapeSizes[Math.floor(Math.random() * shapeSizes.length)];
            const shapeDuration = Math.floor(Math.random() * 1000) + 1500;
            const gameBoardHeight = $('.game-board').height();
            const maxTop = gameBoardHeight - shapeSize;
            const top = Math.floor(Math.random() * maxTop);
            const boardWidth = $('.game-board').width();
            const left = Math.floor(Math.random() * (boardWidth - shapeSize));
            const shape = $('<div class="game-shape ' + shapeType + '" style="top: ' + top + 'px; left: ' + left + 'px; background-color: ' + shapeColor + '; width: ' + shapeSize + 'px; height: ' + shapeSize + 'px; animation-duration: ' + shapeDuration + 'ms;"></div>');
            $('.game-board').append(shape);

            shape.click(function () {
                $(this).remove();
                score++;
                $('#score').text(score);
            });

            setTimeout(function () {
                shape.remove();
            }, shapeDuration);
        }, 1000);

    }
});
