
def main():
    normal_sedan = CarFactory.make_sedan(200, 200, 'red')
    HD_sedan = HDCarFactory.make_sedan(200, 200, 'red')

    print(normal_sedan.emblem)
    print(HD_sedan.emblem)


class CarFactory:

    @classmethod
    def make_sedan(cls, width: int, height: int, color: str,):
        return cls.Sedan(width, height, color)

    @classmethod
    def make_suv(cls, width: int, height: int, color: str,):
        return cls.SUV(width, height, color)

    class Sedan:

        def __init__(self, width: int, height: int, color: str):
            self.emblem = 'NORMAL'
            self.width = width
            self.height = height
            self.color = color

        def change_color(self, color):
            self.color = color

    class SUV:

        def __init__(self, width: int, height: int, color: str):
            self.emblem = 'NORMAL'
            self.width = width
            self.height = height
            self.color = color

        def change_color(self, color):
            self.color = color


class HDCarFactory(CarFactory):
    class Sedan:
        def __init__(self, width: int, height: int, color: str):
            self.emblem = 'HYUNDAI'
            self.width = width
            self.height = height
            self.color = color

    class SUV:
        def __init__(self, width: int, height: int, color: str):
            self.emblem = 'HYUNDAI'
            self.width = width
            self.height = height
            self.color = color



if __name__ == "__main__":
    main()