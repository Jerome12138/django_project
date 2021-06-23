/**
 * @fileoverview meiju use bridge
 */
// import $ from 'jquery';

var mdSmartios = mdSmartios || {};
(function(mdSmartios) {
    if (mdSmartios.bridge) {
        console.log("mdSmartios.bridge is already defined.");
        return;
    }
    mdSmartios.bridge = mdSmartios.bridge || {};

    mdSmartios.bridge.storage={};

    mdSmartios.bridge.interfaceWrapper = function (name, paramOrigin, callback, callbackFail) {
        let param = Object.assign({}, paramOrigin);
        if (param == undefined || param == '') {
            param = {};
        }
        param.cammandId = Math.floor(Math.random() * 100000);
        var commandIds = param.cammandId;
        var p = JSON.stringify(param);
        if (typeof callback === 'function') {
            mdSmartios.bridge.callbackFunctions[commandIds] = callback;
        }

        if (typeof callbackFail === 'function') {
            mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
        }

        var commandId = mdSmartios.bridge.po._execObjcMethod(name, p);

        return commandId;
    };
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
	 * 获取网络状态(7.2）
	 * @return callback(result)
	 * result: {
	 * status:0, //0表示不可用，1表示可用
	 * type: 1 //0:非wifi, 1: wifi
	 * }
	 */
	mdSmartios.bridge.getNetworkStatus = function (param, callback, callbackFail) {
		return mdSmartios.bridge.interfaceWrapper('getNetworkStatus', param, callback, callbackFail);
	};
	/**
	 * 字节埋点接口(6.8）
	 * @param {json} param
	 */
	mdSmartios.bridge.trackEvent = function (param, callback, callbackFail) {
		mdSmartios.bridge.commandInterface('trackEvent', param, callback && callback, callbackFail && callbackFail);
	};

    /**
     * 保存图片至手机相册(6.6.1）
     * @param {json} param
     * {
        url: xxxx, //url为http开头的在线图片
        base64 //图片的base64数据
        }
     //url或者base64必填一个，若两者同时存在，优先url参数
     * @return {Number} 処理結果
     *                   -1，没有相册权限
     *
     */
    mdSmartios.bridge.imageSaveAs = function (param, callback, callbackFail) {
        return mdSmartios.bridge.interfaceWrapper('imageSaveAs', param, callback, callbackFail);
    };

    /**
     * #define getUserInfoBase64 @"getUserInfoBase64" 获取用户信息能力
     * @param {String} callback 处理成功后的回调函数
     * @param {String} callbackFail 后续处理异常时的回调函数
     * @param {intArray} messageBody 命令的整数数组
     * @return {Number} 命令ID 对数据进行base64编码
     *                    0以上 : 处理成功
     *                   -1     : 处理失败
     */
    mdSmartios.bridge.getUserInfoBase64 = function(callback) {
        console.log('function:mdSmartios.bridge.getUserInfoBase64: callback=' + callback);
        let param = {};
        let p = JSON.stringify(param);
        if (typeof callback === 'function') {
            mdSmartios.bridge.callbackUserInfo = callback;
        }
        let commandId = mdSmartios.bridge.po._execObjcMethod('getUserInfoBase64', p);
        return commandId;
    };

    /**
     * 权限判断与设置(6.6.1）
     * @param {json} param
     * {
        "type":"CAMERA"//根据不同的权限，传入不同的type
        }
     * @return {Number} 処理結果
     *                  callback ，当检查有权限时，执行成功回调。若没有权限，则不执行callback，APP会弹框引导用户去开启权限
     *
     */
    mdSmartios.bridge.checkAndRequestPermission = function (param, callback, callbackFail) {
        return mdSmartios.bridge.interfaceWrapper('checkAndRequestPermission', param, callback, callbackFail);
    };

    /**
     * 美居6.3.0 转换在线图片成base64数据
     * @param {*} param
     * {
     * url: xxxx, //url为http开头的在线图片
     * }
     * @param {*} callback
     * {base64: "xxxxxxxx"}
     * @param {*} callbackFail
     */
    mdSmartios.bridge.convertImageToBase64 = function (param, callback, callbackFail) {
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

        let commandId = mdSmartios.bridge.po._execObjcMethod('convertImageToBase64', p);

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
     * 美居6.4.0 拍照
     * @param {*} param
     * {
        compressRage: 0;//Number,返回照片的压缩率，范围为0~100，数值越高保真率越高
        "type": "";//值为jpg或png，指定返回相片的格式
        isNeedBase6: true/false;//是否需要返回相片base64数据
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
     * 美居6.4.0 选择照片(多选) 选择多张相册照片，并返回相片数据，不支持base64的转换
     * @param {*} param
     * {
        max: 9;//Number,max一次最多可选择的数量，默认为9，最多9张.
     * }
     * @param {*} callback
     * @param {*} callbackFail
     */
    mdSmartios.bridge.chooseMulPhoto = function (param, callback, callbackFail) {
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

        let commandId = mdSmartios.bridge.po._execObjcMethod('chooseMulPhoto', p);

        return commandId;
    };

    /**
     * 美居6.4.0 将手机本地的图片地址上传给指定服务器，返回线上图片地址
     * @param {*} param
     * {
        path: string, //值为 图片在手机中的路径
        url: string, //值为服务器上传图片的url
        maxWidth: number, //最大宽度，如果不设置，则使用图片宽度
        maxHeight: number, //最大高度，如果不设置，则使用图片高度
        compressRage: number, //图片的压缩率，范围为0~100，数值越高保真率越高。默认值：100，不压缩，直接上传图片 ps: 压缩后的图片文件格式，固定为jpg 格式
        netParam: {
        xxx: xxx, //weex需要原生填充给服务器的post 表单参数1
        xxx: xxx, //weex需要原生填充给服务器的post 表单参数2
        }
     * @param {*} callback
     * @param {*} callbackFail
     */
    mdSmartios.bridge.uploadImgFileToMas = function (param, callback, callbackFail) {
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

        let commandId = mdSmartios.bridge.po._execObjcMethod('uploadImgFileToMas', p);

        return commandId.url;//返回线上图片地址
    };

    /* H5调用原生拨打手机号
     * param = {
        phoneNumber: "", //手机号码
        cammandId: ""
     }
    */
    mdSmartios.bridge.makingCall = function(param, callback, callbackFail) {
        if (param == undefined || param == "") {
            param = {};
        }
        param.cammandId = Math.floor(Math.random() * 100000);
        let commandIds = param.cammandId;
        let p = JSON.stringify(param);
        console.log(p);

        if (typeof callback == "function") {
            bridge.callbackFunctions[commandIds] = callback;
        }

        if (typeof callbackFail == "function") {
            bridge.callbackFailFunctions[commandIds] = callbackFail;
        }

        let commandId = mdSmartios.bridge.po._execObjcMethod('makingCall', p);

        return commandId;
    };

    /* H5通过原生发送云端接口网络请求（mini网关） */
    /*  eg:
        params = {
            "url": "gateway/subdevice/list",
            "params": {
                "nodeId":xxx,
                "applianceId": xxx
            }
        }
    */
    mdSmartios.bridge.nativeNetService = function(param, callback, callbackFail) {
        if (param == undefined || param == "") {
            param = {};
        }
        if (param.url == undefined) {
            param.url = "";
        }
        if (param.params == undefined) {
            param.params = {};
        }
        param.cammandId = Math.floor(Math.random() * 1000);
        var commandIds = param.cammandId;
        var p = JSON.stringify(param);
        if (typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandIds] = callback;
        }

        if (typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
        }
        var commandId = mdSmartios.bridge.po._execObjcMethod('nativeNetService', p);

        return commandId;
    };

    /*AES128解密*/
    mdSmartios.bridge.decodeAES128 = function(code, callback, callbackFail) {
        var param = {};
        param.cammandId = Math.floor(Math.random() * 100000);
        param.code = code;
        var commandIds = param.cammandId;

        var p = JSON.stringify(param);
        console.log(p);

        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandIds] = callback;
        }

        if ( typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
        }

        var commandId = mdSmartios.bridge.po._execObjcMethod('decodeAES128', p);

        return commandId;
    };

    /**
     * H5 调用APP,取得家电SN
     * @return {Number}
     *                    0 : 成功
     *                   -1 : 失败(无插件)
     *                   -2 : 失败(无文件)
     */
    mdSmartios.bridge.getDeviceSN = function(callback, callbackFail) {
        var param={};
        param.cammandId = Math.floor(Math.random() * 1000);
        var commandIds = param.cammandId;
        var p = JSON.stringify(param);
        console.log(p);

        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandIds] = callback;
        }

        if ( typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
        }

        var commandId = mdSmartios.bridge.po._execObjcMethod('getDeviceSN', p);

        return commandId;
    };

    /**
     * H5 调用APP,取得家电id
     * @return {Number}
     *                    0 : 成功
     *                   -1 : 失败(无插件)
     *                   -2 : 失败(无文件)
     */
    mdSmartios.bridge.getApplianceID = function(callback, callbackFail) {
        var param={};
        param.cammandId = Math.floor(Math.random() * 1000);
        var commandIds = param.cammandId;
        var p = JSON.stringify(param);
        console.log(p);

        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandIds] = callback;
        }

        if ( typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
        }

        var commandId = mdSmartios.bridge.po._execObjcMethod('getApplianceID', p);

        return commandId;
    };

    /**
     * 存储数据到app内存中(JS->WebView）
     * @return {Number} 処理結果
     *                    0 : 成功
     *                   -1 : 失败(无插件)
     *                   -2 : 失败(无文件)
     */

    mdSmartios.bridge.setterValToStorage = function(key,value) {
        var p={};
        p[key]=value;
        mdSmartios.bridge.storage[key]= value;
        return  mdSmartios.bridge.po._execObjcMethod('setterVal',JSON.stringify(p));
    };

    /**
     * 从app内存中取得数据(JS->WebView）
     * @return {Number} 処理結果
     *                    0 : 成功
     *                   -1 : 失败(无插件)
     *                   -2 : 失败(无文件)
     */
    mdSmartios.bridge.getterValFromStorage = function(keyName, callback, callbackFail) {
        var param = {};
        param.keyName = keyName;
        param.cammandId = Math.floor(Math.random() * 1000);
        var commandIds = param.cammandId;

        var p = JSON.stringify(param);
        console.log(p);

        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandIds] = callback;
        }

        if ( typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
        }

        var commandId = mdSmartios.bridge.po._execObjcMethod('getterVal', p);

        return commandId;
    };

    /**
     * 处理从app内存中取数据的回调(WebView>JS)
     * @return {Number} 処理結果
     *                    0 : 成功
     *                   -1 : 失败(无插件)
     *                   -2 : 失败(无文件)
     */


    mdSmartios.bridge.putValueToStorage = function(keyName,value) {
        console.log("putValueToStorage: "+keyName+ " : "+value);
        mdSmartios.bridge.storage[keyName]=value;
    };

    mdSmartios.bridge.setValueToStorageValues = function(value){
        var jsLocalStorageJsonObj = JSON.parse(value);
        for(var key in jsLocalStorageJsonObj){
            mdSmartios.bridge.storage[key] = jsLocalStorageJsonObj[key];
        }
    }

    /**
     * H5 调用APP,取得家电子类型
     * @return {Number}
     *                    0 : 成功
     *                   -1 : 失败(无插件)
     *                   -2 : 失败(无文件)
     */
    mdSmartios.bridge.getApplianceSubtype = function(callback, callbackFail) {
        var param={};
        param.cammandId = Math.floor(Math.random() * 1000);
        var commandIds = param.cammandId;
        var p = JSON.stringify(param);
        console.log(p);

        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandIds] = callback;
        }

        if ( typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
        }

        var commandId = mdSmartios.bridge.po._execObjcMethod('getApplianceSubtype', p);

        return commandId;
    };

    /**
     * 向iOS写log(JS->WebView）
     * @param {String} logContent log内容
     */
    mdSmartios.bridge.logToIOS = function(logContent) {
        console.log("function:mdSmartios.bridge.logToIOS");
        return mdSmartios.bridge.po._execObjcMethod('logToIOS', logContent);
    };

    /*
     * 取得网络类型
     * return LAN或WAN
     */
    mdSmartios.bridge.getNetType = function() {
        console.log("function:mdSmartios.bridge.getNetType");
        return mdSmartios.bridge.po._execObjcMethod('getCommunicationMethod');
    };

    /*
     * 取得卡片页在同类卡片中的顺序
     * return 0:第1、3、5...，1:第2、4、6...
     */
    mdSmartios.bridge.getCardOrder = function() {
        console.log("function:mdSmartios.bridge.getCardOrder");
        return mdSmartios.bridge.po._execObjcMethod('getCardOrder');
    };

    /*
     * marco 修改：2015.12.10
     * 修改 取得设备SN
     * return 取得设备SN
     */
    mdSmartios.bridge.getCurrentDevSN = function() {
        console.log("function:mdSmartios.bridge.getCurrentDevSN");
        return mdSmartios.bridge.retSnValue || mdSmartios.bridge.po._execObjcMethod('getCurrentDevSN');
    };

    /*
     * marco 修改：2015.12.10
     * 修改 取得设备SN
     * 设置sn
     */
    mdSmartios.bridge.setSnValue = function(retObjcValue) {

        mdSmartios.bridge.retSnValue = retObjcValue;

    };

    /*
     * marco 修改：2015.12.10
     * 修改 取得设备子类型
     * 设置子类型
     */
    mdSmartios.bridge.setcurrentApplianceSubtype = function(retObjcValue) {

        mdSmartios.bridge.currentApplianceSubtype = retObjcValue;

    };

    /*
     * marco 修改：2015.12.10
     * 修改 取得设备id
     * 设置设备id
     */
    mdSmartios.bridge.setApplicationIdValue = function(retObjcValue) {

        mdSmartios.bridge.applicationId = retObjcValue;

    };

    /**
     * 取家电协议版本(JS->WebView）
     * @return {Number} 家电协议版本
     */
    mdSmartios.bridge.getApplianceProtocolVersion = function() {
        console.log("function:mdSmartios.bridge.getApplianceProtocolVersion");
        return mdSmartios.bridge.po._execObjcMethod('getApplianceProtocolVersion');
    };

    /**
     * 显示家电信息入口页(JS->WebView）
     * @return {Number} 処理結果
     *                    0 : 成功
     *                   -1 : 失败(无插件)
     *                   -2 : 失败(无文件)
     */
    mdSmartios.bridge.showApplianceInfoEntryPage = function() {
        console.log("function:mdSmartios.bridge.showApplianceInfoEntryPage");
        return mdSmartios.bridge.po._execObjcMethod('showApplianceInfoEntryPage');
    };

    /**
     * 显示家电信息页(JS->WebView）
     * @return {Number} 処理結果
     *                    0 : 成功
     *                   -1 : 失败(无插件)
     *                   -2 : 失败(无文件)
     */
    mdSmartios.bridge.showApplianceInfoPage = function() {
        console.log("function:mdSmartios.bridge.showApplianceInfoPage");
        return mdSmartios.bridge.po._execObjcMethod('showApplianceInfoPage');
    };

    /**
     * 显示消息中心页(JS->WebView）
     * @return {Number} 処理結果
     *                    0 : 成功
     *                   -1 : 失败(无插件)
     *                   -2 : 失败(无文件)
     */
    mdSmartios.bridge.showInfoCenterPage = function() {
        console.log("function:mdSmartios.bridge.showInfoCenterPage");
        return mdSmartios.bridge.po._execObjcMethod('showInfoCenterPage');
    };

    /**
     * 开始异步处理的命令
     * @param {String} callback 处理成功后的回调函数
     * @param {String} callbackFail 后续处理异常时的回调函数
     * @param {intArray} messageBody 命令的整数数组
     * @return {Number} 命令ID
     *                    0以上 : 处理成功
     *                   -1     : 处理失败
     */
    mdSmartios.bridge.startCmdProcess = function(messageBody, callback, callbackFail) {
        console.log('function:mdSmartios.bridge.startCmdProcess: messageBody=' + messageBody + ', callback=' + callback + ', callbackFail=' + callbackFail);
        var param = {};
        if (messageBody != undefined) {
            param.messageBody = messageBody;
        }

        var commandId = mdSmartios.bridge.startCmdProcessGo(param);

        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandId] = callback;
        }

        var isQuery=true;
        switch(messageBody[2]){
            case 0xea:
            case 0xeb:
            case 0xec:
            case 0xed:
            case 0xef:
                if((messageBody[18]<<8|messageBody[17])==50002){
                    isQuery=true;
                }else{
                    isQuery=false;
                }
                break;
            default:
                if(messageBody[9]==3){
                    isQuery=true;
                }else{
                    isQuery=false;
                }
        }
