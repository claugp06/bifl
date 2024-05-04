#!/usr/bin/env python

from setuptools import setup, Extension


def mkcpy(name):
    return Extension('_' + name, ['bifl/cpy/%s.cpp' % (name,)],
                     include_dirs=['bifl/cpy'],
                     libraries=['c', 'opencv_imgproc', 'opencv_core'],)
with open('README.rst', 'r') as f:
    long_description = f.read()


setup(name='bifl',
      version='0.0.1',
      description='basic image feature library',
      long_description=long_description,
      author='Johannes Steger',
      author_email='jss@eyequant.com',
      packages=['bifl', 'bifl.cpy', ],
      package_data={
          'bifl': ['jet.npy', ],
      },
      ext_package='bifl.cpy',
      ext_modules=[
          mkcpy('colorsplit'),
          mkcpy('intdim'),
      ],
      entry_points={
          'console_scripts': [
              'bifl = bifl.run:main',
          ],
      },
      install_requires=['Pillow', ],
      requires=['opencv', ],
      )
