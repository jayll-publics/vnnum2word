# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import unicode_literals
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from unittest import TestCase
from vnnum2word import convert_number


class WordConverterTest(TestCase):

    def test_0(self):
        self.assertEqual(convert_number(0), "không")

    def test_1_to_10(self):
        self.assertEqual(convert_number(1), "một")
        self.assertEqual(convert_number(2), "hai")
        self.assertEqual(convert_number(7), "bảy")
        self.assertEqual(convert_number(10), "mười")

    def test_11_to_19(self):
        self.assertEqual(convert_number(11), "mười một")
        self.assertEqual(convert_number(13), "mười ba")
        self.assertEqual(convert_number(14), "mười bốn")
        self.assertEqual(convert_number(15), "mười lăm")
        self.assertEqual(convert_number(16), "mười sáu")
        self.assertEqual(convert_number(19), "mười chín")

    def test_20_to_99(self):
        self.assertEqual(convert_number(20), "hai mươi")
        self.assertEqual(convert_number(23), "hai mươi ba")
        self.assertEqual(convert_number(28), "hai mươi tám")
        self.assertEqual(convert_number(31), "ba mươi mốt")
        self.assertEqual(convert_number(40), "bốn mươi")
        self.assertEqual(convert_number(66), "sáu mươi sáu")
        self.assertEqual(convert_number(92), "chín mươi hai")

    def test_100_to_999(self):
        self.assertEqual(convert_number(100), "một trăm")
        self.assertEqual(convert_number(150), "một trăm năm mươi")
        self.assertEqual(
            convert_number(196), "một trăm chín mươi sáu"
        )
        self.assertEqual(convert_number(200), "hai trăm")
        self.assertEqual(convert_number(210), "hai trăm mười")

    def test_1000_to_9999(self):
        self.assertEqual(convert_number(1000), "một nghìn")
        self.assertEqual(convert_number(1500), "một nghìn năm trăm")
        self.assertEqual(
            convert_number(7378), "bảy nghìn ba trăm bảy mươi tám"
        )
        self.assertEqual(convert_number(2000), "hai nghìn")
        self.assertEqual(convert_number(2100), "hai nghìn một trăm")
        self.assertEqual(
            convert_number(6870), "sáu nghìn tám trăm bảy mươi"
        )
        self.assertEqual(convert_number(10000), "mười nghìn")
        self.assertEqual(convert_number(100000), "một trăm nghìn")
        self.assertEqual(
            convert_number(523456),
            "năm trăm hai mươi ba nghìn bốn trăm năm mươi sáu"
        )

    def test_big(self):
        self.assertEqual(convert_number(1000000), "một triệu")
        self.assertEqual(
            convert_number(1200000), "một triệu hai trăm nghìn"
        )
        self.assertEqual(convert_number(3000000), "ba triệu")
        self.assertEqual(
            convert_number(3800000), "ba triệu tám trăm nghìn"
        )
        self.assertEqual(convert_number(1000000000), "một tỷ")
        self.assertEqual(convert_number(2000000000), "hai tỷ")
        self.assertEqual(
            convert_number(2000001000), "hai tỷ một nghìn"
        )
        self.assertEqual(
            convert_number(1234567890),
            "một tỷ hai trăm ba mươi bốn triệu năm trăm sáu mươi bảy nghìn "
            "tám trăm chín mươi"
        )

    def test_decimal_number(self):
        self.assertEqual(
            convert_number(1000.11), "một nghìn phẩy mười một"
        )
        self.assertEqual(
            convert_number(1000.21), "một nghìn phẩy hai mươi mốt"
        )

    def test_special_number(self):
        """
        Some number will have some specail rule
        """
        self.assertEqual(convert_number(21), "hai mươi mốt")
        self.assertEqual(convert_number(25), "hai mươi lăm")
        # >100
        self.assertEqual(convert_number(101), "một trăm lẻ một")
        self.assertEqual(convert_number(105), "một trăm lẻ năm")
        self.assertEqual(convert_number(701), "bảy trăm lẻ một")
        self.assertEqual(convert_number(705), "bảy trăm lẻ năm")

        # >1000
        self.assertEqual(convert_number(1001), "một nghìn lẻ một")
        self.assertEqual(convert_number(1005), "một nghìn lẻ năm")
        self.assertEqual(
            convert_number(98765),
            "chín mươi tám nghìn bảy trăm sáu mươi lăm"
        )

        # > 1000000
        self.assertEqual(convert_number(3000005), "ba triệu lẻ năm")
        self.assertEqual(convert_number(1000007), "một triệu lẻ bảy")

        # > 1000000000
        self.assertEqual(
            convert_number(1000000017), "một tỷ lẻ mười bảy"
        )
        self.assertEqual(
            convert_number(1000101017),
            "một tỷ một trăm lẻ một nghìn lẻ mười bảy"
        )
    
    def test_2_decimal_number(self):
        self.assertEqual(
            convert_number(1000.11), "một nghìn phẩy mười một"
        )
        self.assertEqual(
            convert_number(13.21), "mười ba phẩy hai mươi mốt"
        )
        self.assertEqual(
            convert_number(19.5), "mười chín phẩy năm"
        )
        self.assertEqual(
            convert_number(19.00), "mười chín"
        )