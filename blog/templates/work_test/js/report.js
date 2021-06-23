var openid = window.localStorage.getItem("openid");
var id = window.localStorage.getItem("resId");
var uinfoid = window.localStorage.getItem("uinfoid");
var res,firstData,secondData,faceAll,analyse;

$.ajax({
    type: "POST",
    url: 'https://skin-check-api.midea-hotwater.com/midea/get_result',
    dataType: "json",
    contentType: "application/x-www-form-urlencoded",
    headers: {},
    data: {
        id: id,
        uinfoid:uinfoid
    },
    success: function(re) {
        res = JSON.parse(re);
        console.log("result",res);
        firstData = res.multiple;
        faceAll = res.face;
        secondData = res.dimension; //肌肤维度数据
        analyse = res.analyse;
        getFirstTab();
        getsecondTab();
    },
    error: function(re) {
        console.log(JSON.stringify(res));
    }
});

function switchPic(){
    $(".switch_img").toggleClass("show");
}

//综合
function getFirstTab() {
    var gender = firstData.skin_info.gender;
    var skinName = firstData.skin_info.nickname;
    var skinAge = firstData.skin_info.skin_age;
    var skinScore = firstData.skin_info.skin_score;
    var skinType = firstData.skin_info.skin_type;
    $("#gender").attr("src","images/gender"+gender+".png");
    // $(".problems_head").attr("src","images/pro_gender"+gender+".png");
    $(".det_time").html(firstData.skin_info.dateline);
    $(".det_name").html(skinName);
    $(".score_now").find("span").html(skinScore);
    $(".pro_now").find("span").html(skinType);
    $(".age_now").find("span").html(skinAge);

    $(".switch_img.si1").attr("src",analyse.photo);
    $(".si2").attr("src",secondData[9].label_img);
    $(".si3").attr("src",secondData[3].label_img);
    $(".si4").attr("src",secondData[4].label_img);
    
    // window.localStorage.setItem("face", analyse.photo);
    window.localStorage.setItem("skinAge", skinAge);
    window.localStorage.setItem("skinName", skinName);
    window.localStorage.setItem("skinColour", firstData.colour.name);
    window.localStorage.setItem("skinType", skinType);

    var cd =firstData.skin_info.record;
    $(".p1").find("span").html(cd.blackhead);
    $(".p2").find("span").html(cd.pore);
    $(".p3").find("span").html(cd.wrinkle);
    $(".p4").find("span").html(cd.eyes);
    $(".p5").find("span").html(cd.stain);
    drawRadar();
}


function getsecondTab() {
    //黑头、痤疮和色斑
    var HeiTou = secondData[9];
    var SeiBan = secondData[3];
    var CuoChuang = secondData[4];
    //毛孔和敏感
    var MaoKong = secondData[1];
    var MinGan = secondData[8];

    var HeiYanQuan = secondData[5];
    var ZhouWen = secondData[2];

    showDetail(HeiTou);

}
function showDetail(data){
    $(".now").css("left",(100-data.score)+"%");
    $(".pro_desc").html(data.description);
    var html='';
    var fordata= data.plan.point;
    for(var i=0;i<fordata.length;i++){
        html+='<p>'+fordata[i]+'</p>'
    }
    $(".pro_adv").html(html);

    var pro_html='';
    var prodata= data.product;
    for(var i=0;i<prodata.length;i++){
        pro_html+='<div class="recm_list flexCon"><div class="recm_pic"> <img src="'+prodata[i].image+'"/> </div><div class="recm_det flexCon"><div class="recm_det_name">'+prodata[i].name
        +'</div><div class="recm_det_tag"><span>过滤余氟</span><span>无味</span></div><a class="recm_det_buy flexCon" href="'+prodata[i].url+'"> 去抢购</a></div></div>';
    }
    $(".recm_title").after(pro_html);
    
}