//keane 指令失败函数自定义
//        if(!isQuery){
//            if(typeof callbackFail != "function"){
//                callbackFail=function(){};
//            }
//        }

        if ( typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandId] = callbackFail;
        }


        return commandId;
    };

    /**
     * 开始异步处理的命令 可自定义Loading是否显示
     * @param {String} callback 处理成功后的回调函数
     * @param {String} callbackFail 后续处理异常时的回调函数
     * @param {intArray} messageBody 命令的整数数组
     * @param {bool} isLoading 是否显示loading阻塞界面
     * @return {Number} 命令ID
     *                    0以上 : 处理成功
     *                   -1     : 处理失败
     */
    mdSmartios.bridge.startCmdProcessCustomLoading = function(messageBody,isLoading, callback, callbackFail) {
        console.log('function:mdSmartios.bridge.startCmdProcess: messageBody=' + messageBody + ', callback=' + callback + ', callbackFail=' + callbackFail);
        var param = {};
        if (messageBody != undefined) {
            param.messageBody = messageBody;

        }

        if(isLoading != undefined){
            param.isLoading = isLoading;
        }

        var commandId = mdSmartios.bridge.startCmdProcessGo(param);

        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandId] = callback;
        }

//        if(typeof callbackFail != "function"){
//            callbackFail=function(){};
//        }

        if ( typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandId] = callbackFail;
        }

        return commandId;
    };

    /**
     * 开始异步处理的命令 真实发送接口
     * @param {intArray} param 发送的数据
     * @return {Number} 命令ID
     *                    0以上 : 处理成功
     *                   -1     : 处理失败
     */

    mdSmartios.bridge.startCmdProcessGo = function(param) {
        var p = JSON.stringify(param);
        var commandId = mdSmartios.bridge.po._execObjcMethod('startCmdProcess', p);
        return commandId;

    };


    /**
     * 针对管家插件 开始异步处理的命令
     * @param {String} callback 处理成功后的回调函数
     * @param {String} callbackFail 后续处理异常时的回调函数
     * @param {intArray} param 发送的数据
     * @return {Number} 命令ID
     *                    0以上 : 处理成功
     *                   -1    : 处理失败
     */

    mdSmartios.bridge.startCmdProcessExt = function(messageBody, callback, callbackFail) {
        console.log('function:mdSmartios.bridge.startCmdProcessExt: messageBody=' + messageBody + ', callback=' + callback + ', callbackFail=' + callbackFail);
        var param = {};
        if (messageBody != undefined) {
            param.messageBody = messageBody;
        }
        var p = JSON.stringify(param);
        var commandId = mdSmartios.bridge.po._execObjcMethod('startCmdProcessExt', p);
        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandId] = callback;
        }

        if(typeof callbackFail != "function"){
            callbackFail=function(){};
        }
        mdSmartios.bridge.callbackFailFunctions[commandId] = callbackFail;
        return commandId;
    };


    /**
     * 取消命令执行
     * @param {Number} commandId 命令ID
     * @return void
     * @note 不是处理中的时候,忽略
     */
    mdSmartios.bridge.stopCmdProcess = function(commandId) {
        console.log('function:mdSmartios.bridge.stopCmdProcess: commandId=' + commandId);
        var p = JSON.stringify({
            commandId : commandId
        });
        mdSmartios.bridge.po._execObjcMethod('stopCmdProcess', p);
    };

    /**
     * 取得命令执行状态
     * @param {Number} commandId 命令ID
     * @return {JSONObject} 命令执行状态
     *         {Number} .status 命令执行状态
     *                     0 : 未开始
     *                     1 : 进行中
     *                     2 : 结束
     *                    -1 : 异常
     *                    -2 : 取消
     *         {String} .errMessage 异常信息
     */
    mdSmartios.bridge.getCmdProcessInfo = function(commandId) {
        console.log('function:mdSmartios.bridge.getCmdProcessInfo: commandId=' + commandId);
        var p = JSON.stringify({
            commandId : commandId
        });
        return mdSmartios.bridge.po._execObjcMethod('getCmdProcessInfo', p);
    };

    /**
     * 取得卡片头部Tilte信息
     * @param {String} callback 处理成功后的回调函数
     * @return {Number} 命令ID
     *                    0以上 : 处理成功
     *                   -1     : 处理失败
     */
    mdSmartios.bridge.getCardTitle = function(callback) {
        console.log('function:mdSmartios.bridge.getCardTitle: callback=' + callback);
        var param = {};
        var p = JSON.stringify(param);
        if ( typeof callback == "function") {
            mdSmartios.bridge.setCardTitleCBF = callback;
        }
        var commandId = mdSmartios.bridge.po._execObjcMethod('getCardTitle', p);
        return commandId;
    };

    /**
     * 取得插件版本信息
     * @param {String} callback 处理成功后的回调函数
     * @return {Number} 命令ID
     *                    0以上 : 处理成功
     *                   -1     : 处理失败
     */
    mdSmartios.bridge.getPlugVersion = function() {
        console.log('function:mdSmartios.bridge.getPlugVersion');
        var param = {};
        var p = JSON.stringify(param);
        var version = mdSmartios.bridge.po._execObjcMethod('getPlugVersion', p);
        return version;
    };

    //配置文件
    mdSmartios.bridge.getConfigInfo = function(cmdParamers,callback) {
        console.log('function:mdSmartios.bridge.getConfigInfo: callback=' + callback);
        //var param = {"fileName":"0xDB"};
        cmdParamers.cammandId = Math.floor(Math.random() * 10000000);
        var commandId = cmdParamers.cammandId;
        var p = JSON.stringify(cmdParamers);
        if ( typeof callback == "function") {
            mdSmartios.bridge.setConfigInfoCBF[commandId] = callback;
        }
        var commandId = mdSmartios.bridge.po._execObjcMethod('getConfigInfo', p);
        return commandId;

    };

    mdSmartios.bridge.setConfigInfoCBF = {};
    mdSmartios.bridge.setConfigInfo = function(retObjcValue,message) {
        // var jsonResult = JSON.parse(message);
        var cbf = mdSmartios.bridge.setConfigInfoCBF[retObjcValue];

        if ( typeof cbf == "function") {
            //mdSmartios.bridge.setConfigInfoCBF(jsonResult.messageBody);
            cbf(message);
        }
        delete mdSmartios.bridge.setConfigInfoCBF[retObjcValue];
    };

    //配置文件排序
    mdSmartios.bridge.getSort = function(callback) {
        console.log('function:mdSmartios.bridge.getSort: callback=' + callback);
        var param = {
            "isWritestr":0,
            "fileName":"cycleArray"
        };
        var p = JSON.stringify(param);
        if ( typeof callback == "function") {
            mdSmartios.bridge.setSortCBF = callback;
        }
        var commandId = mdSmartios.bridge.po._execObjcMethod('getSort', p);
        return commandId;
    };

    mdSmartios.bridge.setSortCBF = undefined;
    mdSmartios.bridge.setSort = function(message) {
        if ( typeof mdSmartios.bridge.setSortCBF == "function") {
            mdSmartios.bridge.setSortCBF(message);
        }
    };


    /**
     * 取得语言Code
     * @return {String} 语言Code
     *                    zh : 中国语
     *                    en : 英语
     */
    mdSmartios.bridge.getLangCode = function() {
        console.log('function:mdSmartios.bridge.getLangCode');
        var param = {};
        var p = JSON.stringify(param);

        var langCode = mdSmartios.bridge.po._execObjcMethod('getLangCode', p);

        if (langCode == undefined || langCode == 0 || langCode.length == 0) {
            langCode = "zh";
        }
        return langCode;
    };

    /*
     * marco 修改：2015.12.10
     * 修改 取得当前家电id
     * return 取得当前家电id
     */
    mdSmartios.bridge.getCurrentApplianceID = function() {
        //var currentApplicanceID = mdSmartios.bridge.po._execObjcMethod('getCurrentApplianceID');

        return mdSmartios.bridge.applicationId || mdSmartios.bridge.po._execObjcMethod('getCurrentApplianceID');
    };

    /**
     * 取得当前家电子类型
     * @return {String}
     */
    mdSmartios.bridge.getCurrentApplianceSubtype = function() {

        return mdSmartios.bridge.currentApplianceSubtype;
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

    /**
     * 输出日志
     */
    mdSmartios.bridge.jsWindowOnError = function(obj, arg1, arg2, arg3) {
        var param = {
            obj : obj,
            arg1 : arg1,
            arg2 : arg2,
            arg3 : arg3
        };
        var p = JSON.stringify(param);
        console.log('mdSmartios.bridge.jsWindowOnError():' + p);
    };
    //IOS主动上报的消息-设备连接状态(IOS调用：主动发起)
    //pIsConnect 1:连接成功 0:断开连接
    mdSmartios.bridge.setApplianceConnnectStatus = function(pIsConnect) {
        mdSmartios.bridge.isApplianceConnected = parseInt(pIsConnect);
        if (0x01 == mdSmartios.bridge.isApplianceConnected) {
            for (var index in mdSmartios.bridge.applianceConnectedEvents) {
                var item = mdSmartios.bridge.applianceConnectedEvents[index];
                if ( typeof item == "object") {
                    item.fire();
                }
            }
        } else {
            for (var index in mdSmartios.bridge.applianceDisconnectedEvents) {
                var item = mdSmartios.bridge.applianceDisconnectedEvents[index];
                if ( typeof item == "object") {
                    item.fire();
                }
            }
        }
    };

    /**
     *  管家接口
     *
     */
    mdSmartios.bridge.callbackUserInfo = undefined;
    mdSmartios.bridge.callbackAppInfo = undefined;
    mdSmartios.bridge.callbackUserApplianceList = undefined;
    mdSmartios.bridge.callbackUserHomeInfo = undefined;
    mdSmartios.bridge.callbackRequestDataTransmit = {};
    mdSmartios.bridge.callbackFailRequestDataTransmit = {};
    mdSmartios.bridge.commandIds = {};
    mdSmartios.bridge.callbackGPSInfo = undefined;
    mdSmartios.bridge.callbackQrCode = undefined;
    mdSmartios.bridge.callbackJumpPlugin = undefined;
    mdSmartios.bridge.callbackLvmiDeviceInfo = undefined;

    //获取空调伴侣页面初始信息
    mdSmartios.bridge.getLvmiDeviceInfo = function(callback) {
        console.log('function:mdSmartios.bridge.getLvmiDeviceInfo: callback=' + callback);
        var param = {};
        var p = JSON.stringify(param);
        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackLvmiDeviceInfo = callback;
        }
        var commandId = mdSmartios.bridge.po._execObjcMethod('getLvmiDeviceInfo', p);
        return commandId;
    };

    mdSmartios.bridge.setLvmiDeviceInfo = function(message) {
        // alert(message);
        // var jsonResult = JSON.parse(message);
        if ( typeof mdSmartios.bridge.callbackLvmiDeviceInfo == "function") {
            mdSmartios.bridge.callbackLvmiDeviceInfo(message);
        }
    };

    //GPS信息获取 JS－>iOS
    mdSmartios.bridge.getGPSInfo = function(callback) {
        console.log('function:mdSmartios.bridge.getGPSInfo: callback=' + callback);
        var param = {};
        var p = JSON.stringify(param);
        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackGPSInfo = callback;
        }
        var commandId = mdSmartios.bridge.po._execObjcMethod('getGPSInfo', p);
        return commandId;
    };

    //GPS信息能力(IOS调用：回复getGPSInfo)
    mdSmartios.bridge.setGPSInfo = function(message) {
        var jsonResult = JSON.parse(message);
        if ( typeof mdSmartios.bridge.callbackGPSInfo == "function") {
            mdSmartios.bridge.callbackGPSInfo(jsonResult.messageBody);
        }
    };

    //扫码功能 JS－>iOS
    mdSmartios.bridge.qrCodeScan = function(callback) {
        console.log('function:mdSmartios.bridge.qrCodeScan: callback=' + callback);
        var param = {};
        var p = JSON.stringify(param);
        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackQrCode = callback;
        }
        var commandId = mdSmartios.bridge.po._execObjcMethod('qrCodeScan', p);
        return commandId;
    };

    //扫码功能(IOS调用：回复qrCodeScan)
    mdSmartios.bridge.setQrCode = function(message) {
        var jsonResult = JSON.parse(message);
        if ( typeof mdSmartios.bridge.callbackQrCode == "function") {
            mdSmartios.bridge.callbackQrCode(JSON.stringify(jsonResult.messageBody));
        }
    };

    //跳转功能 JS－>iOS
    mdSmartios.bridge.jumpOtherPlugin = function(cmdParamers,callback) {
        console.log('function:mdSmartios.bridge.jumpOtherPlugin');
        var param = {};
        if (cmdParamers != undefined) {
            param.cmdParamers = cmdParamers;
        }
        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackJumpPlugin = callback;
        }

        var p = JSON.stringify(param);
        var commandId = mdSmartios.bridge.po._execObjcMethod('jumpOtherPlugin', p);
        return commandId;
    };

    //跳转功能(IOS调用：回复jumpOtherPlugin)
    mdSmartios.bridge.jumpOtherPluginCB = function(message) {
        var jsonResult = JSON.parse(message);
        if ( typeof mdSmartios.bridge.callbackJumpPlugin == "function") {
            mdSmartios.bridge.callbackJumpPlugin(jsonResult.messageBody);
        }
    };

    /**
     * #define GetUserInfo @"getUserInfo" 获取用户信息能力
     * @param {String} callback 处理成功后的回调函数
     * @param {String} callbackFail 后续处理异常时的回调函数
     * @param {intArray} messageBody 命令的整数数组
     * @return {Number} 命令ID
     *                    0以上 : 处理成功
     *                   -1     : 处理失败
     */
    mdSmartios.bridge.getUserInfo = function(callback) {
        console.log('function:mdSmartios.bridge.getUserInfo: callback=' + callback);
        var param = {};
        var p = JSON.stringify(param);
        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackUserInfo = callback;
        }
        var commandId = mdSmartios.bridge.po._execObjcMethod('getUserInfo', p);
        return commandId;
    };

    //用户信息能力(IOS调用：回复getUserInfo)
    mdSmartios.bridge.setUserInfo = function(message) {
        var jsonResult = JSON.parse(message);
        if ( typeof mdSmartios.bridge.callbackUserInfo == "function") {
            mdSmartios.bridge.callbackUserInfo(jsonResult.messageBody);
        }
    };

    /**
     * #define GetAppInfo @"getAppInfo" 获取用户信息能力
     * @param {String} callback 处理成功后的回调函数
     * @param {String} callbackFail 后续处理异常时的回调函数
     * @param {intArray} messageBody 命令的整数数组
     * @return {Number} 命令ID
     *                    0以上 : 处理成功
     *                   -1     : 处理失败
     */
    mdSmartios.bridge.getAppInfo = function(callback) {
        console.log('function:mdSmartios.bridge.getAppInfo: callback=' + callback);
        var param = {};
        var p = JSON.stringify(param);
        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackAppInfo = callback;
        }
        var commandId = mdSmartios.bridge.po._execObjcMethod('getAppInfo', p);
        return commandId;
    };
    //用户信息能力(IOS调用：回复getAppInfo)
    mdSmartios.bridge.setAppInfo = function(message) {
        var jsonResult = JSON.parse(message);
        if ( typeof mdSmartios.bridge.callbackAppInfo == "function") {
            mdSmartios.bridge.callbackAppInfo(jsonResult.messageBody);
        }
    };
    /**
     * #define GetUserApplianceList @"getUserApplianceList" 获取用户家电列表
     * @param {String} callback 处理成功后的回调函数
     * @param {String} callbackFail 后续处理异常时的回调函数
     * @param {intArray} messageBody 命令的整数数组
     * @return {Number} 命令ID
     *                    0以上 : 处理成功
     *                   -1     : 处理失败
     */
    mdSmartios.bridge.getUserApplianceList = function(callback) {
        console.log('function:mdSmartios.bridge.getUserApplianceList: callback=' + callback);
        var param = {};
        var p = JSON.stringify(param);
        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackUserApplianceList = callback;
        }
        var commandId = mdSmartios.bridge.po._execObjcMethod('getUserApplianceList', p);
        return commandId;
    };

    //用户家电列表(IOS调用：回复getUserApplianceList)
    mdSmartios.bridge.setUserApplianceList = function(message) {
        var jsonResult = JSON.parse(message);
        if ( typeof mdSmartios.bridge.callbackUserApplianceList == "function") {
            mdSmartios.bridge.callbackUserApplianceList(jsonResult.messageBody);
        }
    };

    /**
     * #define GetUserHomeInfo @"getUserHomeInfo"  获取用户家庭信息
     * @param {String} callback 处理成功后的回调函数
     * @param {String} callbackFail 后续处理异常时的回调函数
     * @param {intArray} messageBody 命令的整数数组
     * @return {Number} 命令ID
     *                    0以上 : 处理成功
     *                   -1     : 处理失败
     */
    mdSmartios.bridge.getUserHomeInfo = function(callback) {
        console.log('function:mdSmartios.bridge.getUserHomeInfo:callback=' + callback);
        var param = {};
        var p = JSON.stringify(param);
        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackUserHomeInfo = callback;
        }
        var commandId = mdSmartios.bridge.po._execObjcMethod('getUserHomeInfo', p);
        return commandId;
    };

    //用户家庭信息(IOS调用：回复getUserHomeInfo)
    mdSmartios.bridge.setUserHomeInfo = function(message) {
        var jsonResult = JSON.parse(message);
        if ( typeof mdSmartios.bridge.callbackUserHomeInfo == "function") {
            mdSmartios.bridge.callbackUserHomeInfo(jsonResult.messageBody);
        }
    };

    //用户家庭信息(IOS调用：回复getUserHomeInfo)
    mdSmartios.bridge.setDataTransmit = function(retObjcValue, result) {
        var jsonResult = JSON.parse(result);
        var cbf = mdSmartios.bridge.callbackRequestDataTransmit[retObjcValue];
        var cbff = mdSmartios.bridge.callbackFailRequestDataTransmit[retObjcValue];
        {
            if ( typeof cbf == "function") {

                cbf(jsonResult.messageBody);
            }
        }
        delete mdSmartios.bridge.callbackRequestDataTransmit[retObjcValue];
        delete mdSmartios.bridge.callbackFailRequestDataTransmit[retObjcValue];
    };

    /**
     * 购买耗材(JS->WebView）
     * @param {json} pageParamers  参数
     * @return {Number} 处理結果
     *                    0 : 成功
     *                   -1 : 失败
     *
     */
    mdSmartios.bridge.buyConsumable = function(pageParamers) {
        console.log("function:mdSmartios.bridge.buyConsumable");
        var p = JSON.stringify({
            pageParameters : pageParamers
        });
        return mdSmartios.bridge.po._execObjcMethod('buyConsumable', p);
    };


    /**
     * #define RequestDataTransmit @"requestDataTransmit" 请求通用数据接口能力
     * @param {String} callback 处理成功后的回调函数
     * @param {String} callbackFail 后续处理异常时的回调函数
     * @param {intArray} messageBody 命令的整数数组
     * @return {Number} 命令ID
     *                    0以上 : 处理成功
     *                   -1     : 处理失败
     */
    mdSmartios.bridge.requestDataTransmit = function(cmdParamers, callback, callbackFail) {
        var param = {};
        if (cmdParamers != undefined) {
            param.cmdParamers = cmdParamers;
        }
        param.cammandId = Math.floor(Math.random() * 10000000);
        var p = JSON.stringify(param);
        var commandId = mdSmartios.bridge.po._execObjcMethod('requestDataTransmit', p);
        //if (isAndroid) {
        commandId = param.cammandId;
        //}
        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackRequestDataTransmit[commandId] = callback;
        }

        callbackFail=function(){};
        mdSmartios.bridge.callbackFailRequestDataTransmit[commandId] = callbackFail;
        return commandId;
    };

    /**
     * H5 调用APP,取得家电id
     * @return {Number}
     *                    0 : 成功
     *                   -1 : 失败(无插件)
     *                   -2 : 失败(无文件)
     */
    mdSmartios.bridge.getApplianceIDTX = function(callback, callbackFail) {
        var param={};
        param.cammandId = Math.floor(Math.random() * 1000);
        var commandIds = param.cammandId;
        var p = JSON.stringify(param);
        console.log(p);

        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandIds] = callback;
        }

        if ( typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
        }
        var commandId = mdSmartios.bridge.po._execObjcMethod('getApplianceIDTX', p);

        return commandId;
    };

    /**
     * 获取设备在线离线状态
     * @param {Object} deviceId
     * @param {Object} callback
     * @param {Object} callbackFail
     */
    mdSmartios.bridge.getDeviceOnlineStatus = function(deviceId,callback, callbackFail) {
        var param={};
        param.cammandId = Math.floor(Math.random() * 1000);
        param.deviceId = deviceId;
        var commandIds = param.cammandId;
        var p = JSON.stringify(param);
        console.log(p);

        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandIds] = callback;
        }

        if ( typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
        }
        var commandId = mdSmartios.bridge.po._execObjcMethod('getDeviceOnlineStatus', p);

        return commandId;
    };

    /**
     * H5 调用APP,取得套系列表
     * @return {Number}
     *                    0 : 成功
     *                   -1 : 失败(无插件)
     *                   -2 : 失败(无文件)
     */
    mdSmartios.bridge.getTXList = function(callback, callbackFail) {
        var param={};
        param.cammandId = Math.floor(Math.random() * 1000);
        var commandIds = param.cammandId;
        var p = JSON.stringify(param);
        console.log(p);

        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandIds] = callback;
        }

        if ( typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
        }
        var commandId = mdSmartios.bridge.po._execObjcMethod('getTXList', p);

        return commandId;
    };

    mdSmartios.bridge.getDeviceName = function(deviceId,callback, callbackFail) {
        var param={};
        param.cammandId = Math.floor(Math.random() * 1000);
        param.deviceId = deviceId;
        var commandIds = param.cammandId;
        var p = JSON.stringify(param);
        console.log(p);


        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandIds] = callback;
        }

        if ( typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
        }
        var commandId = mdSmartios.bridge.po._execObjcMethod('getDeviceName', p);

        return commandId;
    };

    mdSmartios.bridge.getApplianceSubtypeTX = function(deviceId,callback, callbackFail) {
        var param={};
        param.cammandId = Math.floor(Math.random() * 1000);
        param.deviceId = deviceId;
        var commandIds = param.cammandId;
        var p = JSON.stringify(param);
        console.log(p);


        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandIds] = callback;
        }

        if ( typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
        }
        var commandId = mdSmartios.bridge.po._execObjcMethod('getApplianceSubtypeTX', p);

        return commandId;
    };

    mdSmartios.bridge.getApplianceType = function(deviceId,callback, callbackFail) {
        var param={};
        param.cammandId = Math.floor(Math.random() * 1000);
        param.deviceId = deviceId;
        var commandIds = param.cammandId;
        var p = JSON.stringify(param);
        console.log(p);


        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandIds] = callback;
        }

        if ( typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
        }
        var commandId = mdSmartios.bridge.po._execObjcMethod('getApplianceType', p);

        return commandId;
    };

    mdSmartios.bridge.getDeviceSNTX = function(deviceId,callback, callbackFail) {
        var param={};
        param.cammandId = Math.floor(Math.random() * 1000);
        param.deviceId = deviceId;
        var commandIds = param.cammandId;
        var p = JSON.stringify(param);
        console.log(p);


        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandIds] = callback;
        }

        if ( typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
        }
        var commandId = mdSmartios.bridge.po._execObjcMethod('getDeviceSNTX', p);

        return commandId;
    };

    /**
     * 开始异步处理的命令
     * @param {String} callback 处理成功后的回调函数
     * @param {String} callbackFail 后续处理异常时的回调函数
     * @param {intArray} messageBody 命令的整数数组
     * @return {Number} 命令ID
     *                    0以上 : 处理成功
     *                   -1     : 处理失败
     */
    mdSmartios.bridge.startCmdProcessTX = function(messageBody,deviceId, callback, callbackFail) {
        console.log('function:mdSmartios.bridge.startCmdProcess: messageBody=' + messageBody + ', callback=' + callback + ', callbackFail=' + callbackFail);
        var param = {};
        if (messageBody != undefined) {
            param.messageBody = messageBody;
        }
        param.deviceId = deviceId;
        //param.cammandId = Math.floor(Math.random() * 1000);
        //var commandIds = param.cammandId;
        var p = JSON.stringify(param);
        var commandId = mdSmartios.bridge.startCmdProcessGo(param);


        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandId] = callback;
        }

        var isQuery=true;
        switch(messageBody[2]){
            case 0xea:
            case 0xeb:
            case 0xec:
            case 0xed:
            case 0xef:
                if((messageBody[18]<<8|messageBody[17])==50002){
                    isQuery=true;
                }else{
                    isQuery=false;
                }
                break;
            default:
                if(messageBody[9]==3){
                    isQuery=true;
                }else{
                    isQuery=false;
                }
        }
