# sa-clock

I have certain applications running on heroku, but there is a problem with them.
Heroku has a time limit for application, if the app is not used for a certain time then it will stop the process.
This leads to the increase in the loading time of the app.

To deal with this problem I wrote a python script that will keep the server running by making request to the app every 15 minutes.
