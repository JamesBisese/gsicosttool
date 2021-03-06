from django.conf import settings
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
# from django.utils.crypto import get_random_string
from django.contrib.auth.models import Permission

class Command(BaseCommand):
    help = 'Create demonstration application users'

    def handle(self, *args, **kwargs):

        CustomUser = get_user_model()

        user_list = {
            'admin': {'email': 'admin@tetratech.com', 'password': 'cost2018', 'is_superuser': True, 'is_staff': True},
            'manager': {'email': 'manager@tetratech.com', 'password': 'cost2018', 'is_staff': True},
            'user1': {'email': 'user1@tetratech.com', 'password': 'user1018'},
            'user2': {'email': 'user2@tetratech.com', 'password': 'user2018'},
            'user3': {'email': 'user3@tetratech.com', 'password': 'user3018'},
        }

        is_staff_permissions = [
            'Can add scenario',
            'Can change scenario',
            'Can delete scenario',
            'Can add project',
            'Can change project',
            'Can delete project',
            # 'Can add person',
            # 'Can change person',
            # 'Can delete person',
        ]

        is_user_permissions = [
            'Can add scenario',
            'Can change scenario',
            'Can delete scenario',
            'Can add project',
            'Can change project',
            'Can delete project',
        ]

        for user in user_list:
            user_atts = user_list[user]

            if not CustomUser.objects.filter(email=user_atts['email']).exists():
                u = CustomUser.objects.create_user(
                                                    email=user_atts['email'],
                                                    password=user_atts['password'],
                                                    # agency='Tetra Tech',
                                                    name=user_atts['email'][0:user_atts['email'].index('@')],
                                                    is_staff=user_atts['is_staff'] if 'is_staff' in user_atts else False,
                                                    is_superuser=user_atts['is_superuser'] if 'is_superuser' in user_atts else False,
                                                   )

                if 'is_staff' in user_atts and user_atts['is_staff'] is True:
                    for perm in is_staff_permissions:
                        permission = Permission.objects.get(name=perm)
                        u.user_permissions.add(permission)
                elif not ('is_staff' in user_atts or 'is_superuser' in user_atts):
                    for perm in is_user_permissions:
                        permission = Permission.objects.get(name=perm)
                        u.user_permissions.add(permission)

                print('User "{}" created'.format(user_atts['email']))
            else:
                print('User "{}" exists already, not created'.format(user_atts['email']))