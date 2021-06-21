function getMonthDate() {
    var date = new Date();
    var year = date.getFullYear() + "";    
    var month = (date.getMonth() + 1) + "";  
    if(month.length<2){
     month='0'+month  
    } 
    var day = date.getDate() + "";
    if(day .length<2){
        day ='0'+day                 
    }
    var now= year + "-" + month + "-"  + day 
    return now;
}

var today = getMonthDate();
var uinfoid = window.localStorage.getItem("uinfoid");

var start= $("#startTime").val(); var end= $("#endTime").val();
getRecord('',''); console.log(start,end);

window.onload = function() {
    new Rolldate({
        el: "#startTime",
        value: "2021-06-01",
        format: "YYYY-MM-DD",
        beginYear: 2010,
        endYear: 2021,
        init: function() {
            $("input").blur(); //其他input始去焦点
        },
        confirm: function(date) {
            if (date > today) {
                alert('不能大于当前的日期');
                return false;
            }
            start = date;
            if(end!='全部'){
                getRecord(date,end);
            }
            
        }
    })
    new Rolldate({
        el: "#endTime",
        format: "YYYY-MM-DD",
        beginYear: 2010,
        endYear: 2021,
        init: function() {
            $("input").blur(); //其他input始去焦点
        },
        confirm: function(date) {
            if (date > today) {
                alert('不能大于当前的日期');
                return false;
            }
            end = date;
            if(date!='全部'){
                getRecord(start,date);
            }
            
        }
    })
    
};

function getRecord(stattime,endtime){
    $.ajax({
        type: "POST",
        url: "http://skin-check-api.midea-hotwater.com/midea/get_record",
        dataType: "json",
        contentType: "application/x-www-form-urlencoded",
        headers: {},
        data: { "uinfoid": uinfoid,"page":1,"starttime":stattime,"endtime":endtime },
        success: function(a) {
            console.log(JSON.parse(a));
            a = JSON.parse(a);
            if(a.code=="200"){
                var recordList = a.data.record;
                var userhtml='';
                if(recordList.length>0){
                    for(var i=0;i<recordList.length;i++){
                        var nick='女神'; if(recordList[i].gender==1){ nick='男神'; }
                        userhtml+='<div class="his_list_con" onclick="updateResult('+recordList[i].id+')"><div class="list_about flexCon"><div class="li_about_name flexCon">'+recordList[i].nickname
                        +'<span class="flexCon">'+nick+'</span><span class="flexCon">'+recordList[i].age+'岁</span></div><span class="iconfont icon-gengduo"></span></div>'+
                        '<div class="li_about2"><div class="li_about_score">当前肤质综合得分<span class="score_cut">'+recordList[i].skin_score+
                        '<span class="score_per">分</span></span></div><div class="li_about_time">'+recordList[i].dateline+
                        '</div></div><div class="about_problems flexCon">'+
                        '<div class="pro p1">黑头 '+recordList[i].blackhead+'</div><div class="pro p2">毛孔 '+recordList[i].pore+'</div><div class="pro p3">皱纹 '+recordList[i].wrinkle+'</div>'+
                        '<div class="pro p4">黑眼圈 '+recordList[i].eyes+'</div><div class="pro p5">法令纹 '+recordList[i].stain+'</div><img class="problems_head" src="images/problems_head.png"></div></div>';
                    }
                    $(".his_list").html(userhtml);
                }else{
                    $(".his_list").html('<p class="none_data">当前时间段没有记录哦</p>'); 
                }
            }else {
                console.log(a.message);
                alert(a.message.message);
            }
        },
        error: function(a) {
            console.log(JSON.stringify(a))
        }
    })
}

function updateResult(id){
    window.localStorage.setItem("resId",id);
    window.location.href="result.html";
}