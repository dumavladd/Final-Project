from django.contrib.auth.decorators import login_required

from membership.models import Membership, UserMembership


def get_all_memberships(request):
    return {'memberships': Membership.objects.all()}


def get_membership(request):
    if request.user.is_authenticated:
        try:
            memb = UserMembership.objects.get(user=request.user.id)

            return {'type': memb.membership.type,
                    'color': memb.membership.color,
                    'start_date': memb.start_date,
                    'end_date': memb.end_date
                    }

        except UserMembership.DoesNotExist:
            return {}
    else:
        return {}
