from instapy import InstaPy
from instapy import smart_run
session = InstaPy(username="tawhidshaikhpvt", password="", headless_browser=False)
with smart_run(session):
    #session.follow_by_list(followlist=['muftimenkofficial', 'iamomarsuleiman'], times=1, sleep_delay=10, interact=False)
    session.unfollow_users(amount=2, allFollowing=True, sleep_delay=10)
    session.end()