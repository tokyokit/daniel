# Daniel
Daniel is a slack bot on Tokyokit.

## Requirements
* Python 2.x
* pip
* GoogleAppEngine SDK
    * https://cloud.google.com/appengine/downloads?hl=ja

## create dev environ

clone from git

   ```
   git clone https://github.com/tokyokit/daniel
   ```

install requirements

   ```
   cd daniel
   cp src/settings.py.sample src/settings.py
   edit src/settings.py
   pip install -r requirements.txt -t lib
   pip install -e . -t lib
   ```

Run this project locally from the command line:

   ```
   dev_appserver.py .
   ```

Visit the application [http://localhost:8080](http://localhost:8080)

## Run pytest
```
python lib/pytest.py tests
```

## Deploy
```
cp app.yaml.sample app.yaml
edit app.yaml
appcfg.py update .
```
