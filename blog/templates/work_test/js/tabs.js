/**
 * Created by Administrator on 2020/10/23 0013.
 */

var mySwiper = new Swiper('#tab-detail', {
    direction: 'horizontal',
    loop: false,
    observer: true,
    initialSlide: 0,
    observeParents: true,
    keyboardControl: true,
    updateOnImagesReady: true,
    autoHeight: true, //切换tab时滚动到顶部
    noSwipingClass: 'face_area_scroll', //设置可滚动内容
    onSlideChangeStart: function(swiper) {
        var i = mySwiper.activeIndex;
        $(".tabA").attr("class", "tabA flexCon");
        $(".tabA").eq(i).addClass("active");
        if (i == 1) {
            $(".sw_pro_tab").css("display", 'flex');
        } else {
            $(".sw_pro_tab").css("display", 'none');
        }
        $("#swang").css("padding-bottom", '0');
        window.scrollTo(0, 0);

        swiper.enableMousewheelControl();
        console.log("aaa");
    }
})

$('#wt0').click(function() {
    $(".tabA").attr("class", "tabA flexCon");
    $(this).addClass("active");
    mySwiper.slideTo(0, 600, false); //切换到第一个slide
    setting();
})
$('#wt1').click(function() {
    $(".tabA").attr("class", "tabA flexCon");
    $(this).addClass("active");
    mySwiper.slideTo(1, 600, false); //切换到第二个slide
    setting();
    $(".sw_pro_tab").css("display", 'flex');
})
$('#wt2').click(function() {
    $(".tabA").attr("class", "tabA flexCon");
    $(this).addClass("active");
    mySwiper.slideTo(2, 600, false); //切换到第三个slide
    setting();
});
$('#wt3').click(function() {
    $(".tabA").attr("class", "tabA flexCon");
    $(this).addClass("active");
    mySwiper.slideTo(3, 600, false); //切换到第四个slide
    setting();
});
$('#wt4').click(function() {
    $(".tabA").attr("class", "tabA flexCon");
    $(this).addClass("active");
    mySwiper.slideTo(4, 600, false); //切换到第五个slide
    setting();
});

function cliSedTab(e) {
    var nowTab = parseInt($(e).attr("data-id"));
    $(".sw_pro_tab").find('div').attr("class", "");
    $(e).addClass("tab_now");
    window.scrollTo(0, 0);
    mySwiper2.slideTo(nowTab, 300, false);
    var now_left = (nowTab * 14.28) + "%";
    $(".tab_bg").animate({ left: now_left }, 300);
    setTimeout(function() { $(".sw_pro_tab").find('div').eq(nowTab).addClass("tab_now"); }, 150);
}

var startScroll, touchStart, touchCurrent;



function show_tb(e) {
    var index = $(e).attr("data-id");
    $(".nav-item2").attr("class", "nav-item2");
    $(e).addClass("pro_active");
    mySwiper3.slideTo(index, 600, false);
}

function setting() {
    window.scrollTo(0, 0);
    $(".sw_pro_tab").css("display", 'none');
    $("#swang").css("padding-bottom", '0');
}