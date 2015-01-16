#############################################################################
#                         Conceptual database models                        #
#               Based on the ER Diagram and Django's DB interaction         #
#                                                                           #
#   See http://www.tangowithdjango.com/book/chapters/models.html            #
#                                                                           #   
# This file defines the Tables's names for internal (within django) usage   #
# as well as defines the names and types of the tables attributes. Primary  #
# and foreign keys are defined using this module as well as some other shit #
#                                                                           # 
# There are probably still a lot of errors to be fixed, but meh...          #
# -Atanas                                                                   #
#                                                                           #
#############################################################################


from __future__ import unicode_literals

from django.db import models

class Address(models.Model):
    addressid = models.IntegerField(primary_key=True, db_column='addressID') # Field name made lowercase.
    city = models.CharField(max_length=45L, blank=True)
    country = models.CharField(max_length=45L, blank=True)
    street = models.CharField(max_length=45L, blank=True)
    number = models.IntegerField(null=True, blank=True)
    label = models.CharField(max_length=45L, blank=True)
    class Meta:
        db_table = 'address'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80L, unique=True)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50L)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100L)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128L)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(max_length=30L, unique=True)
    first_name = models.CharField(max_length=30L)
    last_name = models.CharField(max_length=30L)
    email = models.CharField(max_length=75L)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'

class Block(models.Model):
    blockid = models.IntegerField(primary_key=True, db_column='BlockID') # Field name made lowercase.
    begindate = models.DateField(db_column='beginDate') # Field name made lowercase.
    enddate = models.DateField(db_column='endDate') # Field name made lowercase.
    label = models.CharField(max_length=45L, blank=True)
    class Meta:
        db_table = 'block'

class BtmRank(models.Model):
    uid = models.ForeignKey('User', db_column='uID') # Field name made lowercase.
    membershipnum = models.IntegerField(null=True, db_column='membershipNum', blank=True) # Field name made lowercase.
    numofponts = models.IntegerField(null=True, db_column='numOfPonts', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'btm rank'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L)
    app_label = models.CharField(max_length=100L)
    model = models.CharField(max_length=100L)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40L, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100L)
    name = models.CharField(max_length=50L)
    class Meta:
        db_table = 'django_site'

class Experience(models.Model):
    experienceid = models.IntegerField(primary_key=True, db_column='experienceID') # Field name made lowercase.
    xp = models.ForeignKey('Experiencelevel', db_column='XP') # Field name made lowercase.
    class Meta:
        db_table = 'experience'

class Experiencelevel(models.Model):
    levelid = models.IntegerField(primary_key=True, db_column='levelID') # Field name made lowercase.
    label = models.CharField(max_length=45L, blank=True)
    class Meta:
        db_table = 'experiencelevel'

class Extras(models.Model):
    extrasid = models.IntegerField(primary_key=True, db_column='extrasID') # Field name made lowercase.
    label = models.CharField(max_length=45L, blank=True)
    price = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=45L, blank=True)
    ownersessionid = models.ForeignKey('Session', db_column='ownerSessionID') # Field name made lowercase.
    class Meta:
        db_table = 'extras'

class Logindetails(models.Model):
    password = models.CharField(max_length=45L, blank=True)
    username = models.CharField(max_length=45L, blank=True)
    user_uid = models.ForeignKey('User', primary_key=True, db_column='User_uID') # Field name made lowercase.
    class Meta:
        db_table = 'logindetails'

