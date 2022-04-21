import logging
import math

import numpy as np
from matplotlib import pyplot as plt
from time import time
import matplotlib.dates as md
from dirtyscatter.db.orm import User, History
import datetime as dt

plt.xticks(rotation=25)
log = logging.getLogger(__name__)

def generate_plot():
    #plt.style.use('dark_background')
    fig, ax = plt.subplots()
    begin = int(time()) - 30 * 24 * 3600
    histories = History.get_after_timestamp(begin)
    user_histories = {}
    # Group by username
    for user_history in histories:
        try:
            user_histories[user_history.name] = user_histories[user_history.name]+[user_history]
        except KeyError:
            user_histories[user_history.name] = [user_history]
    # Add user graph to plot
    for user in user_histories.keys():
        user_history = user_histories[user]
        user_history.append(History.History(name=user, scatter=user_history[-1].scatter, timestamp=int(time())))
        x = [dt.datetime.fromtimestamp(history.timestamp) for history in user_history]
        y = [history.scatter for history in user_history]
        ax.step(x, y, where='post', label=f'{user}')
    xfmt = md.DateFormatter('%d.%m')
    ax.set_ylabel('Scatter')
    ax.xaxis.set_major_formatter(xfmt)
    ax.legend(fontsize=7, labelspacing=0.15, bbox_to_anchor=(1, 1), ncol=2)
    plt.savefig("output.png", bbox_inches="tight", edgecolor='none')
    log.debug(f'Saved leadboard-graph to output.png')
    plt.close(fig)
    return "output.png"
