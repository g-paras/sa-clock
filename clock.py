from apscheduler.schedulers.blocking import BlockingScheduler
import requests

sched = BlockingScheduler()


@sched.scheduled_job("interval", minutes=15)
def update_server():
    url = "https://sentiment-analysis-web-app.herokuapp.com/"
    res = requests.get(url)


# sched.configure(options_from_ini_file)
sched.start()