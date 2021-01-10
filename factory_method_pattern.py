"""
Factory Method Pattern
객체 생성을 요청할 때 하위 클래스가 인스턴스화할 클래스를 지정할 수 있게끔 고안된 패턴이다.
자바로 치면 인스페이스를 만드는느낌인듯
"""


def main():
    sonata = HyundaiCar('sonata', 'sedan')

    sonata.start_engine()


class AbstractCar:
    def __init__(self, name: str, car_type: str):
        self.name = name
        self.car_type = car_type

    def start_engine(self):
        raise NotImplementedError


class HyundaiCar:
    def __init__(self, name: str, car_type: str):
        self.name = name
        self.car_type = car_type

    def start_engine(self):
        print(f'{self.name} start!')


if __name__ == "__main__":
    main()
