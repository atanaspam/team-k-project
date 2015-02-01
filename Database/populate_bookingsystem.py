import os

def populate():

    add_auth_group(id=1
        name="Manager")

     add_auth_group(id=2
        name="Parent")

     add_auth_group(id=3
        name="Coach")

    add_auth_user(id=1, password="pbkdf2_sha256$10000$I08MVZGZXcbK$SH99yKVcEyUQtq8kpqN+Qzy75S9t6b6RiLhYOQQ8pVI=", last_login="2015-01-25 01:11:26.424717", is_superuser=1, username="atanaspam", first_name="", last_name="", email="sfors123@gmail.com", is_staff=1, is_active=1, date_joined="2015-01-24 22:32:36.a")

   add_auth_user(id=2, password="pbkdf2_sha256$12000$Vs1tQHke2l8r$PvLEyP49BA+JTNYhKGQakYjwDFwt4/HFWlsDvrpdJdI=", last_login="2015-01-27 16:43:37.233680", is_superuser=1, username="dimitris", first_name="Dimitris", last_name="Kiker", email="", is_staff=1, is_active=1, date_joined="2015-01-25 01:14:31")

    add_auth_user(id=3, password="pbkdf2_sha256$12000$LEd3NVboCvJe$anYYTZKgKvQsPwx5OdbRBpHH00ygmp4EySU4l8s9+/g=", last_login="2015-01-31 13:53:02.959000", is_superuser=1, username="zoe", first_name="Zoe", last_name="Gerolemou", email="", is_staff=1, is_active=1, date_joined="2015-01-25 01:15:25")

    add_auth_user(id=4, password="pbkdf2_sha256$12000$4qxRcVaxlgb3$9mqnXEN5RI46gXPqsbwydkOi0lIM2WHKV5h/eiESnXk=", last_login="2015-01-29 23:26:40.562000", is_superuser=1, username="pedro", first_name="Pedro", last_name="Quintas", email="", is_staff=1, is_active=1, date_joined="2015-01-25 01:16:04")

    add_auth_user(id=5, password="pbkdf2_sha256$12000$uTnYqdApT7Jn$Pu+u5GYp7cdxBia3v6yzc09NN4wKu9kx5NImF4Yt7j4=", last_login="2015-01-29 23:27:18.049000", is_superuser=1, username="karl", first_name="Karl", last_name="Drouven", email="", is_staff=1, is_active=1, date_joined="2015-01-25 01:16:56")

    add_auth_user(id=6, password="pbkdf2_sha256$10000$Fec9MI6rCP2C$QG9Om/kV1uPRR1L4xyilx2F02D5dXISpgvnxkeX/aQE=", last_login="2015-01-25 01:17:45.036092", is_superuser=1, username="ross", first_name="Ross", last_name="", email="", is_staff=1, is_active=1, date_joined="2015-01-25 01:17:45.036118")

    add_auth_user(id=7, password="pbkdf2_sha256$10000$xeuMlUUawXEj$biTz0tQgnipHdfynYBS0k7VTaaV6/6eiD4vXrI2ck+c=", last_login="2015-01-31 14:07:55.299000", is_superuser=1, username="atanas", first_name="Atanas", last_name="Pamukchiev", email="", is_staff=1, is_active=1, date_joined="2015-01-25 01:18:05")

    add_auth_user_groups(id=1, user_id=7, group_id=1)

    add_auth_user_groups(id=3, user_id=4, group_id=3)

    add_auth_user_groups(id=4, user_id=3, group_id=2)

    add_auth_user_groups(id=5, user_id=5, group_id=1)

    add_auth_user_groups(id=6, user_id=5, group_id=2)

    add_auth_user_groups(id=7, user_id=5, group_id=3)

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_auth_group(id,name):
    p = auth_group.objects.get_or_create(id=id, name=name)[0]
    return p

def add_auth_user(id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined):
    c = auth_user.objects.get_or_create(id=id, password=password, last_login=last_login, is_superuser=is_superuser, username=username, first_name=first_name, last_name=last_name, email=email, is_staff=is_staff, is_active=is_active, date_joined=date_joined)[0]
    return c
def add_auth_user_groups(id, user_id, group_id):
    g = add_auth_user_group.objects.get_or_create(id=id, user_id=user_id, group_id=group_id)
    return g;

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
    from rango.models import Category, Page
    populate()