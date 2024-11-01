class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())

#-----------------------------------------------------------------------------------------------------------------------

import logging


logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="utf-8",
                    format="%(levelname)s, | %(message)s")

#-----------------------------------------------------------------------------------------------------------------------

import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner_w = Runner('Name_w', speed=-5)       #создаем объект класса Runner с отрицательной скоростью
            logging.info(f'"test_walk" выполнен успешно')
            for i in range(10):                     #вызываем метод 10 раз
                runner_w.walk()
            self.assertEqual(runner_w.distance, 50)       #сравнение distance с ожидаемым значением
        except:
            logging.warning(f'Неверная скорость для Runner')
            return 0

    def test_run(self):
        try:
            runner_r = Runner(958)                              #передача неверного типа данных
            logging.info(f'"test_run" выполнен успешно')
            for i in range(10):
                runner_r.run()
            self.assertEqual(runner_r.distance, 100)
        except:
            logging.warning(f'Неверный тип данных для объекта Runner')
            return 0



