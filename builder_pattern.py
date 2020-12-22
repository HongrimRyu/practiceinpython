'''
빌더 패턴
다른 객체를 조합한 복합객체를 생성하기 위해 고안됐다는 점에서 추상 팩터리 패턴과비슷
빌더 패턴은 복합 객체를 구축하는 메서드를 제공할뿐더러 전체 복합 객체 자체의 표현을 보유한다는 점에서 팩터리와 구별된다.
복합객체의 표현을 알고리즘과 별도로 유지해야할때 적합하다
'''
import abc
import datetime


class MemberClassBuilder:

    @abc.abstractmethod
    def set_name(self, new_name: str):
        pass

    @abc.abstractmethod
    def accumulate_credit(self, price: int):
        pass

    @abc.abstractmethod
    def get_discount_rate(self) -> float:
        pass

    @abc.abstractmethod
    def refund(self):
        pass


class GreenMember(MemberClassBuilder):

    def __init__(self,
                 name: str,
                 joined_date: datetime.date,
                 order_count: int,
                 total_amount: int,
                 credit: int
                 ):
        self.name = "[GREEN]" + name
        self.joined_date = joined_date
        self.order_count = order_count
        self.total_amount = total_amount
        self.credit = credit

    def set_name(self, new_name: str):
        self.name = "[GREEN]" + new_name

    def accumulate_credit(self, price: int):
        point = self.order_count * 0.001 * price

        self.credit += point

    def get_discount_rate(self) -> float:
        return 0.05

    def refund(self):
        raise NotImplementedError


class GoldMember(MemberClassBuilder):

    def __init__(self,
                 name: str,
                 joined_date: datetime.date,
                 order_count: int,
                 total_amount: int,
                 credit: int
                 ):
        self.name = "[GOLD]" + name
        self.joined_date = joined_date
        self.order_count = order_count
        self.total_amount = total_amount
        self.credit = credit

    def set_name(self, new_name: str):
        self.name = "[GOLD]" + new_name

    def accumulate_credit(self, price: int):
        point = self.order_count * 0.005 * price

        self.credit += point

    def get_discount_rate(self) -> float:
        return 0.1

    def refund(self):
        raise NotImplementedError


def main():
    mike = GreenMember('mike', datetime.date(2020, 10, 10), 10, 10000, 0)
    john = GoldMember('jhon', datetime.date(2020, 10, 10), 20, 20000, 0)

    print(mike.name)
    print(john.name)

    mike.accumulate_credit(1000)
    john.accumulate_credit(1000)
    print(mike.credit)
    print(john.credit)


if __name__ == "__main__":
    main()
