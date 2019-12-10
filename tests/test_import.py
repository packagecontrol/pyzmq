import sublime

import unittest
import os
import sys


class TestImport(unittest.TestCase):
    mpath = None

    @classmethod
    def setUpClass(cls):
        basedir = os.path.dirname(__file__)
        mpath = os.path.normpath(os.path.join(
            basedir, "..", "st3_{}_{}".format(sublime.platform(), sublime.arch())))
        if mpath not in sys.path:
            cls.mpath = mpath
            sys.path.append(mpath)

    def test_toplevel(self):
        """test toplevel import"""
        import zmq  # noqa
        self.assertTrue("zmq" in sys.modules)

    def test_core(self):
        """test core imports"""
        from zmq import Context  # noqa
        from zmq import Socket  # noqa
        from zmq import Poller  # noqa
        from zmq import Frame  # noqa
        from zmq import constants  # noqa
        from zmq import device, proxy  # noqa
        from zmq import (    # noqa
            zmq_version,
            zmq_version_info,
            pyzmq_version,
            pyzmq_version_info,
        )

    def test_devices(self):
        """test device imports"""
        import zmq.devices  # noqa
        from zmq.devices import basedevice  # noqa
        from zmq.devices import monitoredqueue  # noqa
        from zmq.devices import monitoredqueuedevice  # noqa

    def test_log(self):
        """test log imports"""
        import zmq.log  # noqa
        from zmq.log import handlers  # noqa

    def test_eventloop(self):
        import zmq.eventloop  # noqa
        from zmq.eventloop import ioloop  # noqa
        from zmq.eventloop import zmqstream  # noqa

    def test_utils(self):
        """test util imports"""
        import zmq.utils  # noqa
        from zmq.utils import strtypes  # noqa
        from zmq.utils import jsonapi  # noqa

    def test_ssh(self):
        """test ssh imports"""
        from zmq.ssh import tunnel  # noqa

    def test_decorators(self):
        """test decorators imports"""
        from zmq.decorators import context, socket  # noqa


    @classmethod
    def tearDownClass(cls):
        if not cls.mpath:
            return
        mpath = cls.mpath
        if mpath in sys.path:
            sys.path.remove(mpath)
        if "psutil" in sys.modules:
            del sys.modules["psutil"]
