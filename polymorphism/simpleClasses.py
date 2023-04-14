class Violin:
    def play(self):
        return 'Playing the violin'


class Musician:
    def play(self):
        return 'Musicians are playing'


def start_playing(object):
    return object.play()


violin = Violin()
print(start_playing(violin))

musician = Musician()
print(start_playing(musician))

