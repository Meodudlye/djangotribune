# -*- coding: utf-8 -*-
"""
Tribune command line
"""
import json

from optparse import OptionValueError, make_option

from django.conf import settings
from django.core.cache import cache
from django.core.management.base import CommandError, BaseCommand
from django.contrib.auth.models import User

from djangotribune.models import Message

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option("--build_test_attempts", dest="build_test_attempts", action="store_true", default=None, help="Print out some values to check in the unittests. For Development purpose only."),
    )
    help = "Command for Sveetchies-tribune"

    def handle(self, *args, **options):
        if len(args) != 0:
            raise CommandError("Command doesn't accept any arguments")
        
        self.build_test_attempts = options.get('build_test_attempts')
        self.verbosity = int(options.get('verbosity'))
        
        if self.build_test_attempts:
            self.do_build_test_attempts()

    def do_build_test_attempts(self):
        """
        Create values to attempt in unittests
        """
        # Users
        self.user_with_filter_1 = User.objects.get(username='user_with_filter_1')
        self.user_with_filter_2 = User.objects.get(username='user_with_filter_2')
        
        # With anonymous, with no channel filter
        base_total = Message.objects.orderize()
        base_from_10 = Message.objects.orderize(10)
        print "base_total =", list(base_total.flat())
        print "base_from_10 =", list(base_from_10.flat())
        print "base_from_10_limit_10 =", list(base_from_10[:10].flat())
        print
        
        # With anonymous, with default channel filter
        default_chan_total = Message.objects.orderize().from_chan()
        default_chan_from_10 = Message.objects.orderize(10).from_chan()
        #backend_default_chan_total = Message.objects.orderize().from_chan()
        print "default_chan_total =", list(default_chan_total.flat())
        print "default_chan_from_10 =", list(default_chan_from_10.flat())
        print "default_chan_from_10_limit_10 =", list(default_chan_from_10[:10].flat())
        print
        
        # With superman
        #self.user_with_filter_1.filterentry_set.get_filters_args()
        user_with_filter_1_total = Message.objects.from_chan("troie").bunkerize(self.user_with_filter_1).orderize()
        user_with_filter_1_from_10 = Message.objects.from_chan("troie").bunkerize(self.user_with_filter_1).orderize(10)
        print "user_with_filter_1_total =", list(user_with_filter_1_total.flat())
        print "user_with_filter_1_from_10 =", list(user_with_filter_1_from_10.flat())
        print "user_with_filter_1_from_10_limit_10 =", list(user_with_filter_1_from_10[:10].flat())
        print
        
        # With wonderwoman
        #self.user_with_filter_2.filterentry_set.get_filters_args()
        user_with_filter_2_total = Message.objects.from_chan("troie").bunkerize(self.user_with_filter_2).orderize()
        user_with_filter_2_from_10 = Message.objects.from_chan("troie").bunkerize(self.user_with_filter_2).orderize(10)
        print "user_with_filter_2_total =", list(user_with_filter_2_total.flat())
        print "user_with_filter_2_from_10 =", list(user_with_filter_2_from_10.flat())
        print "user_with_filter_2_from_10_limit_10 =", list(user_with_filter_2_from_10[:10].flat())
        print