document.addEventListener('WeixinJSBridgeReady', function onBridgeReady() {
    WeixinJSBridge.call('hideOptionMenu');
});

var file_img;
$(".iosP").on("change", function() {
    window.mdSmartios.bridge.buttonClickTracking("开始拍摄")
    var files = $(this)[0].files;
    if (files.length > 0) {
        var file = files[0];
        file_img = files[0]; //file图片文件
        var reader = new FileReader();
        reader.onload = function(e) {
            dataURL = reader.result;
            $(".user_container").css("display", "none");
            $(".take_photo").css("display", "block");
            $(".getPic").attr("src", reader.result);
            $(".getPicImg").css("opacity", "1");
            document.title = '拍照';
            //回调函数
        }
        reader.readAsDataURL(file);
        $(".if_not").css("display", "flex");
    }
})

$('.to_a').on('click', function() {
    window.mdSmartios.bridge.buttonClickTracking("确定")
    $(".if_not").css("display", "none");
    $(".ana_container").css("display", "flex");
    var id = window.localStorage.getItem("id");
    var uinfoid = window.localStorage.getItem("uinfoid");
    let a = Date.now();
    console.log(a);
    var data = new FormData();
    data.append('file', file_img);
    data.append('uid', id);
    data.append('uinfoid', uinfoid);
    data.append('times', a);
    var per_now =0; var per_score=0;
    var timer1 = setInterval(function(){
        if(per_now<100){
            per_now+=2;
            $(".progress_bar_now").css("width",per_now+"%");
        }
    },100);
    var timer2 = setInterval(function(){
        if(per_score<99){
            per_score += 2;
            if(per_score==100){
                $(".progress_percent").html(per_score-2+"%");
            }else{
                $(".progress_percent").html(per_score+"%");
            }
        }
    },100);
    setTimeout(function(){
        clearInterval(timer1)
        clearInterval(timer2);
    },6000)
    $.ajax({
        type: "POST",
        url: 'https://skin-check-api.midea-hotwater.com/midea/analyse',
        dataType: "json",
        contentType: false,
        processData: false,
        headers: {},
        data: data,
        success: function(res) {
            var res = JSON.parse(res).data;
            console.log(res);
            if (res.code == 200) {
                window.localStorage.setItem("resId", res.data.id);
                window.location.href = "result.html";
            } else {
                var tip = res.message;
                $(".tishi3").html(tip);
                $(".pink_div").css("opacity", "1");
                $(".loadTip").css("display", "none");
                $(".loadGif").css("display", "none");
            }
        },
        error: function(res) {
            console.log(JSON.stringify(res));
        }
    });
})

$(".reShot").on('click', function() {
        $(".take_photo").css("display", "none");
        $(".user_container").css("display", "flex");
        window.mdSmartios.bridge.buttonClickTracking("重拍")
        window.location.reload();
    })
    //未识别到人脸重拍
$(".returnShot").on('click', function() {
    $(".user_container").css("display", "flex");
    $(".if_not").css("display", "none");
    $(".ana_container").css("display", "none");
    window.location.reload();
})

//将base64转换为文件
function dataURLtoFile(dataurl, filename) {
    var arr = dataurl.split(','), mime = arr[0].match(/:(.*?);/)[1],
        bstr = atob(arr[1]), n = bstr.length, u8arr = new Uint8Array(n);
    while(n--){
        u8arr[n] = bstr.charCodeAt(n);
    }
    return new File([u8arr], filename, {type:mime});
}
// 安卓兼容
function takePhotoAndroid() {
    window.mdSmartios.bridge.buttonClickTracking("开始拍摄")
    window.mdSmartios.bridge.takePhoto({"compressRage": 50,"type": "jpg","isNeedBase64": true}, res=>{
        // alert(JSON.stringify(res))
        if (res.status == 0) {
            var img_base64 = res.data
            file_img = dataURLtoFile(img_base64, "photo.png")
            $(".user_container").css("display", "none");
            $(".take_photo").css("display", "block");
            $(".getPic").attr("src", img_base64);
            $(".getPicImg").css("opacity", "1");
            document.title = '拍照';
            $(".if_not").css("display", "flex");
        }
    })
}