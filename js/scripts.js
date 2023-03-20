$(document).ready(function () {
    // Back to top button functionality
    $(".back-to-top").on("click", function (event) {
        event.preventDefault();
        $("html, body").animate({scrollTop: 0}, "slow");
    });
});
