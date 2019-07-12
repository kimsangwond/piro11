#######################################################################
# 개복치의 아류작! 과연 나무를 끝까지 키워낼 수 있을 것인가??
###나무 요소
# 키, 두께 이름
##나무 속성
# 물 저항력, 가분수 저항력, 잡초 허용치.
###나무 키운데 영향을 주는 것
# (토양양분상태: 수분 영양)
# 주변 잡초상황
# 가지/키 : 가분수로 사망
# 계절;봄 여름 가을 겨울
#
#
###나무의 성장을 어떻게=잡초의 성장은 어떻게
#
#
#
###구현하고 싶은 버튼
# 잡초 속아내기: (버튼 누르면 잡초 속아내기도 가능하게 하기)(너무 없을 경우 외로워서 사망)(너무 많으면 영양 뺐겨서 사망)
# 물주기(강수량*계절패널티+물주기로 수분량 측정하고 수분 저항력에 대해 사망 함수 만들기)
# 비료주기(기분 좋으라고)(굵기의 성장 촉진)(나무 굵기과 태풍 견디기 강도를 함수로 구현)
###사망 요소
# 가분수 사망(두께가 길이에 비해 비율이 너무 클경우 사망시켜)
# 잡초 친구 사망(외로워 사망(나무 하나만 키웠자너))(
# 자연재해 사망:( 1요소: 햇살이 너무 강해서 사망  ,비가 너무 많이와서 사망 2요소: 폭풍으로 인한 사망)
# 랜덤의 확률로 (잡아먹혀 사망,공사구역지정
#
#
########################################################################



import random


class tree:
    def __init__(self):
        self.weed = random.randrange(20, 40)
        status = ["봄", "여름", "가을", "겨울"]
        self.weather_count = 0
        self.width = random.randrange(6, 9)
        self.height = random.randrange(6, 9)
        self.weather = status[self.weather_count % 4]
        self.menu = None
        self.menu_1 = 0
        self.menu_2 = 0
        self.max_risk = 1
        self.risk = 0
        self.fractions_risk = 0
        self.fractions = self.width // self.height  # 나무의 가분수  결정
        self.weed_risk = 0
        self.weather_risk = 0
        self.main_risk = None

    def naming(self):
        self.name = input("나무의 이름을 입력하세요: ")
        print("나무 이름: {}".format(self.name))

    def tree_output(self):
        print("나무이름 : {0}".format(self.name))
        print("두께: {0}".format(self.width))
        print("높이: {0}".format(self.height))
        print("잡초: {0}".format(self.weed))

    def calculator_risk(self):
        if self.fractions > 3:
            self.fractions_risk = 20
        else:
            self.fractions_risk = 0

        if (self.weed < 3) or (self.weed > 80):
            self.weed_risk = 80
        else:
            self.weed_risk = 0

        if self.weather_count % 4 == 0:  # 봄일때
            self.weather_risk = 20
            print("봄에는 새가 나무를 쪼아대서 나무가 아파합니다")
        elif self.weather_count % 4 == 1:  # 여름일때
            self.weather_risk = 40
            print("여름엔 비가 너무 와서 나무가 괴로워합니다")
        elif self.weather_count % 4 == 2:  # 가을일때
            self.weather_risk = 20
            print("가을엔 나무가 가을을 타서 외로워합니다")
        elif self.weather_count % 4 == 3:  # 겨울일때
            self.weather_risk = 50
            print("겨울엔 추워서 나무가 추워서 덜덜 떨어요")
        self.death()


    def death(self):
        if 80 < (self.weather_risk + self.fractions_risk + self.weed_risk):
            risk = [self.weather_risk, self.fractions_risk, self.weed_risk]

            if max(risk) == self.weather_risk:
                self.main_risk = '날씨'
                print("날씨로 인해 죽음!")
                exit()

            elif max(risk) == self.weed_risk:
                self.main_risk = '잡초'
                if self.weed < 3:
                    print('나무가 고독사하였습니다')
                elif self.weed > 80:
                    print('나무가 잡초로 인해 사망하였습니다.')
                else:
                    pass
                exit()

            elif max(risk) == self.fractions_risk:
                self.main_risk = '가분수'
                print('가분수로 인해')
                exit()

            else:
                pass

        else:
            print('나무가 견딤')

    def menu_select(self):
        print("\n****************농부의 일상**************\n")
        print("\n****************이미지**************\n")
        print('''
               #
              ###
            #######
          ###########
             #####
          ##########
        ###############
              ##''')
        for i in range(self.height):
            print('              ##')

        print("\n*****************************************\n")
        print("         사랑스러운 우리 %s!" % (self.name))
        print("\n*****************************************\n")
        print("1. 물 주기")
        print("2. 비료 주기")
        print("3. 잡초 골라내기")
        print("4. skip")
        print("\n*****************************************\n")
        self.menu = input("할 일을 입력하세요: ")
        print("\n");

        if self.menu == '1':
            self.menu_1 = int(random.randrange(1, 11))
            if (int(self.menu_1) >= 1) and (int(self.menu_1) <= 9):
                self.height *= int(random.randrange(1, 6))
                print('높이가 증가하였습니다')
            else:
                self.width += int(random.randrange(1, 6))
                print('두께가 증가하였습니다')
            self.weed = self.weed * (100 + random.randrange(30)) // 100
            print("\n")
            print(self.tree_output())
            self.calculator_risk()

            self.weather_count += 1


        elif self.menu == '2':
            self.menu_2 = int(random.randrange(1, 11))
            if (self.menu_2 >= 1) and (self.menu_2 <= 9):
                self.width += int(random.randrange(1, 6))
                print('확률로 두께가 증가하였습니다')
            else:
                self.height += int(random.randrange(1, 6))
                print('확률로 높이가 증가하였습니다')
            self.weed = self.weed * (100 + random.randrange(50)) // 100
            print("\n")
            print(self.tree_output())
            self.calculator_risk()
            self.weather_count += 1

        elif self.menu == '3':
            self.weed = self.weed * random.randrange(100) // 100
            print("잡초를 솎아냈습니다! 잡초 상황: %d " % (self.weed))

            self.calculator_risk()
            self.weather_count += 1
        else:
            print('단계를 스킵하였습니다.')
            self.calculator_risk()
            self.weather_count += 1


if __name__ == '__main__':
    a = input()
    a = tree()
    a.naming()
    while 1:
        a.menu_select()