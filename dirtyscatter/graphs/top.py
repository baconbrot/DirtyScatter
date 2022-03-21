import logging

import numpy as np
from matplotlib import pyplot as plt
from dirtyscatter.db.orm import User

log = logging.getLogger(__name__)


def generate_plot():
    #plt.style.use('dark_background')
    fig, ax = plt.subplots()
    top_users = User.get_top(10)
    ax.set_ylabel('Scatter')
    plt.xticks(rotation=45)
    for user in top_users:
        ax.bar(user.name, user.scatter, width=0.5)
    plt.savefig("top.png", bbox_inches="tight")
    log.debug(f'Saved top-graph to top.png')
    plt.close(fig)
    return "top.png"
