def create_press_release(headline, *speech, **stats):
    release = {
        'headline': headline.title(),
        'transcript': "\n".join(speech),
        'data': stats
    }
    return release

