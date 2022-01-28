# Herdir, Written in Python; Setup

## Environment

If using Git Bash terminal, run `source herdir/Scripts/activate` while in the `newworld/Herdir_Python/environments` directory.

If you're using Windows terminals, run `herdir\Scripts\activate.bat`.

For both of these, `herdir` is the name of your virtual environment that you've created with `py -m venv <name of virtual environment>`.

## pip Installation

Follow the article [here](https://pip.pypa.io/en/stable/installation/).

Once pip is installed, now we can `pip install` our libraries.

```py
python -m pip install python-dotenv --user
python -m pip install discord.py --user
```

## APIs Available on Discord

[Documentation here.](https://discordpy.readthedocs.io/en/latest/api.html#)