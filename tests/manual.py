import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vnnum2word import convert_number, convert_string

print(convert_number(3.141592))
print(convert_string("giải thưởng là 1000000 đồng"))