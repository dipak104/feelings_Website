from django import template
from django.template import Library
from django.utils import timezone
import datetime
import json

from ..forms import ThoughtForm


register = Library()

@register.inclusion_tag('thoughts/_form.html')

def thought_form():
    form = ThoughtForm()
    return {'form': form}



@register.simple_tag(takes_context=True)
def chart_data(context):
    user = context['user']
    ten_days_ago = timezone.now() - datetime.timedelta(days=10)
    thoughts = user.thoughts.filter(recorded_at__gt=ten_days_ago).order_by('recorded_at')
    return json.dumps({
        'labels': [thought.recorded_at.strftime('%Y-%m-%d') for thought in thoughts],
        'series': [[thought.condition for thought in thoughts]]
    })