$(document).ready(function(){
    $("#mapPreview").click(function(){
        window.location.href="./map.html";
    })
    $(".boardPreviewList:first-child li:first-child").click(function(){
        window.location.href="./infoBoard.html";
    })
    $(".boardPreviewList:nth-child(2) li:first-child").click(function(){
        window.location.href="./freeBoard.html";
    })
})