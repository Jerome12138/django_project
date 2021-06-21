//禁止微信浏览器分享
document.addEventListener('WeixinJSBridgeReady', function onBridgeReady() {
    WeixinJSBridge.call('hideOptionMenu');
});

var gender = '2',age = "",nickName = '',storage = window.localStorage,uid = storage.getItem('uid'),result,deleteId;

function cur_list(index,e){
    $(".cus_list").removeClass("current"); $(e).addClass("current");

    $(".op_sure").css("display","none");
    $(".op_sub").css("display","none");
    if(index=='0'){
        $(".op_edit2").css("display","none");
        $(".op_edit").css("display","flex");
    }
    else{
        $(".op_edit").css("display","none");
        $(".op_edit2").css("display","flex");
    }
    $(".cover_edit").css("display","block");
    if(result.length>0){
        var now_person = result[parseInt(index)];
        deleteId = now_person.uinfoid;
        $("#nickName").val(now_person.nickname);
        $("#age").val(now_person.age);
        gender_chose(now_person.gender);

        //判断是否有历史记录
        haveHistory(deleteId);
        storage.setItem("historyId",deleteId);
    }
    
}
//点击编辑按钮
$(".edit_change").click(function(){
    $(".op_edit").css("display","none");
    $(".op_edit2").css("display","none");
    $(".edit_sure").css("display","flex");
    $(".cover_edit").css("display","none");
})
$(".edit_yes").click(function(){
    $(".edit_sure").css("display","none");
    $(".op_sub").css("display","flex");
})

function gender_chose(index){
    gender = index;
    $('.info_gender_con').removeClass("slide_now");
    $(".gder"+index).addClass("slide_now");
    $(".now_gender").attr("src","images/gender"+index+".png")
}
function haveHistory(cs){
    $.ajax({
        type: "POST",
        url: "http://skin-check-api.midea-hotwater.com/midea/get_record",
        dataType: "json",
        contentType: "application/x-www-form-urlencoded",
        headers: {},
        data: {"uinfoid":cs,"page":1},
        success: function(a) {
            a = JSON.parse(a);
            if(a.data.record.length>0){
                $(".customer_record").attr("id","show")
            }
            console.log("历史记录",a);
        },error: function(a) {
            console.log(JSON.stringify(a))
        }
    })
}


function getUser(){
    $.ajax({
        type: "POST",
        url: "http://skin-check-api.midea-hotwater.com/midea/getrexuser",
        dataType: "json",
        contentType: "application/x-www-form-urlencoded",
        headers: {},
        data: { "uid": uid, },
        success: function(a) {
            console.log(JSON.parse(a));
            a =JSON.parse(a);
            if(a.code=="200"){
                var userList = a.data.userlist;
                result = a.data.userlist;
                var userhtml='';
                if(userList.length>0){
                    cur_list(0);//默认用户信息读取
                    for(var i=0;i<userList.length;i++){
                        if(i==0){
                            userhtml+='<div class="cus_list current" onclick="cur_list('+i+',this)" data-uinfoid="'+userList[i].uinfoid
                            +'"><div class="cus_img flexCon"><img src="images/gender'+userList[i].gender+'.png"></div> <div class="cus_name">'+userList[i].nickname+'</div> </div>';
                        }else{
                            userhtml+='<div class="cus_list" onclick="cur_list('+i+',this)" data-uinfoid="'+userList[i].uinfoid
                            +'"><div class="cus_img flexCon"><img src="images/gender'+userList[i].gender+'.png"></div> <div class="cus_name">'+userList[i].nickname+'</div> </div>';
                        }
                    }
                    $(".cus_scroll").append(userhtml);
                }else{
                    window.location.href="info2_add.html";
                }
            }
        },
        error: function(a) {
            console.log(JSON.stringify(a))
        }
    })
}



//监听输入
$(function() {
    $("#nickName").bind('input propertychange', function() {
        nickName = $("#nickName").val();
    })
    $("#age").bind('input propertychange', function() {
        age = $("#age").val();
    })
})

getUser();


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
                "headimg":"", "uinfoid":deleteId,"uid":uid,"gender":gender,"birthday":age,"nickname":nickName
            },
            success: function(a) {
                a = JSON.parse(a);
                console.log(a);
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
function delete2(){
    $.ajax({
        type: "POST",
        url: "http://skin-check-api.midea-hotwater.com/midea/delrexuser",
        dataType: "json",
        contentType: "application/x-www-form-urlencoded",
        headers: {},
        data: { "uinfoid": deleteId, },
        success: function(a) {
            console.log(JSON.parse(a));
            a = JSON.parse(a);
            if(a.code=="200"){
                console.log("delete success",a);
                location.reload();
            }
        },
        error: function(a) {
            console.log(JSON.stringify(a))
        }
    })
}



var screenHeight = document.documentElement.clientHeight;
$("input").blur(function() { check() });

function check() {
    window.scroll(0, 0);
    window.innerHeight = window.outerHeight = screenHeight;
}