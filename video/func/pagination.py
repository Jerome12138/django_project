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
        prev_page = '<li><a class="page-link" href="%s%s">上一页</a></li>' % (self.base_url, prev)
        page_list.append(prev_page)
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
        next_page = '<li><a class="page-link" href="%s%s">下一页</a></li>' % (self.base_url, nex)
        page_list.append(next_page)
        # 尾页
        last_page = '<li><a class="page-link" href="%s%s">尾页</a></li>' % (self.base_url,self.page_count)
        page_list.append(last_page)
        page_str = mark_safe(''.join(page_list))
        return page_str
