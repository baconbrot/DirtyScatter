import math

import numpy as np
from matplotlib import pyplot as plt
from time import time
import matplotlib.dates as md
from dirtyscatter.db.orm import User, History
import datetime as dt

plt.xticks(rotation=25)

def generate_plot():
    #plt.style.use('dark_background')
    fig, ax = plt.subplots()
    try:
        oldest = History.get_oldest()[0]
        begin = max(int(time()) - 30 * 24 * 3600, oldest.timestamp)
    except:
        begin = int(time())
    histories = History.get_after_timestamp(begin)
    user_histories = {}
    for history in histories:
        try:
            user_histories[history.name] = user_histories[history.name]+[history]
        except:
            user_histories[history.name] = [history]
    if len(user_histories.keys()) == 0:
        top_users = User.get_top(10)
        for user in top_users:
            user_histories[user.name] = [History.History(name=user.name, scatter=user.scatter, timestamp=int(time())-1000),
                                         History.History(name=user.name, scatter=user.scatter, timestamp=int(time()))]
    for user in user_histories.keys():
        user_history = user_histories[user]
        x = [dt.datetime.fromtimestamp(history.timestamp) for history in user_history]
        y = [history.scatter for history in user_history]
        ax.step(x, y, where='post', label=f'{user}')
    xfmt = md.DateFormatter('%d.%m')
    ax.set_ylabel('Scatter')
    ax.xaxis.set_major_formatter(xfmt)
    ax.legend(fontsize=7, labelspacing=0.15, bbox_to_anchor=(1, 1), ncol=2)
    plt.savefig("output.png", bbox_inches="tight")
    plt.close(fig)
    return "output.png"
