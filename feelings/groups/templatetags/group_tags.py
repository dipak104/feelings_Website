from django import template
from django.template import Library

from ..models import FamilyInvite, CompanyInvite


register = Library()


@register.inclusion_tag('groups/_badge.html', takes_context=True)

def invites_badge(context, invite_type):
    if context['user'].is_authenticated:
        if invite_type == 'family':
            return {'invite_count': context['user'].familyinvite_received.filter(
            status=0).count()
                    }

        else:
            return {'invite_count': context['user'].companyinvite_received.filter(
                status=0).count()
                    }
