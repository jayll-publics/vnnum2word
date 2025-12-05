from __future__ import unicode_literals

import os
import sys
from unittest import TestCase

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vnnum2word import convert_string


class StringConverterTest(TestCase):

    def test_no_number(self):
        text = "không có số nào trong chuỗi này"
        self.assertEqual(convert_string(text), text)

    def test_single_small_number(self):
        self.assertEqual(
            convert_string("tôi có 5 quả táo"),
            "tôi có năm quả táo"
        )
        self.assertEqual(
            convert_string("anh ấy đứng thứ 1"),
            "anh ấy đứng thứ một"
        )

    def test_multiple_numbers_in_one_string(self):
        self.assertEqual(
            convert_string("năm 1990 có 12 tháng"),
            "năm một nghìn chín trăm chín mươi có mười hai tháng"
        )
        self.assertEqual(
            convert_string("từ 10 đến 20"),
            "từ mười đến hai mươi"
        )

    def test_large_number(self):
        self.assertEqual(
            convert_string("giải thưởng là 1000000 đồng"),
            "giải thưởng là một triệu đồng"
        )
        self.assertEqual(
            convert_string("tổng cộng: 1234567890"),
            "tổng cộng: một tỷ hai trăm ba mươi bốn triệu "
            "năm trăm sáu mươi bảy nghìn tám trăm chín mươi"
        )

    def test_numbers_adjacent_to_letters(self):
        # Regex \d+ sẽ bắt được "123" trong "abc123def"
        self.assertEqual(
            convert_string("mã abc123def"),
            "mã abc một hai ba def"
        )
        self.assertEqual(
            convert_string("sp001"),
            "sp không không một"
        )

    def test_decimal_with_comma(self):
        # Dấu thập phân mặc định là dấu phẩy ","
        self.assertEqual(
            convert_string("số pi xấp xỉ 3,14"),
            "số pi xấp xỉ ba phẩy mười bốn"
        )
