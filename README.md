# reddit-meetup-data
Repo for tools to fetch the r/Charlotte Reddit meetup data

Followed this guide to get started - https://www.geeksforgeeks.org/scraping-reddit-using-python/

https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/


# Create the venv
```
python -m venv .venv
```

# Use the venv
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned

.\.venv\Scripts\activate

pip install -r requirements.txt
```

# Tips
To get the latest variables provided by the redit API
```
import pprint
pprint.pprint(vars(submission/comment))
```