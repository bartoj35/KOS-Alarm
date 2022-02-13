<h1 align="center"> ⏰ KOS-Alarm ⏰ </h1>

<h4 align="center"> This tiny project was made for purpose of detecting mail that alarming you about school timetable opening. </h4>

## How To Use

To clone and run this project, you will need [Git](https://git-scm.com), [Python](https://www.python.org) and its packages [Imap-tools](https://pypi.org/project/imap-tools/) and [Playsound](https://pypi.org/project/playsound/) 

**Do not forget to fill up your email address etc.**

```bash
# Clone this repository
$ git clone https://github.com/bartoj35/KOS-Alarm

# Go into the reporitory
$ cd KOS-Alarm

# Fill your information in config.py

# Run the app
python3 main.py
```

## Components
**main.py**\
Main part of the project that contains work with mail and alarming about you getting mail today with specified subject.

**config.py**\
Let you configure:
  * **host** of your mail
  * **email**
  * **from** ("noreply@cvut.cz")
  * **password**
  * **sound** for alarm (should be mp3)
  * **subject** of alarming mail ("KOS - Byl jste vpusten do rozvrhu.")

## Credits
Credits for packages for email communication and playing sound belong to:
  * https://github.com/TaylorSMarks
  * https://github.com/ikvk
