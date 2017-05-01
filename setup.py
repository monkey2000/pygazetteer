from setuptools import setup

setup(name='pygazetteer',
      version='0.1.0',
      description='Location extractor by looking up gazetteer',
      url='https://github.com/monkey2000/pygazetteer',
      license='MIT',
      packages=['pygazetteer'],
      install_requires=[
          'pyahocorasick'
      ],
      zip_safe=False,
      include_package_data=True)

