
# -*- coding: utf-8 -*-
'''
    vdirsyncer.tests.storage.dav
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2014 Markus Unterwaditzer
    :license: MIT, see LICENSE for more details.
'''

import os

from .. import StorageTests
import vdirsyncer.exceptions as exceptions
from vdirsyncer.storage.base import Item


dav_server = os.environ.get('DAV_SERVER', '').strip() or 'radicale'
if dav_server in ('radicale', 'radicale_git'):
    from ._radicale import ServerMixin
else:
    raise RuntimeError('{} is not a known DAV server.'.format(dav_server))


class DavStorageTests(ServerMixin, StorageTests):
    def test_dav_broken_item(self):
        item = Item(u'UID:1')
        s = self._get_storage()
        try:
            s.upload(item)
        except exceptions.Error:
            pass
        assert not list(s.list())
