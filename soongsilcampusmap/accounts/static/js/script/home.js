$(document).ready(function(){
    $("#mapPreview").click(function(){
        window.location.href="./map";
    }) 
    $(".boardPreviewList:first-child li:first-child").click(function(){
        window.location.href="./infoBoard";
    }) 
    $(".boardPreviewList:nth-child(2) li:first-child").click(function(){
        window.location.href="./freeBoard";
    }) 
    $(".boardPreviewList li").click(function(){
        window.location.href="./read";
    }) 
})