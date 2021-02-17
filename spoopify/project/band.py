from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        searched_album = [a for a in self.albums if a.name == album_name]
        if not searched_album:
            return f"Album {album_name} is not found."
        if searched_album[0].published:
            return "Album has been published. It cannot be removed."
        self.albums.remove(searched_album[0])
        return f"Album {album_name} has been removed."

    def details(self):
        result = f"Band {self.name}\n"
        for a in self.albums:
            result += a.details()
        return result