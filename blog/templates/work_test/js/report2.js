var openid = window.localStorage.getItem("openid");
var id = window.localStorage.getItem("resId");
var uinfoid = window.localStorage.getItem("uinfoid");
var res,firstData,secondData,faceAll;

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
        console.log("结果",res);
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


//综合
function getFirstTab() {
    var gender = firstData.skin_info.gender;
    var skinName = firstData.skin_info.nickname;
    var skinAge = firstData.skin_info.skin_age;
    var skinScore = firstData.skin_info.skin_score;
    var skinType = firstData.skin_info.skin_type;
    $("#gender").attr("src","images/gender"+gender+".png");
    $(".det_time").html(firstData.skin_info.dateline);
    $(".det_name").html(skinName);
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

    showDetail(HeiTou,0);
    showDetail(MaoKong,1);
    showDetail(CuoChuang,2);
    showDetail(ZhouWen,3);
    showDetail(SeiBan,4);

}
function showDetail(data,index){
    var html='';
    var fordata= data.plan.point;
    var reg = new RegExp("$");
    data.description = data.description.replace(reg,"");
    for(var i=0;i<fordata.length;i++){
        html+='<p>'+fordata[i]+'</p>'
    }
    var pro_html='';
    var prodata= data.product;
    if(prodata.length>0){
        pro_html='<div class="recm_title">以上问题，配合使用，推荐以下产品效果更好</div>';
    }
    for(var i=0;i<prodata.length;i++){
        pro_html+='<div class="recm_list flexCon"><div class="recm_pic"> <img src="'+prodata[i].image+'"/> </div><div class="recm_det flexCon"><div class="recm_det_name">'+prodata[i].name
        +'</div><div class="recm_det_tag"><span>过滤余氟</span><span>无味</span></div><div class="recm_det_buy flexCon" onclick="toBuy('+`'${prodata[i].url}','${prodata[i].name}'`+')"> 去抢购</div></div></div>';
    }

    var all_html='<div class="dims_area mar69"><div class="level_status"><div class="status_top_left bigger_title"><span class="iconfont icon-zhuangtai"></span>'+data.name+
        '状态</div><div class="status_top flexCon"><div class="level_intro"><div class="level_where"><div class="now"style="left: '+(100-data.score)+
        '%;"></div><div class="lc level_color1"></div><div class="lc level_color2"></div><div class="lc level_color3"></div></div>'+
        '<div class="level_name"><div class="ln">轻度</div><div class="ln">中度</div><div class="ln">重度</div></div></div></div>'+
        '<div class="status_pic"><div class="status_pic_v"><img class="pic_v zoom_bgp"src="images/posi'+index+
        '.png"><img class="zoom_bg"src=""></div><div class="status_pro">'+data.description+'</div><div class="radar_title flexCon"style="width: 1.6rem;">解决方案</div>'+
        '<div class="status_pro">'+html+'</div><div class="recm_pro pad30">'+pro_html+
        '</div></div></div></div>';
    
    $("#tab-d"+(index+1)).html(all_html);
    
}

function toBuy(url,name){
    window.mdSmartios.bridge.goToMeijuPage("jumpElecBusiness",{"url":url})
    window.mdSmartios.bridge.buttonClickTracking("去购买",{"url":url,"name":name})
}