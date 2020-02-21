from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from . import models
from django.forms import ModelForm
from django.forms import Form
from django import forms
from django.forms import widgets as F_widgets
from django.forms import fields as F_fields
from django.views import View
from django.utils.decorators import method_decorator
import json, pickle


# 登录验证
def auth(func):
    def inner(request, *args, **kwargs):
        username = request.session.get('username', None)
        if not username:
            return redirect('/blog/sign_in/')
        user_obj = models.UserInfo.objects.filter(username=username).first()
        return func(request, user_obj, *args, **kwargs)

    return inner


# article modelform
class ArticleModelForm(ModelForm):
    class Meta:
        model = models.Article
        fields = ['user', 'title', 'content', 'category', 'tags']
        widgets = {
            'category': F_widgets.RadioSelect(),
            'tags': F_widgets.CheckboxSelectMultiple()
        }
        # choices = models.Category.objects.all().values_list('id', 'name')
        # field_classes = {'category': F_fields.CharField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs.update({'class': 'invisible'})


class CategoryModelForm(ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'


class TagModelForm(ModelForm):
    class Meta:
        model = models.Tag
        fields = '__all__'


class CommentForm(Form):
    content = F_fields.CharField(
        widget=F_widgets.Textarea(attrs={'id': 'id_comment_content'})
    )


# forms.ModelChoiceField(queryset=models.Category.objects.all())
# 信息管理
@method_decorator(auth, name='dispatch')
class Info(View):
    def get(self, request, user_obj):
        return render(request, 'backend_info.html', {'user_obj': user_obj})

    def post(self, request):
        pass


# 文章管理
@method_decorator(auth, name='dispatch')
class Articles(View):
    def get(self, request, user_obj):
        article_objs = models.Article.objects.filter(user=user_obj).all()
        return render(request, 'backend_articles.html', {'user_obj': user_obj, 'article_objs': article_objs})

    def post(self, request, user_obj):
        ret = {'status': True, 'error': None, 'data': None}
        try:
            article_id = request.POST.get('article_id')
            article_obj = models.Article.objects.filter(id=article_id).first()
            if not article_obj:
                ret['status'] = False
                ret['error'] = '当前文章不存在或已删除'
            else:
                article_obj.delete()
                ret['data'] = '删除成功'
        except Exception as e:
            print(e)
            ret['status'] = False
            ret['error'] = '未知错误'
        finally:
            return HttpResponse(json.dumps(ret))


# 标签管理
@method_decorator(auth, name='dispatch')
class Tag(View):
    def get(self, request, user_obj):
        tag_modelform = TagModelForm(initial={'user': user_obj})
        return render(request, 'backend_tag.html', {'user_obj': user_obj, 'tag_modelform': tag_modelform})

    def post(self, request, user_obj):
        tag_modelform = TagModelForm(request.POST)
        if tag_modelform.is_valid():
            tag_modelform.save()
            print('成功创建标签', tag_modelform.cleaned_data)
            return redirect('/blog/backend/tag/')
        else:
            print(tag_modelform.errors.as_json())
            return render(request, 'backend_tag.html', {
                'user_obj': user_obj,
                'tag_mdoelform': tag_modelform
            })


# 分类管理
@method_decorator(auth, name='dispatch')
class Category(View):
    def get(self, request, user_obj):
        categories = user_obj.category_set.all()
        category_modelform = CategoryModelForm(initial={'user': user_obj})
        return render(request, 'backend_category.html',
                      {'user_obj': user_obj, 'categories': categories, 'category_modelform': category_modelform})

    def post(self, request, user_obj):
        category_modelform = CategoryModelForm(request.POST)
        if category_modelform.is_valid():
            category_modelform.save()
            print('成功创建分类')
            return redirect('/blog/backend/category/')
        else:
            print(category_modelform.errors.as_json())
            return render(request, 'backend_category.html',
                          {'user_obj': user_obj, 'category_modelform': category_modelform})


# 评论管理
@method_decorator(auth, name='dispatch')
class Comment(View):
    def post(self, request, user_obj):
        ret = {'status': True, 'error': None, 'data': None}
        try:
            comment_id = request.POST.get('comment_id')
            # print(comment_id)
            comment_obj = models.Comment.objects.filter(id=comment_id).first()
            if not comment_obj:
                ret['status'] = False
                ret['error'] = '当前评论不存在或已删除'
            else:
                comment_obj.delete()
                ret['data'] = '删除成功'
        except Exception as e:
            print(e)
            ret['status'] = False
            ret['error'] = '未知错误'
        finally:
            return HttpResponse(json.dumps(ret))


# 添加或编辑文章
@method_decorator(auth, name='dispatch')
class EditArticle(View):
    def get(self, request, user_obj, article_id=0):
        try:
            if article_id == 0:
                article_modelform = ArticleModelForm(label_suffix='', initial={'user': user_obj})
                html_header = '添加文章'
                url = '/blog/backend/add_article/'
            else:
                article_obj = models.Article.objects.filter(id=article_id).first()
                assert article_obj
                article_modelform = ArticleModelForm(label_suffix='', instance=article_obj)
                html_header = '编辑文章'
                url = '/blog/backend/edit_article/%s/' % article_id

            return render(request, 'backend_edit_article.html', {
                'user_obj': user_obj,
                'article_modelform': article_modelform,
                'html_header': html_header,
                'url': url,
            })
        except Exception as e:
            print(e)
            return HttpResponse(e)

    def post(self, request, user_obj, article_id=0):
        if article_id == 0:
            article_modelform = ArticleModelForm(request.POST)
            html_header = '添加文章'
            url = '/blog/backend/add_article/'
        else:
            article_obj = models.Article.objects.filter(id=article_id).first()
            assert article_obj
            article_modelform = ArticleModelForm(request.POST, instance=article_obj)
            html_header = '编辑文章'
            url = '/blog/backend/edit_article/%s/' % article_id
        if article_modelform.is_valid():
            tag_objs = article_modelform.cleaned_data.get('tags')
            article_modelform_obj = article_modelform.save(commit=False)
            article_modelform_obj.save()  # 先保存单表信息
            # 再保存多对多信息
            models.Article2Tag.objects.filter(article=article_modelform_obj).delete()
            for tag_obj in tag_objs:
                models.Article2Tag.objects.create(article=article_modelform_obj, tag=tag_obj)
            print('article:save')
            return redirect('/blog/backend/articles/')
        else:
            print('article:false')
            print(article_modelform.errors.as_json())
            return render(request, 'backend_edit_article.html', {
                'user_obj': user_obj,
                'article_modelform': article_modelform,
                'article_id': article_id,
                'html_header': html_header,
                'url': url,
            })


# 添加或编辑评论
@method_decorator(auth, name='dispatch')
class AddComment(View):
    def get(self, request, user_obj, article_id):
        ret = {'status': True, 'error': None, 'data': None}
        try:
            comment_id = request.GET.get('comment_id')
            comment_obj = models.Comment.objects.filter(id=comment_id).first()
            if comment_obj:  # 修改回复
                ret['data'] = {'content': comment_obj.content}
                ret['data'].update({'id': comment_id})
            else:  # 楼层不存在
                ret['status'] = False
                ret['error'] = '找不到该回复'
        except Exception as e:
            print(e)
            ret['status'] = False
            ret['error'] = '未知错误'
        finally:
            return HttpResponse(json.dumps(ret))

    def post(self, request, user_obj, article_id):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # print(comment_form.cleaned_data)
            content = comment_form.cleaned_data.get('content')
            comment_id = request.POST.get('comment_id')
            article_obj = models.Article.objects.filter(id=article_id).first()
            # print(comment_id)
            if comment_id:  # 修改评论
                models.Comment.objects.filter(id=comment_id).update(content=content)
            else:  # 添加评论
                reply_id = request.POST.get('reply_id')
                if reply_id:  # 有回复楼层
                    reply_obj = models.Comment.objects.filter(id=reply_id).first()
                    if not reply_obj:
                        print('评论的对象不存在')
                        return redirect('/blog/%s/articles/%s.html' % (
                            article_obj.user.username, article_id))
                else:       # 无回复楼层
                    reply_obj = None
                new_layer = article_obj.comment_count + 1
                models.Comment.objects.create(
                    article=article_obj,
                    user=user_obj,
                    content=content,
                    layer_id=new_layer,
                    reply=reply_obj
                )
                # 更新文章的评论数
                comment_count = article_obj.comment_count + 1
                article_obj.comment_count = comment_count
                article_obj.save()
            return redirect('/blog/%s/articles/%s.html' % (
                article_obj.user.username, article_id))
        else:
            print('false')
            print(comment_form.cleaned_data)
            print(comment_form.errors.as_json())
