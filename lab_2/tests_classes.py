import unittest

from classes import *


class TestGameObjects(unittest.TestCase):

    def test_game_object(self):
        player = GameObject(
            123,
            "Player Name",
            201,
            303,
        )
        self.assertEqual(player.getId(), 123)
        self.assertEqual(player.GetName(), "Player Name")
        self.assertEqual(player.getX(), 201)
        self.assertEqual(player.getY(), 303)

    def test_unit(self):

        igrok = Unit(
            123,
            "Player Name",
            201,
            303,
            True,
            1000,
        )
        self.assertEqual(igrok.getId(), 123)
        self.assertEqual(igrok.GetName(), "Player Name")
        self.assertEqual(igrok.getX(), 201)
        self.assertEqual(igrok.getY(), 303)

        self.assertTrue(igrok.isAlive())
        self.assertEqual(igrok.getHP(), 1000)

        igrok.receiveDamage(500)
        self.assertEqual(igrok.getHP(), 500)

        igrok.receiveDamage(600)
        self.assertFalse(igrok.isAlive())

    def test_building(self):

        user = Building(
            123,
            "Player Name",
            201,
            303,
            100
        )
        self.assertEqual(user.getId(), 123)
        self.assertEqual(user.GetName(), "Player Name")
        self.assertEqual(user.getX(), 201)
        self.assertEqual(user.getY(), 303)

        self.assertTrue(user.isBuild())
        


class ArcherWithMethods(Archer):
    """
    Тестовый класс, который нужен, чтобы проверить работу наследования и интерфейсов
    """
    def attack(self, unit: Unit):
        """
        переопределяем, чтобы сработало наследование
        """
        pass

    def move(self):
        pass



class TestInterfaces(unittest.TestCase):
    def test_archer(self):
        arch = Archer(
            101,
            "Test archer",
            4,
            5,
            True,
            200.1,
        )


if __name__ == '__main__':
    unittest.main()
