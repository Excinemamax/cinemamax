# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Buyticket(models.Model):
    buyid = models.IntegerField(primary_key=True)
    sessionid = models.ForeignKey('Sessions', models.DO_NOTHING, db_column='sessionid', blank=True, null=True)
    seatid = models.ForeignKey('Seats', models.DO_NOTHING, db_column='seatid', blank=True, null=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    isbuy = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buyticket'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Film(models.Model):
    namefilm = models.CharField(primary_key=True, max_length=20)
    description = models.TextField(blank=True, null=True)
    imgurl = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film'


class Filmgenre(models.Model):
    idfilmgenre = models.IntegerField(primary_key=True)
    filmname = models.ForeignKey(Film, models.DO_NOTHING, db_column='filmname', blank=True, null=True)
    genreid = models.ForeignKey('Genre', models.DO_NOTHING, db_column='genreid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filmgenre'


class Genre(models.Model):
    idgenre = models.IntegerField(primary_key=True)
    namegenre = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genre'


class Hall(models.Model):
    idhall = models.IntegerField(primary_key=True)
    format = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hall'


class Seats(models.Model):
    idseats = models.IntegerField(primary_key=True)
    hallid = models.ForeignKey(Hall, models.DO_NOTHING, db_column='hallid', blank=True, null=True)
    num = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seats'


class Sessions(models.Model):
    idsession = models.IntegerField(primary_key=True)
    fillname = models.ForeignKey(Film, models.DO_NOTHING, db_column='fillname', blank=True, null=True)
    datasession = models.DateTimeField(blank=True, null=True)
    numberhall = models.ForeignKey(Hall, models.DO_NOTHING, db_column='numberhall', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessions'


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    uname = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    card = models.BigIntegerField(blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
