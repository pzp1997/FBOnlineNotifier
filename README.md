# Facebook Online Notifier
## Get notified when your friend goes online on Facebook!

Facebook Online Notifier audibly lets you know when certain friends go online. You can specify which friends you would like to be notified for in the `settings.txt` file (see below).

### About
Facebook Online Notifier is a quick hack I put together in about two hours. I built it to satisfy a personal need. There used to be many apps that served this purpose, but most of them no longer work due to Facebook no longer allowing developers to access certain information (including which friends are online). This script is meant to help fill that void.

### Usage
1. Download a zip of the code.
2. Create a `settings.txt` file (see below for instructions).
3. Run the `main.py` script.
  - Open the command line interface (on Mac, the one installed by default is `Terminal`).
  - Type in `python` ` `
  - Drag the `main.py` file into the window.
  - Press the `<Enter>` (aka `<Return>`) key.

### Creating the `settings.txt` file
The `settings.txt` file is in the format of a JSON string. It consists of the settings that are required for the script to work. These settings are:

- `username` - `str`: Your Facebook username
- `password` - `str`: Your Facebook password
- `special_people` - `str[]` (*optional*): The *Facebook names* of the people you want to be audibly notified about when they go online.

These settings must be serialized as a JSON object and placed in a file named `settings.txt` in the same folder/directory as `main.py`.

### A note on security
It is normally considered bad practice to give your username and password directly to a third-party, as that third-party could potentially steal your information. Facebook Online Notifier needs this information to work properly however, since it cannot use the conventional method of requesting the required information from Facebook (see About). Your username and password are only stored locally on your computer (I *cannot* access them). If you don't believe me, take a look at the source code of the script yourself -- it's around only 50 lines of actual code (or if you're not a programmer, have a friend who is take a look at it). That being said, there is still an inherent risk in storing your password in plaintext on a file on your computer. Please keep this in mind when using this script. I will not be responsible if your account is hacked because of it.

### Technical information
On a technical level, Facebook Online Notifier is essentially a web scraper. It uses `selenium` to open up a Firefox browser window, navigate to Facebook, and sign the user in. Once it has the window open to the "main" Facebook page, it grabs the HTML of the page and parses it using `BeautifulSoup`. It checks which friends are online by using the HTML classes on each friend in the chat sidebar.

This method is *far* from robust. If Facebook changes any one of the three class names that Facebook Online Notifier uses, the script will break. That being said, this is really just a hack that I made for my personal use, and I will be happy with however long this lasts for. If it breaks in a minor way (i.e. Facebook changes the class names), I will probably fix it and update the code here.

### A note on Windows
I am not sure whether or not this script works on Windows, but I have a suspicion that it doesn't. If someone with a Windows machine would like to test it and let me know if my hunch is correct (and if so exactly what isn't working) I would be much obliged.
