import random
class reinforcement():
    def __init__(self):
        self.strength = random.randrange(6, 9)
        self.int = random.randrange(6, 9)

    def naming(self):
        self.name = input("캐릭터의 이름을 입력하세요: ")
        print("캐릭터 이름: {}".format(self.name))

    def information(self):
        print("캐릭터 정보: 힘({}), 지력({})".format(self.strength, self.int))
        if self.strength > self.int:
            print("캐릭터 직업: 전사")
        elif self.strength < self.int:
            print("캐릭터 직업: 법사")
        elif self.strength == self.int:
            print("캐릭터 직업: 궁수")

if __name__ == '__main__':
    while 1:
        a=input()
        a=reinforcement()
        a.naming()
        a.information()
