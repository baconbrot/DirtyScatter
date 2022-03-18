from matplotlib import pyplot as plt
from time import time
import matplotlib.dates as md
from dirtyscatter.db.orm import History
import datetime as dt

plt.xticks(rotation=25)
def generate_plot():
    #plt.style.use('dark_background')
    fig, ax = plt.subplots()
    begin = time()-30*24*3600
    histories = History.get_after_timestamp(begin)
    users = {}
    for history in histories:
        try:
            users[history.name] = users[history.name]+[history]
        except:
            users[history.name] = [history]
    for user in users.keys():
        user_histories = users[user]
        x = [dt.datetime.fromtimestamp(history.timestamp) for history in user_histories]
        y = [history.scatter for history in user_histories]
        ax.step(x, y, where='post', label=f'{user}')
    xfmt = md.DateFormatter('%d.%m')
    ax.set_ylabel('Scatter')
    ax.xaxis.set_major_formatter(xfmt)
    ax.legend(fontsize=7, labelspacing=0.15, bbox_to_anchor=(1, 1), ncol=2)
    plt.savefig("output.png", bbox_inches="tight")
