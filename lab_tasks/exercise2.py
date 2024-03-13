import random

class MusicLibrary:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added '{song}' to the music library.")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed '{song}' from the music library.")
        else:
            print(f"'{song}' is not in the music library.")

    def play_random_song(self):
        if self.songs:
            random_song = random.choice(self.songs)
            print(f"Playing random song: '{random_song}'")
        else:
            print("No songs in the music library.")

# Example usage:
music_library = MusicLibrary()

# Adding songs
music_library.add_song("Song 1")
music_library.add_song("Song 2")
music_library.add_song("Song 3")

# Playing a random song
music_library.play_random_song()

# Removing a song
music_library.remove_song("Song 2")

# Playing a random song after removal
music_library.play_random_song()
