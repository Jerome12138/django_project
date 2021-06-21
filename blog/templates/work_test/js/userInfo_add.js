//禁止微信浏览器分享
document.addEventListener('WeixinJSBridgeReady', function onBridgeReady() {
    WeixinJSBridge.call('hideOptionMenu');
});

var gender = '2',age = '',nickName = '',storage = window.localStorage,uid = storage.getItem('uid'),result,deleteId;

function gender_chose(index){
    gender = index;
    $('.info_gender_con').removeClass("slide_now");
    $(".gder"+index).addClass("slide_now");
    $(".now_gender").attr("src","images/gender"+index+".png")
}

//监听输入
$(function() {
    $("#nickName").bind('input propertychange', function() {
        nickName = $("#nickName").val();
    })
    $("#age").bind('input propertychange', function() {
        console.log("age");
        age = $("#age").val();
    })
})

function sub_info() {
    age = $("#age").val();nickName = $("#nickName").val();
    
    console.log(age,nickName,gender);

    if ("" == age || "" == nickName || "" == gender) {
        alert('请将信息填写完整');
        return;
    } else {
        $.ajax({
            type: "POST",
            url: "http://skin-check-api.midea-hotwater.com/midea/updateUserInfo",
            dataType: "json",
            contentType: "application/x-www-form-urlencoded",
            headers: {},
            data: {
                "headimg":"","uinfoid":"","uid":uid,"gender":gender,"birthday":age,"nickname":nickName
            },
            success: function(a) {
                a = JSON.parse(a);  console.log(a);
                if (a.code == 200) {
                    storage.setItem("id", a.data.userinfo.id);
                    storage.setItem("uinfoid", a.data.userinfo.uinfoid);
                    window.location.href = "tips2.html";
                } else {
                    console.log(a.message);
                    alert(a.message);
                }
            },
            error: function(a) {
                console.log(JSON.stringify(a))
            }
        })
    }
}
//防止ios输入法弹出影响页面高度
var screenHeight = document.documentElement.clientHeight;
$("input").blur(function() { check() });

function check() {
    window.scroll(0, 0);
    window.innerHeight = window.outerHeight = screenHeight;
}