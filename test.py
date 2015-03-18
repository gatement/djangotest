import os

print __file__
print os.path.abspath(__file__)
print os.path.join(os.path.abspath(__file__), os.pardir)
print os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir))
print os.path.dirname(os.path.abspath(__file__))

