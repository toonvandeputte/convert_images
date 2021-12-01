This script allows you to convert an entire directory worth of images from one format to another.

To tell the script what to do, you need a `config.py` file, based on the included `config.example.py` file. In this, you can put your source directory, and the conversions that need to happen.

The required packages are listed in `requirements.txt`. The easiest way to run this script is through Python's venv. Install Python 3.9+ from [www.python.org](https://www.python.org) and then do `python3 -m venv .` in a terminal window in the scripts main dir (where this readme file is).

Then, do `source bin/activate` to enter the venv prompt. You can then install the required packages with `pip install -r requirements.txt`.

Then just do `python convert_images.py` to run the script, and you'll see each file being converted one by one. If an output file exists already, it will *not* be overwritten.