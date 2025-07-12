#My name is Jacob Baker and this is Chapter 14 Lab 2 which is being done on July 12
class Computer:

    def __init__(self,cpu_speed,ram_size,drive_size):
        self.cpu_speed = cpu_speed
        self.ram_size = ram_size
        self.drive_size = drive_size

    def __str__(self):
        return f'Computer(_Computer__cpu_speed={self.cpu_speed}, _Computer__ram_size={self.ram_size}, _Computer__drive_size={self.drive_size})'