"""
.. module:: setup

   :synopsis: This script is used to setup the pip packages.

.. moduleauthor:: Scott W. Fleming <fleming@stsci.edu>
"""

from __future__ import absolute_import
from __future__ import unicode_literals
from setuptools import setup
from spec_plots import __version__

setup(name="spec_plots",
      version=__version__,
      description="Create preview plots of HST spectra.",
      classifiers=["Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3.5"],
      url="https://github.com/openSAIL/spec_plots",
      author="Scott W. Fleming",
      author_email="fleming@stsci.edu",
      license="MIT",
      packages=["spec_plots", "spec_plots.utils", "spec_plots.utils.specutils",
                "spec_plots.utils.specutils_cos",
                "spec_plots.utils.specutils_stis"],
      install_requires=["astropy>=0.4.1", "matplotlib>=1.4.1", "numpy>=1.9.1"],
      entry_points={"console_scripts" :
                    ["make_hst_spec_previews = spec_plots.__main__:main"]},
      zip_safe=False)