//keane 指令失败函数自定义
//        if(!isQuery){
//            if(typeof callbackFail != "function"){
//                callbackFail=function(){};
//            }
//        }

        if ( typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandId] = callbackFail;
        }


        return commandId;
    };

    /**
     * #define RequestDataTransmitTX @"requestDataTransmitTX" 请求通用数据接口能力
     * @param {String} callback 处理成功后的回调函数
     * @param {String} callbackFail 后续处理异常时的回调函数
     * @param {intArray} messageBody 命令的整数数组
     * @return {Number} 命令ID
     *                    0以上 : 处理成功
     *                   -1     : 处理失败
     */
    mdSmartios.bridge.requestDataTransmitTX = function(cmdParamers,deviceId, callback, callbackFail) {
        var param = {};
        if (cmdParamers != undefined) {
            param.cmdParamers = cmdParamers;
            param.deviceId = deviceId;
        }
        param.cammandId = Math.floor(Math.random() * 10000000);
        var p = JSON.stringify(param);

        //if (isAndroid) {
        var commandIds = param.cammandId;
        //}
        if ( typeof callback == "function") {
            mdSmartios.bridge.callbackRequestDataTransmit[commandIds] = callback;
        }

        callbackFail=function(){};
        mdSmartios.bridge.callbackFailRequestDataTransmit[commandIds] = callbackFail;

        var commandId = mdSmartios.bridge.po._execObjcMethod('requestDataTransmit', p);
        return commandId;
    };

    //设置是否监控安卓手机物理返回键功能
    /* 若设置的监控返回键，用户按了返回键后通过, app -> 插件:
       receiveMessageFromApp({ messageType: "hardwareBackClick", messageBody: {} })
    */
    mdSmartios.bridge.setBackHandle = function (param,callback, callbackFail) {
        param.cammandId = Math.floor(Math.random() * 1000);
        var commandIds = param.cammandId;
        var p = JSON.stringify(param);
        var commandId = mdSmartios.bridge.po._execObjcMethod('setBackHandle', p);

        if (typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandIds] = callback;
        }

        if (typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
        }

        return commandId;
    };
    /**
     * 获取当前家庭的信息(^5.2.0)
     * @param {Object} callback
     * @param {Object} callbackFail
     * @return {Object} {"messageBody":{
        "homeId": "123456",
        "homeName": "林首富之家",
        "isOwner": "1", //0表示非主人，1表示主人
        deviceList: [{
        "deviceId": "xxxxx", //设备ID
        "deviceName": "xxxxxx", //设备名
        "deviceType": "xxxx", //设备类型
        "deviceSubType": "xxxxx",//设备子类型
        "deviceSn": "xxxxxxxxx"//设备SN
        "isOnline": 1, //设备是否在线，1：在线，0：离线}]
        "isLocal": 0, //是否是本地家庭，1：是，0：否
        }}
     */
    mdSmartios.bridge.getCurrentHomeInfo = function (callback, callbackFail) {
        var param = {};
        param.cammandId = Math.floor(Math.random() * 1000);
        var commandIds = param.cammandId;
        var p = JSON.stringify(param);
        console.log(p);

        if (typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandIds] = callback;
        }

        if (typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
        }
        var commandId = mdSmartios.bridge.po._execObjcMethod('getCurrentHomeInfo', p);

        return commandId;
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

    //loading 显示
    mdSmartios.bridge.showProgress = function() {
        console.log("function:mdSmartios.bridge.showProgress");
        return mdSmartios.bridge.po._execObjcMethod('showProgress');
    };

    //loading 取消
    mdSmartios.bridge.closeProgress = function() {
        console.log("function:mdSmartios.bridge.closeProgress");
        return mdSmartios.bridge.po._execObjcMethod('closeProgress');
    };

    //打开网页， cmdParamers为网页url，如http://www.baidu.com
    mdSmartios.bridge.openWeb = function(url) {
        console.log('function:mdSmartios.bridge.openWeb');
        var param = {};
        if (url != undefined) {
            param.cmdParamers = url;
        }

        var p = JSON.stringify(param);
        var commandId = mdSmartios.bridge.po._execObjcMethod('openWeb', p);
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
    /*
  *IoT通用透传网络请求接口
  * param = {
          url: 'gateway/subdevice/search', //云端api 接口
          params: {} //请求参数
          cammandId: "232"
  }
  */
    mdSmartios.bridge.sendMCloudRequest = function (param, callback, callbackFail) {
        if (param == undefined || param == "") {
            param = {};
        }
        param.cammandId = Math.floor(Math.random() * 100000);
        var commandIds = param.cammandId;
        var p = JSON.stringify(param);
        console.log(p);

        if (typeof callback == "function") {
            bridge.callbackFunctions[commandIds] = callback;
        }

        if (typeof callbackFail == "function") {
            bridge.callbackFailFunctions[commandIds] = callbackFail;
        }

        var commandId = mdSmartios.bridge.po._execObjcMethod('sendMCloudRequest', p);

        return commandId;
    };

    /*
     *美居5.0 移动中台通用透传网络请求接口
     *param : {
     url: 'gateway/subdevice/search', //请求接口路径,
     method: 'POST', //POST/GET, 默认POST
     headers: {}, //请求header
     data: {} //请求参数
     }
     */
    mdSmartios.bridge.sendCentralCloundRequest = function (param, callback, callbackFail) {
        if (param == undefined || param == "") {
            param = {};
        }
        param.cammandId = Math.floor(Math.random() * 100000);
        let commandIds = param.cammandId;
        let p = JSON.stringify(param);
        console.log(p);

        if (typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandIds] = callback;
        }

        if (typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
        }

        let commandId = mdSmartios.bridge.po._execObjcMethod('sendCentralCloundRequest', p);

        return commandId;
    };
    /*
     *美居5.0 获取状态栏信息
     result: {
        isDisplay: true/false, //当前APP端是否控制了状态栏区域。true:状态栏高度属于APP控制，false:状态栏高度属于H5，即全屏满屏为H5区域
        height: xx， //状态栏高度，单位px，用于插件适配状态栏
        }
     */
    mdSmartios.bridge.getStatusBar = function (callback, callbackFail) {
        var param = {};
        param.cammandId = Math.floor(Math.random() * 100000);
        var commandIds = param.cammandId;

        var p = JSON.stringify(param);
        if (typeof callback == "function") {
            bridge.callbackFunctions[commandIds] = callback;
        }

        if (typeof callbackFail == "function") {
            bridge.callbackFailFunctions[commandIds] = callbackFail;
        }

        var commandId = mdSmartios.bridge.po._execObjcMethod('getStatusBar', p);

        return commandId;
    };
    /*
     *美居5.0 设置状态栏
     param:{
        isDisplay: true/false, //选填参数，设置是否显示状态栏，true:状态栏高度属于APP控制，false:状态栏高度属于H5
        bgColor: "#ffffff", //选填参数，设置状态栏背景颜色
        colorMode: "1", //选填参数，设置状态栏字体颜色模式，1：黑色字体色系模式，2：白色字体色系模式
        }
     */
    mdSmartios.bridge.setStatusBar = function (param, callback, callbackFail) {
        if (param == undefined || param == "") {
            param = {};
        }
        param.cammandId = Math.floor(Math.random() * 100000);
        var commandIds = param.cammandId;
        var p = JSON.stringify(param);
        if (typeof callback == "function") {
            bridge.callbackFunctions[commandIds] = callback;
        }

        if (typeof callbackFail == "function") {
            bridge.callbackFailFunctions[commandIds] = callbackFail;
        }

        var commandId = mdSmartios.bridge.po._execObjcMethod('setStatusBar', p);

        return commandId;
    };
    /*
     美居5.0 设置底部安全区域（iOS）
     param:{
         isDisplay: true/false, //选填参数，设置是否显示下面安全区域，true:下面安全区域高度属于APP控制，false:下面安全区域高度属于H5
           bgColor: "#ffffff", //选填参数，设置下面安全区域背景颜色
        }
     */
    mdSmartios.bridge.setBottomStatusBar = function (param, callback, callbackFail) {
        if (param == undefined || param == "") {
            param = {};
        }
        param.cammandId = Math.floor(Math.random() * 100000);
        var commandIds = param.cammandId;
        var p = JSON.stringify(param);
        if (typeof callback == "function") {
            bridge.callbackFunctions[commandIds] = callback;
        }

        if (typeof callbackFail == "function") {
            bridge.callbackFailFunctions[commandIds] = callbackFail;
        }

        var commandId = mdSmartios.bridge.po._execObjcMethod('setBottomStatusBar', p);

        return commandId;
    };
    /*
     城市定位接口：获取GPS定位所在城市名、ID以入经纬度和所选择的天气城市的信息。
     */
    mdSmartios.bridge.cityLocation = function (callback, callbackFail) {
        var param = {};
        param.cammandId = Math.floor(Math.random() * 100000);
        var commandIds = param.cammandId;

        var p = JSON.stringify(param);
        if (typeof callback == "function") {
            bridge.callbackFunctions[commandIds] = callback;
        }

        if (typeof callbackFail == "function") {
            bridge.callbackFailFunctions[commandIds] = callbackFail;
        }

        var commandId = mdSmartios.bridge.po._execObjcMethod('cityLocation', p);

        return commandId;
    };
    /*
     *设置活动页右上角菜单项
     *param{
     *   items:[{
     *     key: string, //菜单标示
     *     icon: url, //菜单icon的在线URL
     *     desc: string, //菜单描述，若没有配置icon则显示描述
     *  }]
     * }
     *  参数items为数组：最前面的排最右边
     *   当参数items为空数组时，则隐藏菜单
     * receiveMessageFromApp({ messageType: "menuItemClick", messageBody: { key: "xxxx" } }) //xxx为传入的菜单项key
     */
    mdSmartios.bridge.setupMenu = function (param, callback, callbackFail) {
        if (param == undefined || param == "") {
            param = {};
        }
        param.cammandId = Math.floor(Math.random() * 100000);
        var commandIds = param.cammandId;
        var p = JSON.stringify(param);
        if (typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandIds] = callback;
        }

        if (typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
        }

        var commandId = mdSmartios.bridge.po._execObjcMethod('setupMenu', p);

        return commandId;
    };

    /**
     * 打开分享窗口(JS->WebView）
     * @param {json} param  分享的参数
     * {
        "types": ["wx","wxTimeline"], //分享类型数组，wx表示微信分享，qq表示qq分享，sms表示短信分享，weibo表示新浪微博，qzone表示QQ空间，wxTimeline表示微信朋友圈
        "title": "xxxxxx", //分享的标题
        "desc": "xxxxxx",//分享的文本内容
        "imgUrl": "xxxxxx",//分享的图片链接
        "link": "xxxxxx", //分享的跳转链接
        }
     * @return {Number} 処理結果
     *                    0 : 打开成功
     *                   -1 : 打开失败
     *
     当收点击某个分享项时，app -> 插件:
     receiveMessageFromApp({ messageType: "shareItemClick", messageBody: { type: "xxxx" } }) //xxx为传入的菜单项types之一
     *
     */
    mdSmartios.bridge.showSharePanel = function (param, callback, callbackFail) {
        if (param == undefined || param == "") {
            param = {};
        }
        param.cammandId = Math.floor(Math.random() * 100000);
        var commandIds = param.cammandId;
        var p = JSON.stringify(param);
        if (typeof callback == "function") {
            mdSmartios.bridge.callbackFunctions[commandIds] = callback;
        }

        if (typeof callbackFail == "function") {
            mdSmartios.bridge.callbackFailFunctions[commandIds] = callbackFail;
        }

        var commandId = mdSmartios.bridge.po._execObjcMethod('showSharePanel', p);

        return commandId;
    };

    //JS监听设备的连接状态
    //eventType   "connected"   :连接
    //            "disconnected":断开连接
    mdSmartios.bridge.isApplianceConnected = 0x01;
    mdSmartios.bridge.applianceConnectedEvents = [];
    mdSmartios.bridge.applianceDisconnectedEvents = [];
    mdSmartios.bridge.appliance = function() {
        function commonEvent() {
            this.handler
        };
        commonEvent.prototype = {
            addHandler : function(handler) {
                this.handler = handler;
            },
            fire : function() {
                this.handler();
            },
            removeHandler : function() {
                this.handler = null;
            }
        };
        //eventType-connected
        var _connectedEvent = new commonEvent();
        //eventType-disconnected
        var _disconnectedEvent = new commonEvent();
        return {
            bind : function(eventType, handler) {
                if (eventType == "connected") {
                    for (var i in mdSmartios.bridge.applianceConnectedEvents) {
                        if (mdSmartios.bridge.applianceConnectedEvents[i] == _connectedEvent) {
                            delete mdSmartios.bridge.applianceConnectedEvents[i];
                        }
                    }
                    _connectedEvent.addHandler(handler);
                    mdSmartios.bridge.applianceConnectedEvents.push(_connectedEvent);
                }
                if (eventType == "disconnected") {
                    for (var i in mdSmartios.bridge.applianceDisconnectedEvents) {
                        if (mdSmartios.bridge.applianceDisconnectedEvents[i] == _disconnectedEvent) {
                            delete mdSmartios.bridge.applianceDisconnectedEvents[i];
                        }
                    }
                    _disconnectedEvent.addHandler(handler);
                    mdSmartios.bridge.applianceDisconnectedEvents.push(_disconnectedEvent);
                }
            },
            unbind : function(eventType) {
                if (eventType == "connected" || eventType == undefined) {
                    for (var i in mdSmartios.bridge.applianceConnectedEvents) {
                        if (mdSmartios.bridge.applianceConnectedEvents[i] == _connectedEvent) {
                            delete mdSmartios.bridge.applianceConnectedEvents[i];
                        }
                    }
                }
                if (eventType == "disconnected" || eventType == undefined) {
                    for (var i in mdSmartios.bridge.applianceDisconnectedEvents) {
                        if (mdSmartios.bridge.applianceDisconnectedEvents[i] == _disconnectedEvent) {
                            delete mdSmartios.bridge.applianceDisconnectedEvents[i];
                        }
                    }
                }
            },
            request : function() {
                mdSmartios.bridge.setApplianceConnnectStatus(mdSmartios.bridge.isApplianceConnected);
            }
        };
    };

    /**

     * 判断是否为安卓系统
     * @author Jun
     */
    if (!mdSmartios.bridge.isAndroid) {
        var u = navigator.userAgent;
        mdSmartios.bridge.isAndroid = u.indexOf('Android') > -1 || u.indexOf('Linux') > -1;
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
