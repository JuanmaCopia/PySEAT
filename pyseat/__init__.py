import sys
import os

folder = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path = [folder, os.path.dirname(folder)] + sys.path