class Notes(models.Model):
    noteid = models.IntegerField(primary_key=True, db_column='noteID') # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True) # Field name made lowercase.
    session_sessionid = models.ForeignKey('Session', db_column='Session_sessionID') # Field name made lowercase.
    hasnotes = models.IntegerField(null=True, db_column='hasNotes', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'notes'

class Payment(models.Model):
    paymentid = models.IntegerField(primary_key=True, db_column='paymentID') # Field name made lowercase.
    amount = models.IntegerField(null=True, blank=True)
    label = models.CharField(max_length=45L, blank=True)
    haspayed = models.IntegerField(null=True, db_column='hasPayed', blank=True) # Field name made lowercase.
    duedate = models.DateField(null=True, db_column='dueDate', blank=True) # Field name made lowercase.
    payeddate = models.DateField(null=True, db_column='payedDate', blank=True) # Field name made lowercase.
    usertopay = models.ForeignKey('User', db_column='userToPay') # Field name made lowercase.
    paymenttype = models.ForeignKey('Paymenttype', db_column='paymentType') # Field name made lowercase.
    class Meta:
        db_table = 'payment'

class Paymenttype(models.Model):
    typeid = models.IntegerField(primary_key=True, db_column='typeID') # Field name made lowercase.
    typelabel = models.CharField(max_length=45L, db_column='typeLabel', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'paymenttype'

class Privelegetypes(models.Model):
    priveleges = models.TextField(primary_key=True) # This field type is a guess.
    privelegelabel = models.CharField(max_length=45L, db_column='privelegeLabel', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'privelegetypes'

class Privileges(models.Model):
    privilegeid = models.IntegerField(primary_key=True, db_column='privilegeID') # Field name made lowercase.
    privilege = models.ForeignKey(Privelegetypes, db_column='privilege')
    class Meta:
        db_table = 'privileges'

class Session(models.Model):
    sessionid = models.IntegerField(primary_key=True, db_column='sessionID') # Field name made lowercase.
    duration = models.CharField(max_length=45L, blank=True)
    begintime = models.DateTimeField(null=True, db_column='beginTime', blank=True) # Field name made lowercase.
    endtime = models.DateTimeField(null=True, db_column='endTime', blank=True) # Field name made lowercase.
    block_blockid = models.ForeignKey(Block, db_column='Block_BlockID') # Field name made lowercase.
    capacity = models.IntegerField(null=True, blank=True)
    agegroup = models.CharField(max_length=45L, db_column='ageGroup', blank=True) # Field name made lowercase.
    skillgroup = models.CharField(max_length=45L, db_column='skillGroup', blank=True) # Field name made lowercase.
    isfull = models.CharField(max_length=45L, db_column='isFull', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'session'

class Subvenue(models.Model):
    subvenueid = models.IntegerField(primary_key=True, db_column='subVenueID') # Field name made lowercase.
    label = models.CharField(max_length=45L, blank=True)
    capacity = models.CharField(max_length=45L, blank=True)
    ownervenue = models.ForeignKey('Venue', db_column='ownerVenue') # Field name made lowercase.
    class Meta:
        db_table = 'subvenue'

class SubvenueUsedforSession(models.Model):
    session_sessionid = models.ForeignKey(Session, db_column='Session_sessionID', primary_key=True) # Field name made lowercase.
    subvenue_subvenueid = models.ForeignKey(Subvenue, db_column='SubVenue_subVenueID', related_name='subvenue_id') # Field name made lowercase.
    subvenue_ownervenue = models.ForeignKey(Subvenue, db_column='SubVenue_ownerVenue', related_name='subvenue_owner') # Field name made lowercase.
    class Meta:
        db_table = 'subvenue_usedfor_session'

class User(models.Model):
    uid = models.IntegerField(primary_key=True, db_column='uID') # Field name made lowercase.
    firstname = models.CharField(max_length=45L, db_column='firstName', blank=True) # Field name made lowercase.
    lastname = models.CharField(max_length=45L, db_column='lastName', blank=True) # Field name made lowercase.
    email = models.CharField(max_length=45L, blank=True)
    telephone = models.BigIntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    medicalcondition = models.CharField(max_length=45L, db_column='medicalCondition', blank=True) # Field name made lowercase.
    ismember = models.IntegerField(null=True, db_column='isMember', blank=True) # Field name made lowercase.
    managedby = models.IntegerField(null=True, db_column='managedBy', blank=True) # Field name made lowercase.
    privilegeid = models.ForeignKey(Privileges, db_column='privilegeID') # Field name made lowercase.
    xperienceid = models.ForeignKey(Experience, db_column='xperienceID') # Field name made lowercase.
    belongsto = models.IntegerField(db_column='belongsTo') # Field name made lowercase.
    genderid = models.IntegerField(null=True, db_column='genderID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'user'

class UserSelectsSession(models.Model):
    user_uid = models.ForeignKey(User, db_column='User_uID', primary_key=True) # Field name made lowercase.
    session_sessionid = models.ForeignKey(Session, db_column='Session_sessionID') # Field name made lowercase.
    class Meta:
        db_table = 'user_selects_session'

class Venue(models.Model):
    venueid = models.IntegerField(primary_key=True,db_column='venueID') # Field name made lowercase.
    capacity = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=45L, blank=True)
    load = models.IntegerField(null=True, blank=True)
    manager = models.ForeignKey(User, db_column='Manager') # Field name made lowercase.
    address_addressid = models.ForeignKey(Address, db_column='Address_addressID') # Field name made lowercase.
    class Meta:
        db_table = 'venue'

