class MusicIterator:
    def __init__(self, songs):
        self.songs = songs
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.songs):
            song = self.songs[self.index]
            self.index += 1
            return song

        raise StopIteration

    def next_song(self):
        if self.index < len(self.songs):
            return self.songs[self.index]

        return "Следующей песни нет"


class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __iter__(self):
        return MusicIterator(self.songs)


playlist = Playlist()

playlist.add_song("Космополитен-gradient")
playlist.add_song("Время-gradient")
playlist.add_song("two-bbno$")

iterator = iter(playlist)

print("Текущая песня:", next(iterator))
print("Следующая песня:", iterator.next_song())
