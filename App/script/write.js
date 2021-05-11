$(document).ready(function(){
    $('#cancelIcon').click(function(){
        var select=confirm("작성을 취소하시겠습니까?");
        if(select)
            history.go(-1);
    })
    $('#finishIcon').click(function(){
        var select=confirm("작성을 완료하시겠습니까?");
        if(select)
            history.go(-1);
    })
    $('.attachmentIcon').click(function(){
        var select=confirm("첨부하시겠습니까?");
        if(select)
            ;//첨부기능 넣기
    })
})