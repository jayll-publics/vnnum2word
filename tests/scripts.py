import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vnnum2word import WordConverter

print(WordConverter()(3.141592))