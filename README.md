# youtube_comments

**Youtube comments:** is a demo repo for youtube comment web scraping. There are 3 options
- **option one:** using BeautifulSoup and Selenium.
- **option two:** using arsenic.
- **option three:** using scrapy and splash (have not done)

**Set up environment for python and this project on window machine:**
- assumption: os is window 10
- install python for window: https://www.python.org/downloads/
- check python version and pip version with command: python --version, pip --version
- install virtualenv: python -m pip install --user virtualenv
- install git for window: https://git-scm.com/download/win. use git bash for command line from now on.
- install wsl: https://docs.microsoft.com/en-us/windows/wsl/install (if possible)
- install docker for window: https://docs.docker.com/desktop/windows/install/ (if possible)
- clone this project from remote repo to you computer: git clone https://gitlab.apdigit.tech/toanbui1991/youtube_comments.git
- create virtual environment: python -m venv venv
- activate virtual environment with bash command: source venv/Scripts/activate
- check is pytho call from virtual environment: where python
- install all dependencies: pip install -r requirements.txt
- for more detail about package and virtual environment reference to this link: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

**run demo script on window:**
- python youtube.py. to run option 1 demo for one youtube link.
- python youtube_v2.py. to run option 1 demo
- python youtube_async.py. to run option 2 demo
- python youtube_async_v2.py. to run option 2 demo with Task Object.


**Set up environment for python and this project on mac machine:**
- assumption: os is macos
- install python for mac: https://www.python.org/downloads/macos/
- check python version and pip version with command: python3 --version, pip --version
- install virtualenv: python3 -m pip install --user virtualenv
- install git for mac: https://git-scm.com/download/mac. use git bash for command line from now on.
- install VirtualBox on mac: https://www.virtualbox.org/manual/ch02.html (if possible)
- install docker for mac: https://docs.docker.com/desktop/mac/install/ (if possible)
- clone this project from remote repo to you computer: git clone https://gitlab.apdigit.tech/toanbui1991/youtube_comments.git
- create virtual envinronment: python3 -m venv venv
- activate virtual environment with bash command: source venv/bin/activate
- check is pytho call from virtual environment: where python3
- install all dependencies: pip install -r requirements.txt
- for more detail about package and virtual environment reference to this link: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/



**run demo script on mac:**
- python3 youtube.py. to run option 1 demo for one youtube link.
- python3 youtube_v2.py. to run option 1 demo
- python3 youtube_async.py. to run option 2 demo
- python3 youtube_async_v2.py. to run option 2 demo with Task Object.
