$(document).ready(function () {
    let timeRemaining = 30;
    let score = 0;
    let gameTimer;
    let shapeInterval;

    // Start the game when the "Start Game" button is clicked
    $('#start-button').click(function () {
        startGame();
    });

    // Start the game
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
                clearInterval(shapeInterval);
                $('.game-shape').remove();
            }
        }, 1000);

        // Create the game shapes
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

            // Remove the shape when clicked and increment the score
            shape.click(function () {
                $(this).remove();
                score++;
                $('#score').text(score);
            });

            // Remove the shape after a random duration
            setTimeout(function () {
                shape.remove();
            }, shapeDuration);
        }, 1000);

    }
});
