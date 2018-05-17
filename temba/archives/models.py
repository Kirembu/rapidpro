import boto3
from urllib.parse import urlparse

from django.conf import settings
from django.db import models

from gettext import gettext as _
from django.utils import timezone
from temba.utils import sizeof_fmt


class Archive(models.Model):
    DOWNLOAD_EXPIRES = 600
    TYPE_MSG = 'messages'
    TYPE_FLOWRUN = 'runs'

    PERIOD_MONTHLY = 'monthly'
    PERIOD_DAILY = 'daily'

    TYPE_CHOICES = (
        (TYPE_MSG, _("Message")),
        (TYPE_FLOWRUN, _("Run"))
    )

    org = models.ForeignKey('orgs.Org', db_constraint=False,
                            help_text="The org this archive is for")
    archive_type = models.CharField(choices=TYPE_CHOICES, max_length=16,
                                    help_text="The type of record this is an archive for")
    created_on = models.DateTimeField(default=timezone.now,
                                      help_text="When this archive was created")

    start_date = models.DateField(help_text="The starting modified_on date for records in this archive (inclusive")
    end_date = models.DateField(help_text="The ending modified_on date for records in this archive (exclusive)")

    record_count = models.IntegerField(default=0,
                                       help_text="The number of records in this archive")

    archive_size = models.IntegerField(default=0,
                                       help_text="The size of this archive in bytes (after gzipping)")
    archive_hash = models.TextField(help_text="The md5 hash of this archive (after gzipping)")
    archive_url = models.URLField(help_text="The full URL for this archive")

    is_purged = models.BooleanField(default=False,
                                    help_text="Whether the records in this archive have been purged from the database")
    build_time = models.IntegerField(help_text="The number of milliseconds it took to build and upload this archive")

    def archive_size_display(self):
        return sizeof_fmt(self.archive_size)

    def archive_period(self):
        if (self.end_date - self.start_date).days > 1:
            return Archive.PERIOD_MONTHLY
        return Archive.PERIOD_DAILY

    def get_s3_location(self):
        url_parts = urlparse(self.archive_url)
        return dict(Bucket=url_parts.netloc.split('.')[0], Key=url_parts.path[1:])

    def get_download_link(self):
        session = boto3.Session(aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
        s3 = session.client('s3')

        s3_params = {
            **self.get_s3_location(),
            # force browser to download and not uncompress our gzipped files
            'ResponseContentDisposition': 'attachment;',
            'ResponseContentType': 'application/octet',
            'ResponseContentEncoding': 'none',
        }

        return s3.generate_presigned_url('get_object', Params=s3_params, ExpiresIn=Archive.DOWNLOAD_EXPIRES)