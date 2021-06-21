

//添加门动画
    setTimeout(function(){
        $('.door_left').addClass("openLeft");
        $('.door_right').addClass("openRight");
    }, 1000);

    setTimeout(function(){
        $(".bImg3").addClass("bImg_ani3");
        $(".rightcircle").addClass("rightcicle_ani");

        var begin; var i=1;
        setInterval(function(){
            i++;
            begin = $(".index_ani").attr("src","imgs/index/tub00"+i+".png");
            if(i==7){ i=0}
        }, 500);

        var j=0;var array=[63,65,78,82,58,66,81];
        setInterval(function(){
            j++;
            $(".wdP").eq(j-1).addClass("word"+(j+1));//添加class让分值显示
            $(".word"+(j+1)).html(array[j]);//替换分值
            if(j==7){ j=0; $(".wdP").attr("class","wdP");$(".word1").html(68);array=[73,86,58,72,65,76,91];}
        }, 500);

        //门动画图层隐藏
        $('.hover_door').addClass("openTotal");
    }, 2500);

    //协议弹窗

    var button_checked = false;//判断是否是从“开始”点击的确定弹窗按钮
    var xieyi1='<p style="text-align:center;"align="center"><span style="font-size:0.32rem;">用户协议</span></p><p><span style="">菲洛嘉委托授权上海商路网络科技有限公司作为软件系统提供者对用户进行肌肤检测服务，用户可以通过线上测肤小程序“AI护肤私教”进行拍照检测皮肤。</span></p><p><span style="">在测试前，您须完成菲洛嘉会员注册，请细阅读本使用条款。您访问或使用“网站”，说明您已同意受本条款的约束</span>。</p><p><span style="">&nbsp;</span></p><p><span style="">1.</span><span style="">隐私权</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">请查阅我们的隐私权政策以便理解我们的隐私保护措施。</span></p><p><span style="">2.</span><span style="">供个人使用的产品和服务</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">我们通过本网站自身或通过指定的经销商提供给您的任何产品和服务及其样品仅供您个人享用。任何从我方购买或收到的产品、服务及其样品均不可出售或转售。</span></p><p><span style="">3.</span><span style="">信息的准确性</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">我们尽量做到在“网站”上对产品的描述准确无误；然而，我们无法保证产品说明、颜色或“网站”上的其他内容完全精确、完整、现时或毫无差错。</span></p><p><span style="">4.</span><span style="">知识产权</span></p><p><span style="">&nbsp;&nbsp;“</span><span style="">网站”的所有内容及其“视觉和感觉”，包括但不限于商标、标志、服务商标、文字、图表、标识、按钮图标、图像、声音片段、数据汇编和软件以及文献编汇（合称“内容”）均为菲洛嘉中国总代理、我们的关联公司、合作伙伴和许可方的财产，并受包括著作权法和商标法在内的法国、中国和国际法律的保护。</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">除下述第五条有限许可的规定或适用法律规定外，未经我们事先明确书面同意，“网站”的内容或任何其他部分均不得为任何目的被全部或部分使用、再版、复制、仿制、出售、转售、访问、修改或以其他方式利用。</span></p><p><span style="">5.</span><span style="">有限许可</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">您可以访问及使用本网站，但不可：</span></p><p><span style="">&nbsp;&nbsp;(1)</span><span style="">框定或使用成帧技术框住本网站或其任何部分；</span></p><p><span style="">&nbsp;&nbsp;(2)</span><span style="">再发表、再发布、销售、许可或下载本网站或任何内容，（除暂存或查看本网站所必需）；</span></p><p><span style="">&nbsp;&nbsp;(3)</span><span style="">除个人使用以外对网站或其内容作其他任何用途；</span></p><p><span style="">&nbsp;&nbsp;(4)</span><span style="">修改、反向工程或根据本网站或任何内容创作衍生作品；</span></p><p><span style="">&nbsp;&nbsp;(5)</span><span style="">为您个人或其他方收集帐户资料；</span></p><p><span style="">&nbsp;&nbsp;(6)</span><span style="">在任何内容上使用任何元标记(Mega tags)或任何其他“隐藏文字”；</span></p><p><span style="">&nbsp;&nbsp;(7)</span><span style="">使用软件机器人、搜索蜘蛛、爬行搜索技术或类似的数据收集和提取工具，或采取可能给我们的信息基础设施造成不合理的负担或重负的任何其他手段。您必须不加修改的保留本网站上的及其上附带或包含的所有权通知。</span></p><p><span style="">6.</span><span style="">您可以对“网站”主页进行超级链接，仅为您个人及非商业之用。与“网站”链接的网站</span></p><p><span style="">&nbsp;&nbsp;(1)</span><span style="">可链接到我们“网站”，但不得复制“网站”的内容；</span></p><p><span style="">&nbsp;&nbsp;(2)</span><span style="">不可暗示我们支持该网站或其服务或产品；</span></p><p><span style="">&nbsp;&nbsp;(3)</span><span style="">不可不实地陈述其与我们的关系；</span></p><p><span style="">&nbsp;&nbsp;(4)</span><span style="">不可包含在适用法律项下可能被理解为非法的、令人反感的、下流的、攻击性的或有争议的内容，且只可包含对所有年龄层均合适的内容；</span></p><p><span style="">&nbsp;&nbsp;(5)</span><span style="">不可以虚假、误导、诽谤或在其他方面具有攻击性或有伤风化的方式描述我们或我们的产品和服务，或将我们与不受欢迎的产品、服务或意见加以联系；</span></p><p><span style="">&nbsp;&nbsp;(6)</span><span style="">不可链接到“网站”主页外的任何其他页面。我们可要求您去除对“网站”的任何链接，一经收到上述要求，您应立即去除或断开这些链接。</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">您对任一“网站”任何未经授权的使用将立即终止本第六条所规定的有限许可。</span></p><p><span style="">7.</span><span style="">您的义务和责任</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">您在访问或使用任一“网站”时，应当遵守本使用条款和“网站”上张贴的访问使用特别警示或指示。您应当根据法律和惯例善意行事。您不应当对“网站”或出现在“网站”上的任何内容或服务进行任何修改或改动，而且不应以任何方式损害“网站”的完整性和正常运作。如果您由于疏忽或故意违反本条款中的任何规定，您应对菲洛嘉中国总代理、我们的关联公司、合作伙伴或许可方造成的损失和损害承担责任。</span></p><p><span style="">8.</span><span style="">您的帐户</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">若您是18岁以上人士，您可以在我们的“网站”注册。如果您未满18岁，请不要注册。如果您已满18岁且注册，您的账户会有一个电子邮件地址/用户名和密码。您应负责对自己的账户、用户名和密码保密，并限制他人使用您的电脑登陆您的账户。您应负责保证账户相关信息现时、完整、准确和真实，并为在您的帐户、用户名和/或密码项下发生的所有行为负责。您同意只提供现时、完整、准确和真实的信息。</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">我们保留无需事先通知，拒绝服务和/或终止帐户的权利。</span></p><p><span style="">9.</span><span style="">第三方链接</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">我们不对“网站”之外的页面或与“网站”相链接的其他网站的内容负责。您应仔细阅读所有您访问的“网站”之外的页面及其他网站的使用条款和隐私权政策。</span></p><p><span style="">10.</span><span style="">特别项目、功能和活动</span></p><p><span style="">&nbsp;&nbsp;(1)“</span><span style="">网站”可能会提供某些特别项目、功能和活动（比如竞赛、抽奖或其他活动），这些活动会适用除本条款之外的使用规则、条款和/或政策；</span></p><p><span style="">&nbsp;&nbsp;(2)</span><span style="">并由我们或第三方提供。若您选择参与这些活动，我们会通知您，您同意参与活动适用另外单独的使用规则、条款和/或政策。</span></p><p><span style="">11.</span><span style="">提交资料</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">我们一般谢绝未经请求的建议和想法。然而，您向我们提供的任何询问、反馈、建议、想法或其他信息（合称“提交资料”）将作为非私有、非保密的资料处理。在遵守我们隐私权政策的前提下，我们可以以任何形式、媒介或技术复印、使用、复制、修改、改编、公布、出售、转让、翻译、制造衍生作品、分发及展示任何提交资料，不论上述提交资料是目前为人所知或今后开发的，单独的或是其他产品的一部分，我们也可在我们的产品或服务上或结合产品或服务而应用提交资料。</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">每一个因特网用户都有义务保护因特网的安全。您保证上述提交资料并不构成或包含软件病毒、商业招揽、链式信函、群发邮件或任何形式的“垃圾信息”。您不可使用虚假的电子邮件地址，假冒任何个人或实体，或以别种方式就任何提交资料的来源误导我们。您同意就您违反本条及而导致的或因提交资料发生的任何损失向我们赔偿。</span></p><p><span style="">12.</span><span style="">使用者信息</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">当您向任一“网站”，尤其是菲洛嘉官方网站传输、上载、发布、电邮或通过其他方式使得“网站”获得数据、文本、软件、音乐、声音、照片、表格、图像、录像、消息或其他材料（“使用者信息”），您须对此等使用者信息全权负责。该使用者信息构成上述11条所述的提交资料。这意味着，资料的提交者，而并非我们，应对在任一“网站”提交的使用者信息全权负责。您同意不进行、协助或鼓励他人向“网站”传输、上载、发布、电邮或通过其他方式使“网站”拥有以下使用者信息：</span></p><p><span style="">&nbsp;&nbsp;(1)</span><span style="">违背中国宪法所确定的基本原则的；</span></p><p><span style="">&nbsp;&nbsp;(2)</span><span style="">危害国家安全，泄露国家秘密，颠覆国家政权，破坏国家统一的；</span></p><p><span style="">&nbsp;&nbsp;(3)</span><span style="">损害国家荣誉和利益的；</span></p><p><span style="">&nbsp;&nbsp;(4)</span><span style="">煽动民族仇恨、民族歧视、破坏民族团结的；</span></p><p><span style="">&nbsp;&nbsp;(5)</span><span style="">破坏国家宗教政策，宣扬邪教和封建迷信的；</span></p><p><span style="">&nbsp;&nbsp;(6)</span><span style="">散布谣言，扰乱社会秩序，破坏社会稳定的；</span></p><p><span style="">&nbsp;&nbsp;(7)</span><span style="">散布淫秽、色情、赌博、暴力、凶杀、恐怖或者教唆犯罪的；</span></p><p><span style="">&nbsp;&nbsp;(8)</span><span style="">侮辱或者诽谤他人，侵害他人合法权利的；</span></p><p><span style="">&nbsp;&nbsp;(9)</span><span style="">含有虚假、诈骗、有害、胁迫、侵害他人隐私、骚扰、侵害、中伤、粗俗、猥亵、或其它道德上令人反感的内容；</span></p><p><span style="">&nbsp;&nbsp;(10)</span><span style="">您无法定权利、协议性权力或代理权发布该信息；</span></p><p><span style="">&nbsp;&nbsp;(11)</span><span style="">您知道该信息是错误的、不准确或误导性的；</span></p><p><span style="">&nbsp;&nbsp;(12)</span><span style="">您发布该信息获得了第三方的报酬；</span></p><p><span style="">&nbsp;&nbsp;(13)</span><span style="">该信息侵犯了任何其他方的任何专利、商标、商业秘密、版权或其他所有权；</span></p><p><span style="">&nbsp;&nbsp;(14)</span><span style="">含有中国法律、法规、规章、条例以及任何具有法律效力之规范所限制或禁止的其它内容的。另外，您同意不传输、上载、发布、电邮或通过其他方式使得“网站”得到软件病毒、未经请求或授权的广告、商业招揽或促销性材料，包括链式信函、群发邮件或任何形式的“垃圾信息”。</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">您还同意不进行下列行为：</span></p><p><span style="">&nbsp;&nbsp;(1)</span><span style="">冒充任何个人或组织，或错误的陈述或通过其他方式表示您与任何个人或实体之间的关联关系；</span></p><p><span style="">&nbsp;&nbsp;(2)</span><span style="">骚扰或袭击他人，包括挑起他人的袭击、诱骗或通过其他方式陷害他人，包括通过任何方式骚扰未成年人；</span></p><p><span style="">&nbsp;&nbsp;(3)</span><span style="">伪造标题或通过其他方式假造标识符以隐藏任何使用者信息的来源；</span></p><p><span style="">&nbsp;&nbsp;(4)</span><span style="">故意或非故意地违反任何适用的当地国家或国际法律；</span></p><p><span style="">&nbsp;&nbsp;(5)</span><span style="">收集或储藏其他用户的个人身份数据。</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">我们并不支持或控制在“网站”传输或上载的使用者信息的内容，所以我们并不保证其精确性、完整性和质量。您应理解，对任一“网站”的使用者信息的接触，您都可能接触到您认为令人不快的、不当的、或有争议的信息。我们在任何情况下都不为任何使用者信息负责，包括但不限于，我们不负责使用者信息的任何错误和遗漏，或由您在使用过程中造成的使用者信息任何形式的遗漏或损坏。</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">您承认，我们完全拥有拒绝发布或删除任何使用者信息的权利（并非义务），并且我们保留修改、压缩、或删除任何使用者信息的权利。在不限制上述说明和本使用条款中其他条款原则的前提下，我们拥有删除违反本使用条款或在其他方面有争议的使用者信息，且对于任何违反本使用条款或对他人侵权的用户，我们保留无提前通知即拒绝对其服务的权利。</span></p><p><span style="">13.</span><span style="">版权争议</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">我们尊重他人的知识产权。如果您认为某一作品在本网站上被抄袭而构成著作权侵权。请通知我们有关侵权诉求</span></p><p><span style="">14.</span><span style="">声明和保证；责任限制</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">本网站按现状提供。在适用法律允许的范围内，我们并不就本网站作任何形式（无论明示或暗示）的声明或保证。</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">在适用法律允许的范围内，我们不为下述情况负责或承担责任（包括合同法、侵权法（包括疏忽）或其他责任）</span></p><p><span style="">&nbsp;&nbsp;(1)</span><span style="">业务中断；</span></p><p><span style="">&nbsp;&nbsp;(2)</span><span style="">对本网站的访问延迟或访问中断；</span></p><p><span style="">&nbsp;&nbsp;(3)</span><span style="">数据不传送、错误传送、讹误、破坏或被篡改；</span></p><p><span style="">&nbsp;&nbsp;(4)</span><span style="">由于处理本网站上的网站外链接或因网站外链接的出现而发生的任何类型的损失或损害；</span></p><p><span style="">&nbsp;&nbsp;(5)</span><span style="">您因使用本网站，包括超级链接出入第三方网站时，可能发生的计算机病毒、系统故障或失灵；</span></p><p><span style="">&nbsp;&nbsp;(6)</span><span style="">任何不准确或有疏漏的内容；</span></p><p><span style="">&nbsp;&nbsp;(7)</span><span style="">在我们合理控制范围以外的事件。而且，在法律允许的最大范围内，我们将不为与本网站有关的任何类型的间接或结果性损害（包括利润损失）负责，不论诉讼形式是基于合同、侵权（包括疏忽）或其他理论，即使我们接到可能发生该等损害的通知。</span></p><p><span style="">15.</span><span style="">补偿</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">您同意对因您使用“网站”或违反本使用条款导致任何第三方提出权利主张、起诉或要求而产生的任何损失、损害或费用，包括合理的律师费向我们作出保护和补偿，并使我们不受损失。您也同意对因您使用软件机器人、搜索蜘蛛、爬行搜索器或类似数据收集和提取工具，或您采取的给我们的信息基础设施造成不合理的负担或重负的任何其他手段而产生的任何损失、损害或费用，包括合理的律师费向我们作出补偿。</span></p><p><span style="">16.</span><span style="">争议</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">对于与“网站”有关的任何争议和本使用条款所包含的您的权利和义务及所有行为应受中华人民共和国法律管辖。与您访问“网站”有关的任何形式的争议应提交给中国国际经济贸易仲裁委员会（“贸仲会”）在北京进行仲裁，您接受该机构的管辖权和程序；但如果您以任何方式侵犯或可能侵犯我们（或我们的关联实体、合作伙伴或许可人）的知识产权或我们有基于衡平法的诉因，我们可在任何有适当管辖权的法院寻求禁令或其他适当的救济，您同意该法院的属人管辖权和属地管辖权。在本协议项下的仲裁应根据贸仲会届时有效的仲裁规则进行。仲裁裁决应具有约束力，并可在任何具有司法管辖权的法院作判决备案。在法律许可的最大范围内，本使用条款项下的任何仲裁不得与涉及受制于本使用条款的任何其他方的仲裁合并，无论是否以集体仲裁程序或其他方式提起。</span></p><p><span style="">17.</span><span style="">同意由网站公告或电邮、短信、印刷材料等形式接受通讯</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">您同意通过包括但不限于电子邮件、短信、印刷材料或本网站上的通告，接受本使用条款提及的任何协议、通知、讯息和其它通讯（合称&quot;通知&quot;）。您同意我们以电子方式提供给您的通知符合该等通知应当书面做出的法律要求。您必须发送电子邮邮件至filorga@fangzigroup.com并停止使用“网站”，来通知我们您不再同意以电子方式接受通知。在此情况下，所有根据本使用条款赋予您的权利，包括但不限于第六条所述有限许可，应当自动终止。遗憾的是，我们无法向不同意以电子方式接受通知的用户提供“网站”的服务。</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">请注意，本条同意接受通知的规定和一切您作出的接收销售通讯的选择不相关联。您对于是否接收销售通讯的选择由我们的隐私权政策.来规定。</span></p><p><span style="">18.</span><span style="">一般规定</span></p><p><span style="">&nbsp;&nbsp;</span><span style="">我们可在任何时间通过在“网站”上公布的方式更改上述使用条款。任何更改在“网站”公布和发出更改通知之时立即生效。您对“网站”的继续使用构成您对所有该等更改的同意。</span></p><p><span style="">19</span><span style="">．会员积分细则</span></p><p><span style="">&nbsp;&nbsp;(1)</span><span style="">单笔积分有效期为12个月，逾期自动清零，若未在积分有效期内兑换积分赠礼，则视同放弃。会员等级将随积分清零同时失效，降为普通会员身份。</span></p><p><span style="">&nbsp;&nbsp;(2)</span><span style="">会员身份不可重复登记，会员注册手机号对应唯一会员ID，菲洛嘉保留依据实际消费记录进一步核查积分的权利。</span></p><p><span style="">&nbsp;&nbsp;(3)</span><span style="">菲洛嘉产品外包装防伪码将作为获取商品积分的唯一途径，采取一物一码原则，如撕毁、丢失、破损将无法找回，积分不予补计。</span></p><p><span style="">&nbsp;&nbsp;(4)</span><span style="">菲洛嘉中小样产品及积分抽奖、换礼、试用所获得的正装产品均为非卖品，不再参与产品积分。</span></p><p><span style="">&nbsp;&nbsp;(5)</span><span style="">积分兑换成功后，系统会将相应积分自动扣除，不可取消或更改。</span></p><p><span style="">&nbsp;&nbsp;(6)</span><span style="">所有产品以实物为准，如遇礼品缺货，菲洛嘉有权以相近价值礼品替换。</span></p><p><span style="">&nbsp;&nbsp;(7)</span><span style="">消费金额与积分不得转让，积分和赠品均不可折换成现金。</span></p><p><span style="">&nbsp;&nbsp;(8)</span><span style="">会员以任何理由退换货时，菲洛嘉将以购买时实际取得的消费积分予以扣除。</span></p><p><span style="">&nbsp;&nbsp;(9)</span><span style="">会员可在菲洛嘉护肤微信公众号或菲洛嘉中国官网进行积分礼品兑换，暂不支持其他渠道店铺，礼品将在7-15个工作日内（遇节假日顺延）寄送到您指定的收货地址。菲洛嘉将不定期更换积分产品，如有变动，不作另行通知，以积分商城发布为准。</span></p><p><span style="">&nbsp;&nbsp;(10)</span><span style="">菲洛嘉有权根据业务情况调整积分规则并于该规则调整之日予以公布，调整后的规则一经发布，即发生效力，会员如有疑问，可联系客服进行了解和咨询。</span></p><p><span style="">&nbsp;&nbsp;(11)</span><span style="">薇黛（北京）商贸有限公司在使用法律法规允许范围内，保留对菲洛嘉会员权益及相关活动规则的最终解释权</span></p><p><span style="">20</span><span style="">．会员权益细则</span></p><p><span style="">&nbsp;&nbsp;(1)</span><span style="">会员等级：</span></p><p><span style="">&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="">普通会员（关注菲洛嘉官方微信公众号并绑定注册成功）享受消费1元=1倍积分</span></p><p><span style="">&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="">高级会员（在菲洛嘉官方渠道累计满2000积分）享受消费1元=1.2倍积分</span></p><p><span style="">&nbsp;&nbsp;&nbsp;&nbsp;VIP</span><span style="">会员（在菲洛嘉官方渠道累计满4000元积分）享受消费1元=1.5倍积分</span></p><p><span style="">&nbsp;&nbsp;(2)</span><span style="">成功绑定会员后，完善个人信息，将额外获得50积分奖励</span></p><p><span style="">&nbsp;&nbsp;(3)</span><span style="">邀请好友关注菲洛嘉微信公众号并完成注册，邀请双方都将获得50积分奖励</span></p><p><span style="">&nbsp;&nbsp;(4)</span><span style="">会员生日礼：会员在商场专柜、微信官方商城、天猫旗舰店、天猫海外旗舰店、京东旗舰店任意消费后，即可在生日月免费领取会员生日臻享礼盒</span></p><p><span style="">&nbsp;&nbsp;(5)</span><span style="">会员积分抽奖：会员每人每天可免费抽奖一次，再次抽奖须消耗20积分，每人每天最多可抽奖5次。</span></p><p><span style="">&nbsp;&nbsp;(6)</span><span style="">会员积分换礼：兑换的礼品将在7-15个工作日内（遇节假日顺延）寄送到您指定的收货地址。菲洛嘉将不定期更换积分产品，如有变动，不作另行通知，以积分商城发布为准。</span></p><p><span style="">21</span><span style="">．口碑细则</span></p><p><span style="">&nbsp;&nbsp;(1)</span><span style="">请发布真实、客观的美妆分享口碑，同样的内容、图片、回复请不要重复发布，菲洛嘉有权对所有口碑中心内容进行管理。</span></p><p><span style="">&nbsp;&nbsp;(2)</span><span style="">请不要发布抄袭的，或非原创且未经作者授权的内容，一经发现会被立即删除，由此产生的不良后果由发布者承担。</span></p><p><span style="">&nbsp;&nbsp;(3)</span><span style="">所有产品信息、口碑报告、收货短评、评论与回复等，未经授权，严禁转载或使用。</span></p><p><span style="">&nbsp;&nbsp;(4)</span><span style="">您所上传的图片、文字、照片等所有口碑信息，将视为您同意由菲洛嘉在中国地区的经销商为其经销的品牌使用您的个人信息向您提供更完善的服务和商品推介，并可能成为前述目的将您上传的口碑信息提供给关联企业及缔约方和合作伙伴。</span></p><p><span style="">上述条款菲洛嘉保留修改一切条款及细则的权利。若有争议，菲洛嘉保留最终解释权。</span></p>';
    var yinsi1='<p style="text-align: center;"align="center"><span style="font-size:0.32rem;">隐私政策</span></p><p><span style="">菲洛嘉高度重视隐私保护，下列原则规制我们与您的隐私有关的行为：</span></p><p>1.<span style="">我们珍视您在向我们提供您的个人信息时对于我们的信任。我们对于您的个人信息的使用将绝不会有负您的信任。</span></p><p>2.<span style="">您有权清楚了解我们如何使用您的个人信息。我们将始终在收集何种信息，如何处理该种信息，与哪方共享信息以及您有疑问时联系我们的联系人信息等方面保持透明。</span></p><p>3.<span style="">如您对于我们如何使用您的个人信息存在疑问，我们将配合您迅速解决您的疑问。</span></p><p>4.<span style="">我们将采取所有必要措施来确保您的信息不被滥用和不当披露。</span></p><p>5.<span style="">我们将遵守所有适用的有关数据保护和法律法规并配合数据保护主管机关的工作。如不存在有关数据保护的立法，我们将依据普遍接受的适用于数据保护的准则来规范我们的行为。</span></p><p><strong><span style="">菲洛嘉隐私保护政策</span></strong></p><p><span style="">菲洛嘉致力于保护您的隐私并且确保您的个人信息受到保护。本隐私保护政策解释了我们收集的信息类型、我们如何使用以及我们如何保护该等信息。</span></p><p><strong><span style="">本隐私权保护政策的适用范围？</span></strong></p><p><span style="">本隐私保护政策适用菲洛嘉所属公司所收集的与其所提供的服务有关的任何个人信息。上述个人信息既包括我们通过服务热线、消费者呼叫热线，直递市场活动、抽奖和竞赛等线下渠道和网站、第三方平台之上的品牌页面、以及菲洛嘉所属公司或其代表所运营的网站或第三方平台所访问或使用的程序等线上渠道</span>(<span style="">以上统称“菲洛嘉网站”</span>)<span style="">所收集的个人信息。所有有关使用菲洛嘉网站的条款和条件中均应当包括作为其组成部分的本隐私保护政策。如欲了解更多关于有责任保护您的个人信息的菲洛嘉所属公司，请参阅下述您的隐私权及如何联系我们。</span></p><p><span style="">本隐私保护政策不适用于：</span></p><p><span style="">我们没有控制权的第三方网站、平台和</span>/<span style="">或应用程序（以下简称为“第三方网站”）所收集的信息；</span></p><p><span style="">您通过菲洛嘉网站的链接所访问的第三方网站所收集的信息；</span></p><p><span style="">我们可能在第三方网站上主办或参与的广告通栏、抽奖以及其他广告或促销。</span></p><p><span style="">该等第三方网站可能有其自己的隐私保护政策以及使用条款与条件。我们鼓励您在使用该等第三方网站之前仔细阅读该等政策和条款</span></p><p><strong><span style="">您的许可</span></strong></p><p><span style="">未经您的许可菲洛嘉不会收集、使用或披露您的个人信息。多数情况下我们会征得您的事先许可。在少数情况下我们会依据您的行动或行为合理推断获得您的同意。使用菲洛嘉网站，您即同意相关菲洛嘉集团所属公司根据本隐私保护政策收集、使用和正当披露您的个人信息。</span></p><p><span style="">如我们需要使用您的个人信息用于本隐私保护政策适用范围以外的目的，我们将会事先征得您的额外许可。您没有义务给予此等额外许可，但如果您未有给予相关额外许可，您在某些活动中的参与可能会有所限制。如您给予额外的许可，此等额外许可的条款在与本隐私保护政策相冲突时将优先适用。</span></p><p><span style="">如果您不同意您的个人信息以上述方式被收集、使用和披露，请勿使用菲洛嘉网站或向菲洛嘉提供您的个人信息。</span></p><p><strong><span style="">未成年人</span></strong></p><p><span style="">菲洛嘉网站的大多数内容系为成人用户设计和计划。如果菲洛嘉网站预期供更加年轻的用户使用，如果我们认为有必要或根据所适用的数据保护法律法规的要求，我们将会在收集个人信息之前获得父母或监护人的同意（需要获得同意的年龄各国不尽相同）。如果您属于未成年人但您的年龄超过了您所在国家要求父母同意的年龄，则您应当与您的父母或监护人一起阅读本隐私权政策，确保您理解并接受这些条款。</span><span style="">如果我们发现未获得该等所必需的父母或监护人的同意而我们已经收集到某用户的信息，我们将会尽快删除该等信息。</span></p><p><span style="">菲洛嘉网站某些部分的访问和</span>/<span style="">或获得奖金、样品或其它报酬的资格，可能仅限于某一特定年龄以上的用户。</span><span style="">我们可能会使用您的个人信息进行年龄验证和核查以执行我们的年龄限制规定。</span></p><p><strong><span style="">我们收集何种信息？</span></strong></p><p><span style="">在本隐私保护政策中，您的“个人信息”是指能够使您被识别的信息或多条信息。该信息典型地包括诸如您的姓名、地址、用户名、个人图片、电子邮件地址以及电话号码等信息，但是也可以包括诸如</span>IP<span style="">地址、购物习惯、爱好以及关于您的生活方式或爱好（例如您的业余爱好和兴趣）的信息。</span></p><p><span style="">我们可以从以下不同来源收集您的个人信息：</span></p><p><span style="">您直接向我们提供的信息</span></p><p><span style="">当您向我们提供个人信息时，例如当您进行抽奖或比赛注册，报名获取信息、使用应用程序、向我们购买产品或服务、填写调查表或进行评论或咨询之时，我们会直接向您收集信息。</span></p><p><strong>&nbsp;<span style="">我们会直接向您收集的信息类型包括您的：</span></strong></p><p><span style="">姓名</span></p><p><span style="">地址</span></p><p><span style="">邮件地址</span></p><p><span style="">用户名</span></p><p><span style="">电话号码</span></p><p><span style="">信用卡或其他支付信息</span></p><p><span style="">年龄</span></p><p><span style="">生日</span></p><p><span style="">性别</span></p><p><span style="">用户生成的内容、帖子以及您向菲洛嘉网站提供的其它内容</span></p><p><span style="">您自愿向我们提供的任何其他个人信息</span></p><p><span style="">您使用菲洛嘉网站时我们自动收集的信息</span></p><p><span style="">当您使用菲洛嘉网站时，我们会在遵守本隐私保护政策和所适用的数据保护法律法规的前提下使用</span>Cookies<span style="">以及其他工具（例如，网站分析工具和像素标签）自动地收集您的有关信息。我们可能自动地收集的信息类型包括：</span></p><p><span style="">您使用的浏览器类型</span></p><p><span style="">您浏览的网页详情</span></p><p><span style="">您的</span>IP<span style="">地址</span></p><p><span style="">点击的超链接</span></p><p><span style="">使用第三方网站</span>(<span style="">例如您使用</span>Facebook<span style="">的“</span>Like<span style="">”功能或</span>Google+<span style="">的“</span>+1<span style="">”功能</span>)<span style="">时您选择共享的您的用户名、个人图片、性别、社交圈以及任</span><span style="">何其他信息</span></p><p><span style="">访问菲洛嘉网站之前您所访问的网站</span></p><p><span style="">多数互联网浏览器的初始设置是接受</span>cookies<span style="">。您可以选择设置拒绝接受</span>cookies<span style="">或收到</span>cookies<span style="">时系统报警。如您取消</span>cookies<span style="">功能，您在菲洛嘉网站的浏览体验可能受到影响。</span></p><p><span style="">我们可能自其它的来源收集您的个人信息，但前提是您已经同意您的信息被分享。此等信息可能包括商业可供来源（例如，公共数据库以及数据聚合器）的信息以及第三方处获得的信息。</span><span style="">我们可以自该等来源收集的个人信息类型包括您的：</span></p><p><span style="">姓名</span></p><p><span style="">街道地址</span></p><p><span style="">年龄</span></p><p><span style="">您的购物习惯</span></p><p><span style="">爱好和您的生活方式相关信息，例如您的业余爱好和兴趣</span></p><p><span style="">法律所允许的公开渠道可得的信息，例如，用户生成内容、博客以及贴子等</span></p><p><span style="">我们如何使用您的个人信息</span></p><p><span style="">我们可能将您的个人信息用于：</span></p><p><span style="">改进我们的产品和提升您在菲洛嘉网站的用户体验。</span></p><p><span style="">我们可能将您的个人信息用于：</span></p><p><span style="">评估菲洛嘉网站、产品以及服务的使用</span></p><p><span style="">分析我们的广告、竞赛以及促销的有效性</span></p><p><span style="">个性化您的网站体验，以及对网站活动的评估统计（匿名且总计数据），例如，您访问的时间、您是否之前访问过以及什么站点将您指引到网站</span></p><p><span style="">使菲洛嘉网站的使用更轻松并且更好地设计研发菲洛嘉网站和产品，以满足您的兴趣和需求</span></p><p><span style="">帮助加速您在菲洛嘉网站上的未来活动和经验。例如，网站识别您曾经提供了个人信息就不再第二次请求相同信息</span></p><p><span style="">收集您用于浏览菲洛嘉网站的设备的相关信息，例如，您的</span>IP<span style="">地址或互联网浏览器类型或您所使用的操作系统，并且将之与您的个人信息相联系，以便确保菲洛嘉为您提供最佳的网站体验</span></p><p><span style="">仅当我们已经获得您的同意后或您之前提出对于我们提供的产品或服务的请求，就您可能感兴趣的产品和服务与您进行联络，且此等联络在适用法律的规定的合理时间期限内与前述的请求</span></p><p><span style="">相关或存在关联。</span></p><p><strong><span style="">我们可能将您的个人信息用于：</span></strong></p><p><span style="">建议我们认为您可能感兴趣的产品或服务（包括相关第三方的产品或服务）</span></p><p><span style="">向您提供参加竞赛或促销的机会</span></p><p><span style="">您可随时选择不再接受我们的联络。并且我们向您发送的任何直销沟通将会向您提供选择退出的所需信息和方式。</span></p><p><span style="">向您提供您向我们所要求的产品或服务</span></p><p><span style="">我们可能将您的个人信息用于：</span></p><p><span style="">用于您已经报名参与的竞赛或促销</span></p><p><span style="">向您发送您所要求的信息、产品或样品</span></p><p><span style="">回复您的询问或评论</span></p><p><span style="">当我们为了一个特定目的收集个人信息时，除非基于合法的商业或法定理由，我们对于该等信息的保存期限仅限于该目的所必需的期限。</span></p><p><span style="">为了确保信息免于因为意外事件或恶意损毁而受损，当我们删除从各项服务过程中收集的信息时我们也许不会立即从我们的服务器中删除剩余副本或立即从备用系统中移除备份信息。</span></p><p><span style="">移动信息服务</span></p><p><span style="">您能通过我们提供的服务在您的无线或移动设备上接收菲洛嘉发出的文字或其它类型的信息</span>(<span style="">诸如短消息</span>SMS<span style="">服务</span>,<span style="">增强型短消息</span>EMS<span style="">服务或多媒体短消息</span>MMS<span style="">服务</span>)<span style="">服务</span>(<span style="">“移动信息服务”</span>)<span style="">。如您订阅任意一项我们提供的移动信息服务，您须同意接收菲洛嘉向您为了此目的所提供的地址或移动号码发送的信息</span>(<span style="">直至您按照下述您的隐私权及如何联系我们条款选择不再接受此类信息</span>)<span style="">。</span></p><p><span style="">您须了解您的无线服务运行商可能对上述信息按照其费率标准收费，您可随时按照下述您的隐私权及如何联系我们条款改变您的决定。如有费用在您的无线账户账单中收取，您应当同意我们可向您收取并据此向您的无线运营商提供您所适用的支付信息。您须声明您是您所用来申请收取移动信息服务的无线设备的所有人或授权使用人且有权批准所产生的费用。为了符合特定的年龄限制或与移动信息服务相关的其他条款和条件的要求，您可能被要求注册登记包括您的姓名、短消息、无线地址或手机号码在内的个人信息。我们也可能会收集您在使用移动信息服务过程中的您所使用的信息的日期，时间和信息内容。我们将按照本隐私保护政策的规定使用。</span></p><p>&nbsp;</p><p><span style="">所收集的与提供移动信息服务相关的信息。请注意，您的无线运营商或其他服务供应商也可能收集有关您无线设备使用的数据，他们的行为受到他们各自政策的规范。您承认并同意移动信息服务系使用以无线信号</span>(<span style="">或其他方式</span>)<span style="">通过复杂网络传送沟通信息的无线网络系统来提供。基于上述原因，我们无法保证您对移动信息服务的使用是完全保密和安全的，我们对于您可能遇到的隐私侵犯或不安全不承担责任。你有责任根据自身情况和预期的对移动信息服务的使用采取相应的防范措施和安全措施。在法律许可的范围内，我们可能会为了鉴别和解决技术故障和</span>/<span style="">或服务相关的投诉的目的而向您的无线运营商了解您的无线服务的份额内容或移动电话账户信息。</span></p><p>&nbsp;</p><p><span style="">作为一般原则，我们不与菲洛嘉所属公司之外的任何人共享您的个人信息。</span><span style="">但是，我们可能会与某些信任的第三方分享您的个人信息。</span></p><p>&nbsp;</p><p><span style="">我们可能与以下各方共享您的个人信息：</span></p><p><span style="">帮助我们提供广告宣传和促销并且分析其有效性的广告、市场和促销代理商</span></p><p><span style="">要向您交付产品或服务的第三方，例如，交付您所订购产品的运输和快递服务</span></p><p><span style="">执法或政府部门，如果他们已经遵守适当法律程序要求我们披露信息</span></p><p><span style="">希望向您发送关于他们的产品与服务的信息的第三方，前提是我们已经获得您的同意</span></p><p><span style="">菲洛嘉的第三方服务提供商，例如，向菲洛嘉提供数据处理的服务的提供商</span></p><p><span style="">网络分析工具提供商，例如，</span>Google<span style="">或</span>Unica</p><p>&nbsp;</p><p><span style="">如我们依据合法理由相信信息的披露是必要的，我们可能向菲洛嘉所属公司以外的公司、组织或个人共享您的个人信息。</span></p><p><span style="">我们可能基于下列理由共享您的个人信息：</span></p><p><span style="">执行与使用菲洛嘉网站相关的条款</span></p><p><span style="">就违反适用法律而进行调查</span></p><p><span style="">对于欺诈和任何技术或安全攻击进行检测、预防和防护</span></p><p><span style="">守适用法律法规，配合司法调查和执行行政机关依法要求</span></p><p><span style="">如果我们的确与第三方分享您的个人信息，我们将会尽最大努力确保该第三方对您的信息保密，防止其被滥用且仅能以与本隐私保护政策以及所适用的数据保护法律法规所允许的方式使用您的个人信息。</span></p><p><span style="">除非我们向一个法律实体出售全部或部分我们的业务时一并提供相关信息</span>(<span style="">例如，与出售某一品牌相关</span>)<span style="">，或与某一业务的业务收购、合并、所有权变更、重组或清算相关，菲洛嘉不对外出售个人信息。</span></p><p><strong><span style="">您的个人信息的转移</span></strong></p><p><span style="">我们可能将您的个人信息转移存储至您所居住国家以外的服务器或转移至位于其他国家的关联企业或可行的第三方以便代表我们处理您的个人信息。对于菲洛嘉网站的使用或向菲洛嘉提供您的个人信息即表明您同意我们按照本隐私保护政策和所适用的数据保护的法律法规。</span></p>';
    function yinsi(){
        $(".policy_tan_desc").html(yinsi1);
        $(".policy_tan").addClass("show");
    }
    function xieyi(){
        $(".policy_tan_desc").html(xieyi1);
        $(".policy_tan").addClass("show");
    }
    function iKnow(){
        $(".policy_tan").removeClass("show");
        $(".policy_check").addClass("checked");
        if(button_checked){
            window.location.href="userInfo.html";
        }
    }

    //点击开始按钮
    
    function toNext(){
        if($(".policy_check").hasClass("checked")){
            window.location.href="userInfo.html";
        }else{
            $(".policy_tan_desc").html(yinsi1);
            $(".policy_tan").addClass("show");
            button_checked = true;
        }
    }
    //点击同意按钮
    function agree(){
        $(".policy_check").toggleClass("checked");
    }


    //测试总数
    // localStorage.clear();
    var totalNum = window.localStorage.getItem("totalNum");

    //if(window.localStorage.getItem("totalNum")  == null){
        // console.log("第一次赋值总测试次数");
       $.ajax({
            type: "POST",
            url: "https://tools.skinrun.cn/filorga/total_test",
            dataType: "json",
            contentType: "application/x-www-form-urlencoded",
            headers: {},
            data: {},
            success: function(a) {
                a = JSON.parse(a); console.log(a);
                totalNum = parseInt(a.data.total);
                window.localStorage.setItem("totalNum",totalNum);
                $(".test_num").find("span").html(totalNum);
            },
            error: function(a) {
                console.log(JSON.stringify(a));
            }
        })
    //}


    //判断手机客户端
    $(function () {
        var u = navigator.userAgent, app = navigator.appVersion;
        var isAndroid = u.indexOf('Android') > -1 || u.indexOf('Linux') > -1;
        var isIOS = !!u.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/); //ios终端
        if (isIOS) {
            $(".beginBtn").css("margin","0 auto 0.8rem");
        }
    });
    //禁止ios 双指缩放
    window.onload = function () {

        // console.log("获取当前测试次数");
        var add_num = Math.floor(Math.random()*10);
		console.log(add_num);
        totalNum = parseInt(totalNum) + add_num;
        window.localStorage.setItem("totalNum",totalNum);
        $(".test_num").find("span").html(totalNum);


        document.addEventListener('touchstart',function (event) {  
            if(event.touches.length>1){  
                event.preventDefault();  //阻止元素的默认行为
            }  
        })
        var lastTouchEnd=0;  
        document.addEventListener('touchend',function (event) {  
            var now=(new Date()).getTime();  
            if(now-lastTouchEnd<=300){
                event.preventDefault();
            }  
            lastTouchEnd=now;  //当前为最后一次触摸
        },false)
    }
    document.addEventListener('gesturestart', function(event) {
        event.preventDefault();
    });
