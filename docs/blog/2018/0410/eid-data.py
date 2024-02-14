#!/usr/bin/env python
#
# Copyright (C) 2017 Vincent Hardy (vincent.hardy.be@gmail.com)
#
# This is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version
# 3.0 as published by the Free Software Foundation.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; if not, see
# https://www.gnu.org/licenses/
#

from PyKCS11 import *
import platform
import sys


class BEID(object):

    def __init__(self):
        self.pkcs11 = PyKCS11.PyKCS11Lib()
        if platform.system().lower() != 'windows':
            self.pkcs11.load('libbeidpkcs11.so.0')
        else:
            self.pkcs11.load('beidpkcs11.dll')

    def show_info(self):
        print(self.pkcs11.getInfo())
        print('======================================================')

    def open_session(self, slot):
        return self.pkcs11.openSession(slot)

    def getData(self, session, name, filename=None):
        lst = session.findObjects([(CKA_CLASS, CKO_DATA), (CKA_LABEL, name)])
        if len(lst) == 0:
            return
        o = lst[0]
        value = session.getAttributeValue(o, [CKA_VALUE])[0]
        # print(value)
        text = ''.join([chr(i) for i in value])
        # text = bytes(value).decode('utf-8')
        if filename:
            open(filename, 'w').write(text)
        else:
            print("{}: {}".format(name, text))


if __name__ == '__main__':

    beid = BEID()
    beid.show_info()

    slots = beid.pkcs11.getSlotList()

    if len(slots) == 0:
        sys.exit(2)

    for slot in slots:
        try:
            sess = beid.open_session(slot)

            # print(dir(sess))
            objs = sess.findObjects([(CKA_CLASS, CKO_DATA)])
            # print(len(objs))
            # print(type(objs[0]), dir( objs[0]), objs[0].to_dict())
            # for o in objs:
            #     d=o.to_dict()
            #     d['TLV'] = ''.join(chr(i) for i in d['CKA_VALUE']) if 'CKA_VALUE' in d else ''
            #     print("%(CKA_CLASS)s %(CKA_LABEL)s %(TLV)r" % d )
            for o in objs:
                d = o.to_dict()
                # ''.join(chr(i) for i in d['CKA_VALUE']) if 'CKA_VALUE' in d else ''
                print(d['CKA_LABEL'])
            # beid.getData(sess, 'surname')
            # beid.getData(sess, 'firstnames')
            # beid.getData(sess, 'other_names')
            # beid.getData(sess, 'PHOTO_FILE', 'foto.jpg')
            # beid.getData(sess, 'gender')
            # beid.getData(sess, 'nationality')
            # beid.getData(sess, 'document_type')
            # beid.getData(sess, 'address_municipality')
            # beid.getData(sess, 'address_zip
            # beid.getData(sess, 'date_of_birth')
            # beid.getData(sess, 'national_id')
            # beid.getData(sess, 'card_id')
            # beid.getData(sess, 'valid_until')
            # beid.getData(sess, 'location_of_birth')
            # beid.getData(sess, 'date_issued')
            # beid.getData(sess, 'address_street_and_number')
            # beid.getData(sess, 'ADDRESS_FILE')
            # beid.getData(sess, 'date_and_country_of_protection')

            # beid.getData(sess, 'ResidencePermitType')
            # beid.getData(sess, 'remark1')
            # beid.getData(sess, 'remark2')
            # beid.getData(sess, 'remark3')
            # beid.getData(sess, 'remark4')
        except PyKCS11.PyKCS11Error as e:
            print("Error: {}".format(e))
