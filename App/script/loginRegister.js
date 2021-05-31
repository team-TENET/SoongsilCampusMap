$(document).ready(function(){
    $('#registerCancel').click(function(){
        window.location.href=".home.html";
    })
    $('#registerDone').click(function(){
        //일단 정보 넘기고 성공하면
        alert("회원가입이 완료되었습니다");
        window.location.href="./home.html";
    })
})