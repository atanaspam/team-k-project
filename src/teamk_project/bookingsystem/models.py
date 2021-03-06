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
# A whole new version with a lot of tables removed and multoiple fields     #
# optimised.                                                                #
# -Atanas                                                                   #
#                                                                           #
#############################################################################
from __future__ import unicode_literals

from django.db import models
from django.db.models import Min
from django.contrib.auth.models import User
import datetime

TYPE_CHOICES = (
	('Morning', 'Morning'),
	('Afternoon', 'Afternoon'),
	('Week', 'Week'),
	('Season', 'Season'),
)

GENDER_CHOICES = (
	(1, 'Male'),
	(0, 'Female')
	)

DURATION_TYPES = (
		('0:30:00', '30 minutes'),
		('1:00:00', '1 hour'),
		('1:30:00', '1:30 hours'),
		('2:00:00', '2 hours'),
		('-1', 'Other'),
		)

@property
def nextArrivalDate(self):
	return self.userselectssession_set.filter(session_sessionid__begintime__gte=datetime.datetime.now()).aggregate(Min('session_sessionid__begintime')).get('session_sessionid__begintime__min')

def __unicode__(self):
	return "%s %s" % (self.firstname, self.lastname)
class Meta:
	db_table = 'client'

class ClientManager(models.Manager):
	def getMales(self):
		return self.filter(genderid = 1)
	def getFemales(self):
		return self.filter(genderid = 0)

# User

class Address(models.Model):
	addressid = models.AutoField(primary_key=True, db_column='addressID') # Field name made lowercase.
	city = models.CharField(max_length=45, blank=True)
	country = models.CharField(max_length=45, blank=True)
	street = models.CharField(max_length=45, blank=True)
	number = models.IntegerField(null=True, blank=True)
	label = models.CharField(max_length=45, blank=True)
	class Meta:
		db_table = 'address'

class AdditionalInfo(models.Model):
	user = models.OneToOneField(User)
	telephone = models.IntegerField()

# Client - Child

class Client(models.Model):
	uid = models.AutoField(primary_key=True, db_column='uID') # Field name made lowercase.
	firstname = models.CharField(max_length=45, db_column='firstName', blank=True) # Field name made lowercase.
	lastname = models.CharField(max_length=45, db_column='lastName', blank=True) # Field name made lowercase.
	email = models.CharField(max_length=45, blank=True)
	telephone = models.IntegerField(blank=True) # This field type is a guess.
	dateofbirth = models.DateField(null=False, blank=False, db_column='dateofbirth')
	ismember = models.BooleanField(db_column='isMember', blank=True) # Field name made lowercase.
	managedby = models.ForeignKey(User, null=True, db_column='managedBy', blank=True, related_name='Manager') # Field name made lowercase.
	belongsto = models.ForeignKey(User, db_column='belongsTo', related_name='Parent') # Field name made lowercase.
	genderid = models.IntegerField(null=True, db_column='genderID', blank=True, choices = GENDER_CHOICES) # Field name made lowercase.
	experiencelevel = models.IntegerField(db_column='experienceLevel') # Field name made lowercase.
	class Meta:
		db_table = 'client'

class Experiencelevel(models.Model):
	levelid = models.AutoField(primary_key=True, db_column='levelID') # Field name made lowercase.
	label = models.CharField(max_length=45, blank=True)
	class Meta:
		db_table = 'experiencelevel'

class Medicalcondition(models.Model):
	ownerid = models.AutoField(primary_key=True, db_column='ownerID') # Field name made lowercase.
	condition = models.CharField(max_length=45, blank=True)
	class Meta:
		db_table = 'medicalcondition'

class DefaultCoaches(models.Model):
	monMor = models.ForeignKey(User, null=True, related_name = 'MondayMorning')
	monAft = models.ForeignKey(User, null=True, related_name = 'MondayAfternoon')
	tueMor = models.ForeignKey(User, null=True, related_name = 'TuesdayMorning')
	tueAft = models.ForeignKey(User, null=True, related_name = 'TuesdayAfternon')
	wedMor = models.ForeignKey(User, null=True, related_name = 'WednesdayMorning')
	wedAft = models.ForeignKey(User, null=True, related_name = 'WednesdayAfternoon')
	thuMor = models.ForeignKey(User, null=True, related_name = 'ThursdayMorning')
	thuAft = models.ForeignKey(User, null=True, related_name = 'ThursdayAfternoon')
	friMor = models.ForeignKey(User, null=True, related_name = 'FridayMorning')
	friAft = models.ForeignKey(User, null=True, related_name = 'FridayAfternoon')

# Blocks and Sessions

class Block(models.Model):
	blockid = models.AutoField(primary_key=True, db_column='BlockID') # Field name made lowercase.
	begindate = models.DateField(db_column='beginDate') # Field name made lowercase.
	enddate = models.DateField(db_column='endDate') # Field name made lowercase.
	label = models.CharField(max_length=45, blank=True)
	type = models.CharField(max_length=45, choices = TYPE_CHOICES)
	class Meta:
		db_table = 'block'
	def __str__(self):
		return '%s %s %s' % (self.begindate, self.enddate, self.label)

