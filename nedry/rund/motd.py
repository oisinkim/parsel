#!/usr/bin/env python

from random import choice

quotes = ["Nobody tells me nothing.",
          "Everyone and their mums is packing round here.",
          "We've got red... and... white?",
          "Ever fired your gun in the air and yelled, 'Aaaaaaah?'",
          "Ever been in a high-speed pursuit?",
          "The Greater Good.",
          "By the power of Greyskull! ",
          "You ain't seen Bad Boys II?",
          "Yarp.",
          "Crusty jugglers.",
          "Cornetto.",
          "Narp?"]


def node_type():
    print """
 _____           _  __
|__  /___   ___ | |/ /___  ___ _ __   ___ _ __
  / // _ \ / _ \| ' // _ \/ _ \ '_ \ / _ \ '__|
 / /| (_) | (_) | . \  __/  __/ |_) |  __/ |
/____\___/ \___/|_|\_\___|\___| .__/ \___|_|
                              |_|
    "%s"

Logs:
   tail -f /var/log/zookeeper/zookeeper.log
   tail -f /var/log/supervisor/exhibitor/exhibitor.err
   tail -f /var/log/supervisor/exhibitor/exhibitor.out

Exhibitor Commands:
  More: https://github.com/Netflix/exhibitor/wiki/REST-Introduction
""" % (choice(quotes))


def run():
    node_type()

run()
