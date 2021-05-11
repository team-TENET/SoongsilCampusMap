$(document).ready(function(){
    $("#mapPreview").click(function(){
        window.location.href="./map.html";
    })
    $(".boardPreviewList:first-child li:first-child").click(function(){
        window.location.href="./infoBoard.html";
    })
    $(".boardPreviewList:last-child li:first-child").click(function(){
        window.location.href="./freeBoard.html";
    })
})