import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/akannan05/Desktop/endoscope/endoscope-camera/endo_ws/install/infer'
