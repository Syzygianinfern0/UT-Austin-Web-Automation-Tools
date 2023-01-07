# UT-Austin-Web-Automation-Tools

It is NOT trivial to perform any webscraping/automation on UT Direct websites since there is a Duo 2FA login system.
This is a workaround to automate the login process. This is done by just saving chrome local storage and cookies to a
local folder and then using that to login to the website in further attempts.

## Setup

1. Install selenium and chromedriver.
2. Rename [`sample_config.json`](/sample_config.json) to `config.json` and fill in the details.
3. Then you need to run the [`generate_dump.py`](/generate_dump.py) file. This will open a Chrome window and ask you to
   login to the website and authenticate yourself. Make sure you select the "remember this browser" option in the
   window. (you can also use [`manual_setup.py`](/manual_setup.py) to do the same thing, but you gotta write the loading
   script yourself)

## Scripts

This repo houses a neat little collection of scripts to perform various tasks. Currently implements

### [`Waitlist Checker`](/check_course_availability.py)

Checking if course has been moved from waitlist to open. This is important if you cannot add yourself to the waitlist
since there is another class with a clashing timeslot (am I wrong to think so?).

## Misc Note

This codebase was entirely created using ChatGPT and GitHub copilot (I'm not kidding). It was a fun experiment to see
how far I could get with these tools. I'm not sure if I would recommend using these tools for serious projects, but it
was a fun experiment (even the last sentence was recommended by copilot lmao 😄🔫).