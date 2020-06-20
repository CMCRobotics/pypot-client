from setuptools import setup, find_packages

setup(
      install_requires=['distribute'],
      optional_requires=['aiohttp[speedups]>=3.6.2', 'requests>=2.16.0'],
      extras_require={
         'test':['testfixtures']
      },
      name = '${PROJECT_NAME}',
      python_requires= '>=3.4.0',
      author = 'Brice Copy',
      url = 'https://github.com/cmcrobotics/pypot-client',
      keywords = ['pypot','poppy','robotics'],
      version = '${VERSION}',
      packages =  find_packages('.')
)
