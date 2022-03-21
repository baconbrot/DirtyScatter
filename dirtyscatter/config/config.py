import getopt
import sys
import toml


try:
    opts, args = getopt.getopt(sys.argv[1:], 'c:')
    if (len(opts) == 0):
        raise Exception()
    for opt, arg in opts:
        if opt == '-c':
            config_path = arg
        else:
            raise Exception()
except:
    config_path = 'config.toml'
config = toml.load(config_path)


def get_leaderboard_url():
    global config
    url = config.get('scraper').get('leaderboard_url')
    return url


def get_table_body_x():
    global config
    table_body_x = config.get('scraper').get('table_body_x')
    return table_body_x


def get_next_page_btn_x():
    global config
    table_body_x = config.get('scraper').get('next_page_btn_x')
    return table_body_x


def get_total_display_count_x():
    global config
    table_body_x = config.get('scraper').get('total_display_count_x')
    return table_body_x


def get_fetch_interval():
    global config
    fetch_interval = config.get('general').get('fetch_interval')
    return fetch_interval


def get_token():
    token = config.get('discord').get('token')
    return token


def get_command_prefix():
    global config
    prefix = config.get('discord').get('command_prefix')
    return prefix


def get_channel_id():
    global config
    channel_id = config.get('discord').get('channel')
    return channel_id


def get_chromedriver_path():
    global config
    path = config.get('chrome').get('driver_path')
    return path


def get_loading_time():
    global config
    lt = config.get('chrome').get('loading_time')
    return lt


def get_interaction_time():
    global config
    it = config.get('chrome').get('interaction_time')
    return it


def get_use_virtual_display():
    global config
    yes = config.get('chrome').get('use_virtual_display')
    return yes

