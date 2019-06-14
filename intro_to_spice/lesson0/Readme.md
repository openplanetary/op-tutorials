# __OpenPlanetary__ - Intro to __SPICE__

### Lesson 0 : Intro & Setup

In this video I first cover the aims of this _Intro to SPICE_ series, before attempting to give the world's shortest explanation of what exactly __SPICE__ is. I finish up by walking you through how to setup __SPICEYPY__ on your own system, so you can jump straight into next lesson's coding challenges!

#### Install Steps
1. Ensure that Python3 is installed (see link below)
2. Open Terminal/Command Prompt, and navigate to the *intro_to_spice* directory.
3. Create a virtual env by running the following code :

  `python3 -m venv venv`

4. Load your virtual env using this command :

  `source venv/bin/activate`

  You should see _(venv)_ at the start of the next line in your console.

5. Install the required modules :

  `pip3 install spiceypy jupyter matplotlib`

6. We're going to test the install by running an example Jupyter notebook. Run the following code to open the Jupyter browser :

  `jupyter notebook`

7. Navigate into the _lesson0_ directory, and click the *Lesson0_Intro_Setup.ipynb* notebook to load it.

8. If you see the current __SPICE__ API build number at the bottom of the notebook, your modules have installed correctly. If not, check the notebook for any error messages, and try again.


#### Jupyter Notebook
A Jupyter Notebook for this lesson is available, which can be used to test that your python environment is setup correctly.

#### Requirements
* Python3 (https://www.python.org/downloads/)

#### Further Reading
* SPICE - https://naif.jpl.nasa.gov/naif/index.html
* SPICEPY - https://spiceypy.readthedocs.io/en/master/
* OpenPlanetary - http://openplanetary.org/

#### OpenPlanetary Forum
Feel free to ask any questions you may have about these videos in the dedicated section over on the OpenPlanetary Forum : https://forum.openplanetary.org
