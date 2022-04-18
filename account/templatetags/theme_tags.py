from django import template
from django.templatetags.static import static

register = template.Library()


@register.simple_tag(takes_context=True)
def theme(context, path):
    request = context.get("request")

    full_path = 'css/' + request.user.profile.theme + "/" + path

    url = static(full_path)

    return url
