__author__ = "Jerome Chang"
from django.utils.safestring import mark_safe


class Page(object):
    def __init__(self, current_page, data_count, per_page_count=1, pager_num=5):
        self.current_page = int(current_page)
        self.data_count = data_count
        self.per_page_count = per_page_count
        self.pager_num = pager_num

    def page_str(self, base_url):
        page_list = []
        if self.data_count <= self.pager_num:
            start_index = 1
            end_index = self.data_count
        else:
            if self.current_page <= (self.pager_num - 1) / 2:
                start_index = 1
                end_index = self.pager_num
            else:
                if self.current_page > self.data_count - (self.pager_num - 1) / 2:
                    start_index = self.data_count - self.pager_num + 1
                    end_index = self.data_count
                else:
                    start_index = int(self.current_page - (self.pager_num - 1) / 2)
                    end_index = int(self.current_page + (self.pager_num - 1) / 2)
        # 前缀
        page_list.append(
            '<div style="float: right;"><nav aria-label="Page navigation example"><ul class="pagination">')
        # 第一页
        prev_page = 1
        # if self.current_page == 1:
        #     prev_page = 1
        # else:
        #     prev_page = self.current_page - 1
        prev = '<li class="page-item"><a class="page-link" href="%s?p=%s" aria-label="Previous"><span aria-hidden="true">&laquo;</span><span class="sr-only">Previous</span></a></li>' % (
            base_url, prev_page)
        page_list.append(prev)
        # 页面
        for page in range(start_index, end_index + 1):
            temp = '<li class="page-item"><a class="page-link" href="%s?p=%s" id="page-%s">%s</a></li>' % (base_url, page, page, page)
            page_list.append(temp)
        # 最后一页
        nex_page = self.data_count
        # if self.current_page == self.data_count:
        #     nex_page = self.data_count
        # else:
        #     nex_page = self.current_page + 1
        nex = '<li class="page-item"><a class="page-link" href="%s?p=%s" aria-label="Next"><span aria-hidden="true">&raquo;</span><span class="sr-only">Next</span></a></li>' % (
            base_url, nex_page)
        page_list.append(nex)
        # 后缀
        page_list.append('</ul></nav></div>')

        page_str = mark_safe(''.join(page_list))
        return page_str
