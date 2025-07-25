#My name is Jacob Baker and this is Chapter 14 Lab 2 which is being done on July 12 and being revised on July 24
from dataclasses import dataclass
@dataclass

class Computer:
    def __init__(self, cpu_speed, ram_size, drive_size):
        self.__cpu_speed = cpu_speed
        self.__ram_size = ram_size
        self.__drive_size = drive_size

    @property
    def cpu_speed(self):
        return self.__cpu_speed

    @cpu_speed.setter
    def cpu_speed(self, value):
        self.__cpu_speed = value

    @property
    def ram_size(self):
        return self.__ram_size

    @ram_size.setter
    def ram_size(self, value):
        self.__ram_size = value

    @property
    def drive_size(self):
        return self.__drive_size

    @drive_size.setter
    def drive_size(self, value):
        self.__drive_size = value