from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name: str = name
        self.albums: list = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."
    
    def find_album_by_name(self, name):
        obj = [a for a in self.albums if a.name == name]
        if obj: 
            return obj[0]
    
    def remove_album(self, album_name: str):
        if not self.find_album_by_name(album_name):
            return f"Album {album_name} is not found."
        if self.find_album_by_name(album_name).published:
            return f"Album has been published. It cannot be removed."
        self.albums.remove(self.find_album_by_name(album_name))
        return f"Album {album_name} has been removed."
    
    def details(self):
        res = f"Band {self.name}\n"
        for a in self.albums:
            res += a.details()
        return res