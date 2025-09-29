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
from vnnum2word import WordConverter
from decimal import Decimal


class WordConverterTest(TestCase):

    def test_0(self):
        self.assertEqual(WordConverter()(0), "không")

    def test_1_to_10(self):
        self.assertEqual(WordConverter()(1), "một")
        self.assertEqual(WordConverter()(2), "hai")
        self.assertEqual(WordConverter()(7), "bảy")
        self.assertEqual(WordConverter()(10), "mười")

    def test_11_to_19(self):
        self.assertEqual(WordConverter()(11), "mười một")
        self.assertEqual(WordConverter()(13), "mười ba")
        self.assertEqual(WordConverter()(14), "mười bốn")
        self.assertEqual(WordConverter()(15), "mười lăm")
        self.assertEqual(WordConverter()(16), "mười sáu")
        self.assertEqual(WordConverter()(19), "mười chín")

    def test_20_to_99(self):
        self.assertEqual(WordConverter()(20), "hai mươi")
        self.assertEqual(WordConverter()(23), "hai mươi ba")
        self.assertEqual(WordConverter()(28), "hai mươi tám")
        self.assertEqual(WordConverter()(31), "ba mươi mốt")
        self.assertEqual(WordConverter()(40), "bốn mươi")
        self.assertEqual(WordConverter()(66), "sáu mươi sáu")
        self.assertEqual(WordConverter()(92), "chín mươi hai")

    def test_100_to_999(self):
        self.assertEqual(WordConverter()(100), "một trăm")
        self.assertEqual(WordConverter()(150), "một trăm năm mươi")
        self.assertEqual(
            WordConverter()(196), "một trăm chín mươi sáu"
        )
        self.assertEqual(WordConverter()(200), "hai trăm")
        self.assertEqual(WordConverter()(210), "hai trăm mười")

    def test_1000_to_9999(self):
        self.assertEqual(WordConverter()(1000), "một nghìn")
        self.assertEqual(WordConverter()(1500), "một nghìn năm trăm")
        self.assertEqual(
            WordConverter()(7378), "bảy nghìn ba trăm bảy mươi tám"
        )
        self.assertEqual(WordConverter()(2000), "hai nghìn")
        self.assertEqual(WordConverter()(2100), "hai nghìn một trăm")
        self.assertEqual(
            WordConverter()(6870), "sáu nghìn tám trăm bảy mươi"
        )
        self.assertEqual(WordConverter()(10000), "mười nghìn")
        self.assertEqual(WordConverter()(100000), "một trăm nghìn")
        self.assertEqual(
            WordConverter()(523456),
            "năm trăm hai mươi ba nghìn bốn trăm năm mươi sáu"
        )

    def test_big(self):
        self.assertEqual(WordConverter()(1000000), "một triệu")
        self.assertEqual(
            WordConverter()(1200000), "một triệu hai trăm nghìn"
        )
        self.assertEqual(WordConverter()(3000000), "ba triệu")
        self.assertEqual(
            WordConverter()(3800000), "ba triệu tám trăm nghìn"
        )
        self.assertEqual(WordConverter()(1000000000), "một tỷ")
        self.assertEqual(WordConverter()(2000000000), "hai tỷ")
        self.assertEqual(
            WordConverter()(2000001000), "hai tỷ một nghìn"
        )
        self.assertEqual(
            WordConverter()(1234567890),
            "một tỷ hai trăm ba mươi bốn triệu năm trăm sáu mươi bảy nghìn "
            "tám trăm chín mươi"
        )

    def test_decimal_number(self):
        self.assertEqual(
            WordConverter()(1000.11), "một nghìn phẩy mười một"
        )
        self.assertEqual(
            WordConverter()(1000.21), "một nghìn phẩy hai mươi mốt"
        )

    def test_special_number(self):
        """
        Some number will have some specail rule
        """
        self.assertEqual(WordConverter()(21), "hai mươi mốt")
        self.assertEqual(WordConverter()(25), "hai mươi lăm")
        # >100
        self.assertEqual(WordConverter()(101), "một trăm lẻ một")
        self.assertEqual(WordConverter()(105), "một trăm lẻ năm")
        self.assertEqual(WordConverter()(701), "bảy trăm lẻ một")
        self.assertEqual(WordConverter()(705), "bảy trăm lẻ năm")

        # >1000
        self.assertEqual(WordConverter()(1001), "một nghìn lẻ một")
        self.assertEqual(WordConverter()(1005), "một nghìn lẻ năm")
        self.assertEqual(
            WordConverter()(98765),
            "chín mươi tám nghìn bảy trăm sáu mươi lăm"
        )

        # > 1000000
        self.assertEqual(WordConverter()(3000005), "ba triệu lẻ năm")
        self.assertEqual(WordConverter()(1000007), "một triệu lẻ bảy")

        # > 1000000000
        self.assertEqual(
            WordConverter()(1000000017), "một tỷ lẻ mười bảy"
        )
        self.assertEqual(
            WordConverter()(1000101017),
            "một tỷ một trăm lẻ một nghìn lẻ mười bảy"
        )
    
    def test_2_decimal_number(self):
        self.assertEqual(
            WordConverter()(1000.11), "một nghìn phẩy mười một"
        )
        self.assertEqual(
            WordConverter()(13.21), "mười ba phẩy hai mươi mốt"
        )
        self.assertEqual(
            WordConverter()(19.5), "mười chín phẩy năm"
        )
        self.assertEqual(
            WordConverter()(19.00), "mười chín"
        )

    def test_fraction_more_than_two_digits_digitwise(self):
        self.assertEqual(
            WordConverter()(Decimal('12.123')), "mười hai phẩy một hai ba"
        )
        self.assertEqual(
            WordConverter()(Decimal('12.556')), "mười hai phẩy năm năm sáu"
        )
        self.assertEqual(
            WordConverter()(Decimal('1000.2135')), "một nghìn phẩy hai một ba năm"
        )

    def test_fraction_trailing_zeros_trim(self):
        self.assertEqual(
            WordConverter()(12.1200), "mười hai phẩy mười hai"
        )
        self.assertEqual(
            WordConverter()(12.100), "mười hai phẩy một"
        )
        # existing behavior: if fractional becomes 0 -> drop fractional part
        self.assertEqual(
            WordConverter()(19.00), "mười chín"
        )

    def test_input_types(self):
        self.assertEqual(
            WordConverter()(Decimal('12.123')), "mười hai phẩy một hai ba"
        )
        self.assertEqual(
            WordConverter()(12.123), "mười hai phẩy một hai ba"
        )

    def test_one_two_decimal_digits_unchanged(self):
        self.assertEqual(
            WordConverter()(12.55), "mười hai phẩy năm mươi lăm"
        )
        self.assertEqual(
            WordConverter()(12.5), "mười hai phẩy năm"
        )