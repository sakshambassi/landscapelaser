from setuptools import find_packages, setup

def install_package():
  """Installs the landscapelaser library
  """
  LONG_DESCRIPTION = "Sharpness value of loss-landscapes"
  setup(
      name='landscapelaser',
      version='0.1.0',
      description=LONG_DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/markdown',
      author='Saksham Bassi',
      license='MIT License',
      packages=find_packages(exclude=['docs', 'tests', 'scripts', 'examples']),
      classifiers=[
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Programming Language :: Python :: 3'
      ],
      keywords=['loss-landscapes', 'sharpness', 'nlp', 'machinelearning'],
      install_requires=[
        'scipy',
        'numpy'
      ]
  )


if __name__ == '__main__':
  install_package()
