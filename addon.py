from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()

URL1 = "http://feeds.feedburner.com/CanaryPod"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://pbs.twimg.com/profile_images/1143486362961817601/x9enQ_0Z_400x400.png"},
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://pbs.twimg.com/profile_images/1143486362961817601/x9enQ_0Z_400x400.png"},
    ]

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items


@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast = mainaddon.get_playable_podcast(soup)
    
    items = mainaddon.compile_playable_podcast(playable_podcast)

    return items


if __name__ == '__main__':
    plugin.run()
