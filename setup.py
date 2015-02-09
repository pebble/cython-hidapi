from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import os
import platform

print platform.system()

if platform.system() == 'Darwin':
	os.environ['CFLAGS'] = "-framework IOKit -framework CoreFoundation"
	os.environ['LDFLAGS'] = ""

	setup(
	    cmdclass = {'build_ext': build_ext},
	    ext_modules = [Extension("hid", ["hid.pyx", "hid-mac.c"])]
	)
elif platform.system() == 'Windows':
	setup(
	    cmdclass = {'build_ext': build_ext},
	    ext_modules = [Extension("hid", ["hid.pyx", "hid-windows.c"],
	                             libraries=["setupapi"])]
	)
else:
	os.environ['CFLAGS'] = "-I/usr/include/libusb-1.0"
	os.environ['LDFLAGS'] = "-L/usr/lib/i386-linux-gnu -lusb-1.0 -ludev -lrt"

	setup(
	    cmdclass = {'build_ext': build_ext},
	    ext_modules = [Extension("hid", ["hid.pyx", "hid-libusb.c"])]
	)