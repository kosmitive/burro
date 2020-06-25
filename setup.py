from distutils.core import setup

import numpy as np


setup(name='burro',
      version='0.0.1',
      description='Backpropagation through the void LAX',
      author='Markus Semmler, Thomas Lautenschlaeger',
      author_email='dev@xploras.net',
      install_requires=['numpy', 'matplotlib'],
      packages=['burro' ],
      include_dirs=[np.get_include()],)
