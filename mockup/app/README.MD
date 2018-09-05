# PitchUp Mockup

A mockup for PitchUp by Bingoogol.

## First time preparation

Preferably use a virtual environment. A common way to create one from the command line is...

```
virtualenv .venv -p /usr/bin/python3
```

Where `/usr/bin/python3` is a path to your python 3 install.

Start your virtual environment...

```
source .venv/bin/activate
```

Then, install dependencies, from the `app` directory...

```
pip install -r requirements.txt
```

## To Run

From the command line and inside the `app` directory...

```
python run.py
```


## Adding a route / template

Check out https://bottlepy.org/docs/dev/tutorial.html , Bottle is super easy to use.

So...
- The views are in the `views` folder.
- The `base.tpl` file is the base html wrapper that houses the `<head>`, any CSS/JS includes, and the top bar/side nav. Anything you write in another template will appear at {{ !base }}
- Create a new view like `example.tpl` in the views folder, and add `% rebase('base.tpl', title='My Cool title')` to the top.
- Add in any html as you normally would.
- Add a route to run.py, based on the current routes there.  If you want to pass in data, simply pass it with an argument name of your choosing. Might want to reference Bottle docs for 30 seconds if you want to do this, but we probably don't need it.
