function drawRadar() {
    var o = document.getElementById("radarCanvas");
    var radarcolor = "#c9a063";
    var mH = o.offsetHeight; //高度
    var mW = o.offsetWidth; //宽度

    var mData = [
        ['细腻度', 77],
        ['细腻度', 72],
        ['细腻度', 66],
        ['细腻度', 60],
        ['细腻度', 80]
    ];
    
    var radar_arr = firstData.skin_info.radar; //读取数据
    for (var i = 0; i < radar_arr.length; i++) {
        mData[i][0] = radar_arr[i].name;
        mData[i][1] = radar_arr[i].score;
    }
    var mCount = 5; //边数 
    var mCenter = mW / 2; //中心点
    var mRadius = mCenter - 50; //半径(减去的值用于给绘制的文本留空间)
    var mAngle = Math.PI * 2 / mCount; //角度
    var mCtx = null;
    var mColorPolygon = 'rgba(204, 204, 204, 1)'; //多边形颜色
    var mColorLines = 'rgba(204, 204, 204, 1)'; //顶点连线颜色

    //初始化
    (function() {
        var canvas = document.createElement('canvas');
        var radar = document.getElementById("radarCanvas");
        radar.appendChild(canvas);
        canvas.height = mH;
        canvas.width = mW;
        mCtx = canvas.getContext('2d');

        drawPolygon(mCtx);
        drawLines(mCtx);
        // drawText(mCtx);
        // drawScore(mCtx);
        drawRegion(mCtx);
    })();

    // 绘制多边形边
    function drawPolygon(ctx) {
        ctx.save();
        ctx.strokeStyle = mColorPolygon;
        var r = mRadius / mCount; //单位半径
        var currentAngle = -Math.PI / 2-120;
        for (var i = 0; i < mCount; i++) {
            ctx.beginPath();
            var currR = r * (i + 1); //当前半径
            //画多条边
            for (var j = 0; j < mCount; j++) {
                var x = mCenter + currR * Math.cos(currentAngle);
                var y = mCenter + currR * Math.sin(currentAngle);
                currentAngle += mAngle;
                ctx.lineTo(x, y);
            }
            ctx.closePath()
            ctx.stroke();
        }
        ctx.restore();
    }

    //顶点连线
    function drawLines(ctx) {
        ctx.save();
        ctx.beginPath();
        ctx.strokeStyle = mColorLines;
        var currentAngle = -Math.PI / 2-120;
        for (var i = 0; i < mCount; i++) {
            var x = mCenter + mRadius * Math.cos(currentAngle);
            var y = mCenter + mRadius * Math.sin(currentAngle);
            currentAngle += mAngle;
            ctx.moveTo(mCenter, mCenter);
            ctx.lineTo(x, y);
        }
        ctx.stroke();
        ctx.restore();
    }
    //绘制分值
    function drawScore(ctx) {
        ctx.save();
        var fontSize = mCenter / 10;
        // console.log(fontSize);
        ctx.font = fontSize + 'px Microsoft Yahei';
        ctx.fillStyle = radarcolor;
        var currentAngle = -Math.PI / 2;
        for (var i = 0; i < mCount; i++) {
            var x = mCenter + mRadius * Math.cos(currentAngle);
            var y = mCenter + mRadius * Math.sin(currentAngle);
            currentAngle += mAngle;
            if (currentAngle >= 0 && currentAngle <= Math.PI / 2) {
                y = y + fontSize
            } else if (currentAngle > Math.PI / 2 && currentAngle <= Math.PI) {
                x = x - ctx.measureText(mData[i][1]).width, y = y + fontSize
            } else if (currentAngle > Math.PI && currentAngle <= Math.PI * 3 / 2) {
                x = x - ctx.measureText(mData[i][1]).width
            } else {}
            if (i == 0) { x = x - 5, y = y - 7 } else if (i == 1) {
                x = x + 10
            } else if (i == 2) {
                x = x + 15, y = y + 35
            } else if (i == 3) {
                x = x - 0, y = y + 52
            } else { x = x - 10, y = y + 0 }
            ctx.fillText(mData[i][1], x, y);
        }
        ctx.restore();
    }
    //绘制文本
    function drawText(ctx) {
        ctx.save();
        var fontSize = mCenter / 10;
        ctx.font = fontSize + 'px Microsoft Yahei';
        ctx.fillStyle = '#333';
        var currentAngle = -Math.PI / 2;
        for (var i = 0; i < mCount; i++) {
            var x = mCenter + mRadius * Math.cos(currentAngle);
            var y = mCenter + mRadius * Math.sin(currentAngle);
            currentAngle += mAngle;
            if (currentAngle >= 0 && currentAngle <= Math.PI / 2) {
                y = y + fontSize
            } else if (currentAngle > Math.PI / 2 && currentAngle <= Math.PI) {
                x = x - ctx.measureText(mData[i][1]).width, y = y + fontSize
            } else if (currentAngle > Math.PI && currentAngle <= Math.PI * 3 / 2) {
                x = x - ctx.measureText(mData[i][1]).width
            } else {}

            if (i == 3) { x = x - 10, y = y + 30 } else if (i == 1) { y = y - 20 } else if (i == 2) { y = y + 12 } else if (i == 4) { x = x - 40, y = y - 20 } else { x = x - 15, y = y - 30 }
            ctx.fillText(mData[i][0], x, y);
        }
        ctx.restore();
    }

    //绘制数据区域
    function drawRegion(ctx) {
        ctx.save();
        ctx.beginPath();
        var currentAngle = -Math.PI / 2 -120;
        for (var i = 0; i < mCount; i++) {
            var x = mCenter + mRadius * Math.cos(currentAngle) * mData[i][1] / 100;
            var y = mCenter + mRadius * Math.sin(currentAngle) * mData[i][1] / 100;
            currentAngle += mAngle;
            ctx.lineTo(x, y);
        }
        ctx.closePath();
        ctx.fillStyle = "rgba(246, 186, 25, 0.7)";
        ctx.fill();
        ctx.restore();
        var html = '';
        for (var j = 0; j < mCount; j++) {
            html += '<div class="radar_score rsc' + j + '"><div class="rs1">' + mData[j][1] + '</div> <div class="rs2">' + mData[j][0] + '</div> </div>'
        }
        $(".radar_div").append(html);
    }
}