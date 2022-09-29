from setuptools import setup, find_packages

VERSION = '0.3.4'

setup(
  name="mkdocs-candy",
  version=VERSION,
  url='https://github.com/usecandy/candy-mkdocs-theme',
  license='Proprietary',
  description='Elegant theme for MkDocs',
  author='usecandy',
  author_email='mkdocs@usecandy.com',
  packages=find_packages(),
  include_package_data=True,
  entry_points={
    'mkdocs.themes': [
      'candy = candy_theme',
    ]
  },
  zip_safe=False
)
