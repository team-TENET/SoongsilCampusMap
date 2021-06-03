$(document).ready(function(){
    $('.menuIcon, .menuQuit, .loginSubmit, .loginRegister, .loginFind, .loginQuit').hover(function(){
        cursor:"hand";
    })
    $('.menuIcon').click(function(){
        console.log('새로 고침에 시간 걸릴때는 메뉴 아이콘 바로 안눌림');
        $('.menuSlide').css("visibility", "visible");
        $('.menuQuit2').css("visibility", "visible");
    })
    $('.menuQuit, .menuQuit2').click(function(){
        $('.menuSlide').css("visibility", "hidden");
        $('.menuQuit2').css("visibility", "hidden");
    })
    $('.loginPlease').click(function(){
        $('.menuSlide').css("visibility", "hidden");
        $('.menuQuit2').css("visibility", "hidden");
        $('.loginSlide').css("visibility", "visible");
    })
    $('.loginQuit').click(function(){
        $('.loginSlide').css("visibility", "hidden");
    })
    $('.loginSubmit').click(function(){
                if($('.loginId').val()!=""&&$('.loginPwd').val()!="")
                {
                    alert("처리되었습니다");
                    $('.loginSlide').css("visibility", "hidden");
                    //프로필 사진과 이름등의 정보를 그사람껄로 바꿔준다
                }    
    })
    $('.loginRegister').click(function(){
        window.location.href="./loginRegister";
    });
    $('.loginFind').click(function(){
        window.location.href="./loginFind";
    });
})