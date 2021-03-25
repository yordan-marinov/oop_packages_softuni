from project.song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name: str = name
        self.songs: [Song] = list(songs)
        self.published = False

    def add_song(self, song: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        
        if song in self.songs:
            return "Song is already in the album."
        
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."
    
    def song_in_album(self, name):
        obj = [s for s in self.songs if s.name == name]
        if obj:
            return obj[0]
    
    def remove_song(self, song_name: str):
        if self.published:
            return f"Cannot remove songs. Album is published."
        if not self.song_in_album(song_name):
            return "Song is not in the album."
        self.songs.remove(self.song_in_album(song_name))
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."
    
    def details(self):
        res = f"Album {self.name}\n"
        for s in self.songs:
            res += f"== {s.get_info()}\n"
        return res