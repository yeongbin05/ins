from django import template
import re

register = template.Library()

@register.filter
def word_link(value):
    content = value.content   
    hashtags = value.hashtags.all() # value객체의 hashtag전체를 가져오는 Qset
    for hashtag in hashtags:
        # hashtag의 문자열을 링크문자열로 replace
        link = f'<a href="/posts/{hashtag.pk}/hashtag">#{hashtag.content}</a>'
        content = re.sub(r'\#'+hashtag.content+r'\b', link, content)
    return content           