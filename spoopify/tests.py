import unittest

from project.song import Song
from project.album import Album
from project.band import Band


class TestProject(unittest.TestCase):
    def setUp(self):
        self.s = Song("Hello", 1.11, False)
        self.a = Album("My name", self.s)
        self.b = Band("band_name")

    def test_song_initcializations(self):
        self.assertEqual("Hello", self.s.name)
        self.assertEqual(1.11, self.s.lenght)
        self.assertEqual(False, self.s.single)

    def test_song_get_info(self):
        self.assertEqual("Hello - 1.11", self.s.get_info())

    def test_album_init(self):
        self.assertEqual("My name", self.a.name)
        self.assertEqual([self.s], self.a.songs)
        self.assertEqual(False, self.a.published)

    def test_add_song_and_is_in_album(self):
        self.assertEqual("Song is already in the album.", self.a.add_song(self.s))

    def test_add_song_if_album_is_published(self):
        self.a.published = True
        self.assertEqual(
            "Cannot add songs. Album is published.", self.a.add_song(self.s)
        )

    def test_song_is_single(self):
        self.s.single = True
        self.assertEqual(
            f"Cannot add {self.s.name}. It's a single", self.a.add_song(self.s)
        )

    def test_add_song_to_album(self):
        self.a.songs = []
        self.assertEqual(
            f"Song {self.s.name} has been added to the album {self.a.name}.",
            self.a.add_song(self.s),
        )

    def test_remove_song_if_album_is_published(self):
        self.a.published = True
        self.assertEqual(
            "Cannot remove songs. Album is published.", self.a.remove_song(self.s)
        )

    def test_remove_song_if_song_not_in_album(self):
        self.a.songs = []
        self.assertEqual("Song is not in the album.", self.a.remove_song(self.s))

    def test_remove_song_from_list(self):
        self.assertEqual(
            "Removed song Hello from album My name.", self.a.remove_song("Hello")
        )
        self.assertEqual([], self.a.songs)

    def test_album_publish_is_already_published(self):
        self.a.published = True
        self.assertEqual("Album My name is already published.", self.a.publish())

    def test_album_publush_if_not_published(self):
        self.assertEqual("Album My name has been published.", self.a.publish())

    def test_band_init(self):
        self.assertEqual("band_name", self.b.name)
        self.assertEqual([], self.b.albums)

    def test_band_add_album_if_not_in_albums(self):
        self.assertEqual(
            "Band band_name has added their newest album My name.",
            self.b.add_album(self.a),
        )

    def test_band_add_album_if_album_in_albums(self):
        self.b.add_album(self.a)
        self.assertEqual(
            "Band band_name already has My name in their library.",
            self.b.add_album(self.a),
        )

    def test_remove_album_from_band_albums_if_not_in(self):
        self.assertEqual(
            "Album My name is not found.", self.b.remove_album(self.a.name)
        )

    def test_remove_album_from_band_albums_if_published(self):
        self.a.published = True
        self.b.add_album(self.a)
        self.assertEqual(
            "Album has been published. It cannot be removed.",
            self.b.remove_album(self.a.name),
        )

    def test_remove_album_from_band_albums_success(self):
        self.b.add_album(self.a)
        self.assertEqual(
            "Album My name has been removed.", self.b.remove_album(self.a.name)
        )


if __name__ == "__main__":
    unittest.main()
    # s = Song("Hello", 1.11, False)
    # print(s.get_info())
    # a = Album("My name", s)
    # print(a.details())
    # song = Song("Running in the 90s", 3.45, False)
    # print(song.get_info())
    # album = Album("Initial D", song)
    # second_song = Song("Around the World", 2.34, False)
    # print(album.add_song(second_song))
    # print(album.details())
    # print(album.publish())
    # band = Band("Manuel")
    # print(band.add_album(album))
    # print(band.remove_album("Initial D"))
    # print(band.details())