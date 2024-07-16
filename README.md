## Pre run

The script uses selenium headless browser as the fetched site relies on JS to load content, the easiest way to move forward is to install it using pip3.

```sh
pip3 install selenium 
pip3 install webdriver_manager
```

The script will run Chrome in headless mode, navigate to the URL, and print the source of the page.
Note: If chrome is not already installed
you will need to install it using the below commands 

### Mac
```sh
brew install --cask google-chrome
```

### Linux

```sh
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

### Windows

Unfortunately you will need to install it from chrome website

## Run

to run the script
```sh
python3 fetch_url.py
```
or
```sh
python fetch_url.py
```
based on your env configurations.



