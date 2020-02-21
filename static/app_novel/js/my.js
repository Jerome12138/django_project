function comment(art_id){
	$.post("/comment/saveData",{comment_mid:2,comment_rid:art_id,comment_content:$(".comment-btn").val()},function(result){
	  		if(result.code==11004){
	 			layer.msg("请登录后再试！");
	  		}else{
	  			layer.msg(result.msg);
	  		}
	  });
}
function getTxt(c_id,a_id,ac){
	$.post("/art/getBookText",{c_id:c_id,a_id:a_id,ac:ac},function(result){
			 $(".models1").fadeOut();
			 $(".content").html(result);
	  });
}
function ajaxBookText(c_id,a_id,ac){
	$.post("/art/ajaxBookText",{c_id:c_id,a_id:a_id,ac:ac},function(result){
			 $(".models1").fadeOut();
			 $(".loading").hide();
			 jz=0;
			 if(result.code==-1){
			 	layer.msg("无更多章节内容了！");
			 	return;	
			 }
			 $("#chapterTitle").text(result.c_name);
			 $(".main").find("h3").text(result.c_name);
			  $(".content").html(' ');
			 $(".content").html(result.content);
			 nowCid=result.c_id;
 			 $('html ,body').animate({scrollTop: 1}, 0);
	  });
}
function noChapter(){
		layer.msg("没有更多的章节了！");
}

function more_comment(){
$.post("/comment/ajax/",{comment_mid:2,comment_rid:art_id,pg:page,format:'json'},function(result){
		if(result.list.length<1){
			layer.msg("没有更多内容了");
			return;
		}
		$.each(result.list,function(k,vo){
		 $("#JthreadList").append('<li >'+
             '<div class="user-head">'+
             ' <a href="" target="_blank"><img src="'+vo.user_portrait+'" alt="" width="50" height="50" /><em class="lv3"></em><span><i class="star star0"></i></span></a>'+
             '</div>'+
             '<div class="for-rp-con"> '+
             '<div class="name">'+vo.user_nick_name+'</div>'+
              '<div class="dec clearfix hide">'+
              '<a class="aLabel" href="javascript:void(0)" target="_blank">'+vo.comment_content+'</a>'+
              '</div>'+
              '<div class="for-quote"> 章评来自 '+
               '<strong>'+vo.data.art_name+'</strong> </div> '+
              '<div class="other"> '+
               '<div class="date fl"></div> '+
               '<div class="fr for-list">'+
                '<a href="javascript:void()" onclick="comment_up('+vo.comment_id+',this)" class="for-praise for-le "><em></em><span>'+vo.comment_up+'</span></a>'+
               '</div> '+
              '</div>'+
             '</div>'+
           '</li>');
		 })
	});
}
//收藏
function favs_set(id){
	if(!id){
		layer.msg("错误的书本！");
		return;
	}
	$.post("/user/ajax_ulog",{ac:'set',mid:2,type:2,sid:1,nid:1,id:id},function(result){
		layer.msg(result.msg);
	});

}
function comment_up(id,obj){
	$.post("/comment/digg",{id:id,type:'up'},function(result){
			layer.msg(result.msg);
			if(result.code==1){
				$(obj).parent().find("span").text(parseInt($(obj).parent().find("span").text())+1)
			}
		});
}
$(function(){
	$(".type font").html($(".typemenu .current").text());
	$(".status font").html($(".statusmenu .current").text());
	$(".fontNum font").html($(".fontNummenu .current").text());
	$(".zm font").html($(".firstcharmenu .current").text());	
	$(".select_con a").click(function(){
		//
})

})

function goPage(url){
	window.location.href=url+"&page="+$("#page").val();
}