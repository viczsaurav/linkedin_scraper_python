Steps for setup:

One-Time-Setup:
1) Check your Chrome version => Chrome > (three dots) > Help > About Google Chrome
2) Download Chromedriver for matching Chrome version from [following link|https://chromedriver.storage.googleapis.com/index.html]
3) On MacOS => Ctrl+Click > Open webdriver to add an exception to security rules(to be able to launch it)
4) Copy Chrome Webdriver to code folder

Each-time-setup:
1) Export following env variables in terminal:
`LINKEDIN_USER` (user-email)
`LINKEDIN_PASSWORD` (user-password)
`LINKEDIN_ID` (just the id of the person you want to scrape, e.g in URL https://www.linkedin.com/in/adrian0350, export `adrian0350`)

export LINKEDIN_USER=<user-email>
export LINKEDIN_PASSWORD=<password>
export LINKEDIN_ID=<adrian0350> (in URL https://www.linkedin.com/in/adrian0350)