class Session(models.Model):
	sessionid = models.AutoField(primary_key=True, db_column='sessionID') # Field name made lowercase
	duration = models.CharField(max_length=45, blank=True, choices=DURATION_TYPES)
	begintime = models.DateTimeField(null=True, db_column='beginTime', blank=True) # Field name made lowercase.
	endtime = models.DateTimeField(null=True, db_column='endTime', blank=True) # Field name made lowercase.
	block_blockid = models.ForeignKey(Block, db_column='Block_BlockID') # Field name made lowercase.
	capacity = models.IntegerField(null=True, blank=True)
	agegroup = models.CharField(max_length=45, db_column='ageGroup', blank=True) # Field name made lowercase.
	skillgroup = models.CharField(max_length=45, db_column='skillGroup', blank=True) # Field name made lowercase.
	isfull = models.BooleanField(max_length=45, db_column='isFull', blank=True) # Field name made lowercase.
	coachedby = models.ManyToManyField(User, blank=True)
	class Meta:
			db_table = 'session'

class UserSelectsSession(models.Model):
	user_uid = models.ForeignKey(Client, db_column='User_uID') # Field name made lowercase.
	session_sessionid = models.ForeignKey(Session, db_column='Session_sessionID') # Field name made lowercase.
	status = models.CharField(max_length=1, blank=True)
	hasattended = models.BooleanField(db_column='hasattended')
	class Meta:
			unique_together = (("user_uid", "session_sessionid"),)
			db_table = 'user_selects_session'

# Coach

# class sessionCoachedBy(models.Model):
#     id = models.IntegerField(primary_key=True, db_column='id')
#     session_id = models.ForeignKey(Session, db_column='session_id')
#     user_id = models.ForeignKey(User, db_column='user_id')
#     class Meta:
#         db_table = 'session_coached_by'

class Notes(models.Model):
	noteid = models.AutoField(primary_key=True, db_column='noteID') # Field name made lowercase.
	note = models.TextField(db_column='Note', blank=True) # Field name made lowercase. This field type is a guess.
	session_sessionid = models.ForeignKey(Session, db_column='Session_sessionID') # Field name made lowercase.
	hasnotes = models.BooleanField(db_column='hasNotes', blank=True) # Field name made lowercase.
	class Meta:
		db_table = 'notes'


# Extras or Unused

class BtmRank(models.Model):
	uid = models.AutoField(primary_key=True, db_column='uID') # Field name made lowercase.
	membershipnum = models.IntegerField(null=True, db_column='membershipNum', blank=True) # Field name made lowercase.
	numofponts = models.IntegerField(null=True, db_column='numOfPonts', blank=True) # Field name made lowercase.
	class Meta:
		db_table = 'btm_rank'

class Extras(models.Model):
	extrasid = models.AutoField(primary_key=True, db_column='extrasID') # Field name made lowercase.
	label = models.CharField(max_length=45, blank=True)
	price = models.IntegerField(null=True, blank=True)
	description = models.CharField(max_length=45, blank=True)
	ownersessionid = models.ForeignKey(Session, db_column='ownerSessionID') # Field name made lowercase.
	class Meta:
		db_table = 'extras'

# Payments

class Paymenttype(models.Model):
	typeid = models.AutoField(primary_key=True, db_column='typeID') # Field name made lowercase.
	typelabel = models.CharField(max_length=45, db_column='typeLabel', blank=True) # Field name made lowercase.
	class Meta:
		db_table = 'paymenttype'

class Payment(models.Model):
	paymentid = models.AutoField(primary_key=True, db_column='paymentID') # Field name made lowercase.
	usertopay = models.ForeignKey(Client, db_column='userToPay') # Field name made lowercase.
	paymenttype = models.ForeignKey(Paymenttype, db_column='paymentType') # Field name made lowercase.
	amount = models.IntegerField(null=True, blank=True)
	label = models.CharField(max_length=45, blank=True)
	haspayed = models.BooleanField(db_column='hasPayed', blank=True) # Field name made lowercase.
	duedate = models.DateField(null=True, db_column='dueDate', blank=True) # Field name made lowercase.
	payeddate = models.DateField(null=True, db_column='payedDate', blank=True) # Field name made lowercase.
	class Meta:
		db_table = 'payment'

# Venue

class Venue(models.Model):
	venueid = models.AutoField(primary_key=True, db_column='venueID') # Field name made lowercase.
	capacity = models.IntegerField(null=True, blank=True)
	name = models.CharField(max_length=45, blank=True)
	load = models.IntegerField(null=True, blank=True)
	manager = models.ForeignKey(User, db_column='Manager') # Field name made lowercase.
	address_addressid = models.ForeignKey(Address, db_column='Address_addressID') # Field name made lowercase.
	class Meta:
		db_table = 'venue'

class Subvenue(models.Model):
	subvenueid = models.AutoField(primary_key=True, db_column='subVenueID') # Field name made lowercase.
	label = models.CharField(max_length=45, blank=True)
	capacity = models.IntegerField(blank=True)
	ownervenue = models.ForeignKey(Venue, db_column='ownerVenue') # Field name made lowercase.
	class Meta:
		db_table = 'subvenue'

class SubvenueUsedforSession(models.Model):
	session_sessionid = models.ForeignKey(Session, db_column='Session_sessionID') # Field name made lowercase.
	subvenue_subvenueid = models.ForeignKey(Subvenue, db_column='SubVenue_subVenueID') # Field name made lowercase. , related_name='subvenue_id'
	subvenue_ownervenue = models.IntegerField(db_column='SubVenue_ownerVenue') # Field name made lowercase. , related_name='subvenue_owner'
	class Meta:
			unique_together = (("subvenue_subvenueid", "session_sessionid"),)
			db_table = 'subvenue_usedfor_session'

