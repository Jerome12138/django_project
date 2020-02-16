from django import template
import datetime
register = template.Library()

@register.simple_tag
def inc_one_day(date):
    new_date = datetime.datetime.strftime(datetime.datetime.strptime(date, "%Y-%m-%d")+ datetime.timedelta(1),"%Y-%m-%d")
    if new_date == datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d"):
        new_date = ""
    return new_date

@register.simple_tag
def dec_one_day(date):
    new_date = datetime.datetime.strftime(datetime.datetime.strptime(date, "%Y-%m-%d")+ datetime.timedelta(-1),"%Y-%m-%d")
    return new_date