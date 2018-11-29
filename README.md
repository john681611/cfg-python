1. Copy `Procfile`and change `flask-learn.py` to your file
1. Copy runtime.text and requirements.text
1. in terminal `cd` to your app
  1. In terminal `heroku create
  1. `git push heroku master` (use this to update the app)
  1. `heroku open
1. Make sure app run in your file is like this: 
```py
from os import environ
app.run(host='0.0.0.0',debug=True, port=environ.get("PORT", 5000))
```
 (so it can take the port it needs) 
1. DONE!!!!