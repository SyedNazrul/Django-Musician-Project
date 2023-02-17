from django import template

register = template.Library( ) 
def my_filter(value,args):
    return value + " " + args

register.filter('custom_filter', my_filter)