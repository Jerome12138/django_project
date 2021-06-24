/**
 * @fileoverview meiju use bridge
 */

var mdSmartios = mdSmartios || {};
(function(mdSmartios) {
    if (mdSmartios.bridge) {
        console.log("mdSmartios.bridge is already defined.");
        return;
    }
    mdSmartios.bridge = mdSmartios.bridge || {};

    mdSmartios.bridge.storage={};

	/*
		通用的接口，operation（string）表示功能类型，params（JSON）表示传参
	*/
	mdSmartios.bridge.commandInterface = function(operation, params, callback, callbackFail) {
		let param = {};
		param.operation = operation;
		param.params = params;
		param.cammandId = Math.floor(Math.random() * 10000);
		let commandIds = param.cammandId;
		let p = JSON.stringify(param);
		if (typeof callback == "function") {
			mdSmartios.bridge.callbackFunctions[commandIds] = callback;
		}

		if (typeof callbackFail == "function") {
			mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
		}
		let commandId = mdSmartios.bridge.po._execObjcMethod('commandInterface', p);
		return commandId;
	};

	/**
	 * 字节埋点接口(6.8）
	 * @param {json} param
	 */
	mdSmartios.bridge.trackEvent = function (param, callback, callbackFail) {
		mdSmartios.bridge.commandInterface('trackEvent', param, callback && callback, callbackFail && callbackFail);
	};

    /**
     * 美居6.4.0 拍照
     * @param {*} param
     * {
        compressRage: 0;//Number,返回照片的压缩率，范围为0~100，数值越高保真率越高
        "type": "";//值为jpg或png，指定返回相片的格式
        isNeedBase64: true/false;//是否需要返回相片base64数据
     * }
     * @param {*} callback
     * @param {*} callbackFail
     */
    mdSmartios.bridge.takePhoto = function (param, callback, callbackFail) {
        if (param == undefined || param == "") {
            param = {};
        }
        param.cammandId = Math.floor(Math.random() * 100000);
        let commandIds = param.cammandId;
        let p = JSON.stringify(param);
        if (typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandIds] = callback;
        }

        if (typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
        }

        let commandId = mdSmartios.bridge.po._execObjcMethod('takePhoto4', p);

        return commandId;
    };

    /**
     * 美居6.4.0 转换本地图片成base64数据
     * @param {*} param
     * {
        filePath: xxxx, //手机本地图片路径
        }
    * @param {*} callback
    * @param {*} callbackFail
    */
    mdSmartios.bridge.convertLocalImageToBase64 = function (param, callback, callbackFail) {
        if (param == undefined || param == "") {
            param = {};
        }
        param.cammandId = Math.floor(Math.random() * 100000);
        let commandIds = param.cammandId;
        let p = JSON.stringify(param);
        if (typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandIds] = callback;
        }

        if (typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
        }

        let commandId = mdSmartios.bridge.po._execObjcMethod('convertLocalImageToBase64', p);

        return commandId;
    };
    
    /**
     * Clear WebView Cache
     * @return void
     */
    mdSmartios.bridge.clearWebViewCache = function() {
        console.log('function:mdSmartios.bridge.clearWebViewCache');
        mdSmartios.bridge.po._execObjcMethod('clearWebViewCache');
    };
    mdSmartios.bridge.callbackFunctions = {};
    mdSmartios.bridge.callbackFailFunctions = {};
    mdSmartios.bridge.setCardTitleCBF = undefined;

    //直接返回值(IOS赋值：回复JS所有类型请求（startCmdProcess：命令id，getLangCode：语言code）)
    mdSmartios.bridge.retObjcValue = 0;

    mdSmartios.bridge.retSnValue = "";

    mdSmartios.bridge.applicationId = "";

    mdSmartios.bridge.currentApplianceSubtype = "";
    
    /*
     *指定命令的回复电文(IOS调用：回复startCmdProcess)
     *@param (int) retObjcValue 命令id
     *       (String) result 回复
     *                result.messageBody 回复电文
     *                result.errCode 错误码
     *                             1 超时   -1 查询超时
     *                result.errMessage 错误信息
     */
     mdSmartios.bridge.callbackFunction = function(retObjcValue, result) {
        console.log('callbackFunction result', retObjcValue, result)
        var jsonResult = result;
        if (typeof jsonResult === 'string') {
            try {
                jsonResult = JSON.parse(jsonResult);
            } catch (error) {
                console.error('callbackFunction parse error', retObjcValue, error)
            }
        }
        var cbf = mdSmartios.bridge.callbackFunctions[retObjcValue];
        var cbff = mdSmartios.bridge.callbackFailFunctions[retObjcValue];
        if (jsonResult.errCode !== undefined && jsonResult.errMessage == 'TimeOut') {
            if(jsonResult.errCode==-1){
                if(location.href.indexOf('card')!=-1){
                    bridge.logToIOS('Jump to cardDisconnect.html.');
                    location.href='cardDisconnect2.html';
                }
            }else{
                //keane 指令失败函数自定义 Mod S
                if (typeof cbff == "function") {
                    cbff(-1);//表示指令超时 －1
                }
                if(jsonResult.isAction == 1) {
                    // 控制超时才弹出提示
                    bridge.popupTimeOut();
                }
                //keane 指令失败函数自定义 Mod E
            }
        } else {
            if ( typeof cbf == "function") {
                cbf(jsonResult.messageBody || jsonResult);
            }
        }
        delete mdSmartios.bridge.callbackFunctions[retObjcValue];
        delete mdSmartios.bridge.callbackFailFunctions[retObjcValue];
    };

    mdSmartios.bridge.po = {
        _execObjcMethod : function(method, data) {
            try {
                var tmp = method;

                if (data != undefined && data != '') {
                    tmp = tmp + '?' + data;
                }
                console.log('Exec ' + tmp);
                var iframe = document.createElement("IFRAME");
                iframe.setAttribute("src", "iosbridge://" + tmp);
                document.documentElement.appendChild(iframe);
                iframe.parentNode.removeChild(iframe);
                iframe = null;
            } catch(e) {
                console.log(method + ' exception');
            }
            //var value = mdSmartios.bridge.commandIds[id];
            //
            //delete mdSmartios.bridge.commandIds[id];

            //if(value != undefined){
            //if(value != undefined){
            //    bridge.logToIOS("javaScript:mdSmartios.bridge.retObjcValue == " + value + " id " + id);
            //}else{
            //    bridge.logToIOS("javaScript:mdSmartios.bridge.retObjcValue == undefined");
            //}
            return mdSmartios.bridge.retObjcValue;
        }
    };

    //显示alert
    mdSmartios.bridge.showAlert = function(cmdParamers) {
        console.log('function:mdSmartios.bridge.showAlert');
        var param = {};
        if (cmdParamers != undefined) {
            param.cmdParamers = cmdParamers;
        }

        var p = JSON.stringify(param);
        var commandId = mdSmartios.bridge.po._execObjcMethod('showAlert', p);
        return commandId;
    };

    /**
     * 跳转App页面
     * @param: type: 跳转类型, 跳转原生页，为”jumpNative”, 跳转插件页，为“jumpPlugin”, 跳转weex，为“jumpWeex”,  跳转webview则为“jumpWebview”
     * @param: param: 详细信息字典 内部具体信息如下
     *                跳转webview，参数有url等
     *                跳转插件页，参数有deviceId等
     *                跳转原生页，参数有pageName等
     *                跳转weex，参数有url等
     *                需不需要带导航栏字段 如needNavigation。1为需要0为不需要
     *                需不需要带底部导航 如needTabbar
     * http://confluence.msmart.com/pages/viewpage.action?pageId=21498414
     */
    mdSmartios.bridge.goToMeijuPage = function (type, param) {
        console.log('function:mdSmartios.bridge.goToMeijuPage');
        type = type || 'jumpNative';
        param = param || {
            pageName: 'service_home',
            needNavigation: '1',
            needTabbar: '1'
        };
        var params = {};
        params.type = type;
        params.param = param;
        var p = JSON.stringify(params);
        var commandId = mdSmartios.bridge.po._execObjcMethod('goToMeijuPage', p);
        return commandId;
    }

    /**

     * 判断是否为安卓系统
     * @author Jun
     */
    if (!mdSmartios.bridge.isAndroid) {
        var u = navigator.userAgent;
        mdSmartios.bridge.isAndroid = u.indexOf('Android') > -1 || u.indexOf('Linux') > -1;
    }

    // -------------------自定义函数（Jerome）----------------
    mdSmartios.bridge.pageName = "肌肤管家首页"

    /**
     * 判断是否美居
     */
    var ua = navigator.userAgent.toLowerCase()
    mdSmartios.bridge.isMeiju = /meiju|msmart/.test(ua)

    /**
     * 获取url中的参数
     * @param variable
     */
    mdSmartios.bridge.getQueryVariable = function(variable){
        var query = window.location.search.substring(1);
        var vars = query.split("&");
        for (var i=0;i< vars.length;i++) {
                var pair = vars[i].split("=");
                if(pair[0] == variable){return pair[1];}
        }
        return(false);
    }

    /**
     * 页面浏览事件埋点
     * @param param
     */
    mdSmartios.bridge.pageViewTracking = function(pageName){
        console.log("pageName:",pageName)
        mdSmartios.bridge.pageName = pageName
        if (mdSmartios.bridge.isMeiju) {
            // var referName = mdSmartios.bridge.getQueryVariable("referName")
            // if (referName) {
            //     console.log("referName:",referName)
            //     mdSmartios.bridge.referName = referName
            // }
            mdSmartios.bridge.pageName = pageName
            let eventTrackingParams = {
                event: 'plugin_page_view',
                eventParams: {
                    module: '插件',
                    bd_name: '厨热',
                    apptype_name: '电热水器',
                    widget_cate: 'E2',
                    page_name:  pageName,
                    // refer_name:  mdSmartios.bridge.referName,
                }
            }
            mdSmartios.bridge.trackEvent(eventTrackingParams)
        } 
    }

    /**
     * 按钮点击事件埋点
     * @param element_content // 按钮名称
     * @param params  // 可选，传入额外的参数（json对象转字符串格式）
     */
    mdSmartios.bridge.buttonClickTracking = function(element_content, params){
        if (mdSmartios.bridge.isMeiju) {
            if (typeof params == 'object') {
              params = JSON.stringify(params)
            }
            let eventTrackingParams = {
                event: 'plugin_button_click',
                eventParams: {
                    module: '插件',
                    bd_name: '厨热',
                    apptype_name: '电热水器',
                    widget_cate: 'E2',
                    page_name:  mdSmartios.bridge.pageName,
                    element_content: element_content,
                    custom_params: params || ''
                }
            }
            console.log("buttonClickTracking:",eventTrackingParams)
            mdSmartios.bridge.trackEvent(eventTrackingParams)
        } 
    }

})(mdSmartios);

(function(window, mdSmartios) {
    console.log('--iPhone bridge--');
    // iPhone log
    if (window.navigator.userAgent.indexOf('DEBUG_LOG') != -1) {
        console = new Object();
        console.log = function(log) {
            var iframe = document.createElement("IFRAME");
            iframe.setAttribute("src", "ios-log:#iOS#" + log);
            document.documentElement.appendChild(iframe);
            iframe.parentNode.removeChild(iframe);
            iframe = null;
        };
        console.warn = function(log) {
            console.log(log);
        };
        console.debug = function(log) {
            console.log(log);
        };
        console.error = function(log) {
            console.log(log);
        };
        console.info = function(log) {
            console.log(log);
        };
        console.trace = function(log) {
            console.log(log);
        };
    }
    window.bridge = mdSmartios.bridge;
    window.mdSmartios = mdSmartios
    mdSmartios.bridge.retObjcValue = 0;

    /*bridge.po._execObjcMethod('getCurrentDevSN');
    bridge.po._execObjcMethod('getCurrentApplianceID');
    bridge.po._execObjcMethod('getCurrentApplianceSubtype');*/
})(window,mdSmartios);
