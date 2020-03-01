__author__ = "Jerome Chang"
from django.utils.safestring import mark_safe


class Page(object):
    def __init__(self, base_url, current_page, page_count):
        self.base_url = base_url    # url前缀
        self.current_page = int(current_page)   # 当前页
        self.page_count = page_count  # 总页数

    def page_str(self):
        page_list = []
        if self.page_count <= 7:
            start_index = 1
            end_index = self.page_count
        else:
            if self.current_page > 3:
                start_index = self.current_page -3
                if self.current_page + 3 < self.page_count :
                    end_index = self.current_page + 3
                else:
                    end_index = self.page_count
            else:
                start_index = 1
                end_index = 7
        # 首页
        first_page = '<li><a class="page-link" href="%s1">首页</a></li>' % self.base_url
        page_list.append(first_page)
        # 上一页
        if self.current_page == 1:
            prev = 1
        else:
            prev = self.current_page - 1
        prev_page = '<li class="hidden-xs"><a class="page-link" href="%s%s">上一页</a></li>' % (self.base_url, prev)
        prev_page2 = '<li class="visible-xs" style="width:13%%"><a class="page-link" href="%s%s"><</a></li>' % (self.base_url, prev)
        page_list.append(prev_page)
        page_list.append(prev_page2)
        # 页码
        page_num = '<li class="visible-xs page-num" style="width:34%%"><span class="num">%s/%s</span></li>' % (self.current_page, self.page_count)
        page_input = '''
            <li class="page-input hidden" style="width:22%%"><input name="page-id" id="page-id" value=%s
            style="width:100%%;display: inline-block;padding: 5px 15px;border-radius: 4px;background-color: #fff;border: 1px solid #eee;"/></li>
            '''%self.current_page
        page_go = '<li class="page-go-li hidden active" style="width:12%"><a class="page-link page-go" href="javascript:">GO</a></li>'
        page_list.append(page_num)
        page_list.append(page_input)
        page_list.append(page_go)
        # 页面
        for page in range(start_index, end_index+1):
            if page == self.current_page:
                temp = '<li class="hidden-xs active"><a class="page-link" href="%s%s">%s</a></li>' % (self.base_url, page,page)
            else:
                temp = '<li class="hidden-xs"><a class="page-link" href="%s%s">%s</a></li>' % (self.base_url, page,page)
            page_list.append(temp)
        # 下一页
        if self.current_page == self.page_count:
            nex = self.page_count
        else:
            nex = self.current_page + 1
        next_page2 = '<li class="visible-xs" style="width:13%%"><a class="page-link" href="%s%s">></a></li>' % (self.base_url, nex)
        next_page = '<li class="hidden-xs"><a class="page-link" href="%s%s">下一页</a></li>' % (self.base_url, nex)
        page_list.append(next_page2)
        page_list.append(next_page)
        # 尾页
        last_page = '<li><a class="page-link" href="%s%s">尾页</a></li>' % (self.base_url,self.page_count)
        page_list.append(last_page)
        # JS
        page_js = '''
        <script>
            $(".page-num").click(function () {
                $(".page-num").removeClass("visible-xs").addClass("hidden");
                $(".page-input").removeClass("hidden");
                $(".page-go-li").removeClass("hidden");
                $("#page-id").removeClass("hidden").focus();
            });
            function func1(){
                $(".page-num").addClass("visible-xs");
                $(".page-input").addClass("hidden");
                $(".page-go-li").addClass("hidden");
            };
            $("#page-id").blur(function(){
                setTimeout('func1()',2000);
            });
            $(".page-go").click(function () {
                var page_id = $("#page-id").val();
                location.href = "%s" + page_id;
            });
        </script>
        ''' % (self.base_url)
        page_list.append(page_js)
        page_str = mark_safe(''.join(page_list))
        return page_str

    def video_page(self,data_list,per_page):
        start_index = (self.current_page-1)*per_page
        if self.current_page < self.page_count: # 非最后一页
            end_index = self.current_page*per_page
        elif self.current_page == self.page_count:  # 最后一页
            end_index = len(data_list)
        else:  # 页码错误
            return -1
        video_list = data_list[start_index:end_index]
        return video_list