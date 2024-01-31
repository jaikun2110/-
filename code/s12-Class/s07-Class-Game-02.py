# 9.2 
# 클래스와 객체 생성하기

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name # 인스턴스 변수 name에 전달값 name 저장
        self.hp = hp # 인스턴스 변수 hp에 전달값 hp 저장
        self.damage = damage # 인스턴스 변수 damage에 전달값 damage 저장
        print("{0} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

soldier1 = Unit("보병", 40, 5) # 보병1 생성, 전달값으로 이름/체력/공격력 전달
soldier2 = Unit("보병", 40, 5) # 보병2 생성, 전달값으로 이름/체력/공격력 전달
tank = Unit("탱크", 150, 35) # 탱크 생성, 전달값으로 이름/체력/공격력 전달

#%%
#9.2.1
class Unit:
    def __init__(self, name, hp, damage): # 생성자, self 외 전달값 3개
        self.name = name 
        self.hp = hp 
        self.damage = damage
        print("{0} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

soldier1 = Unit("보병", 40, 5) # 객체 생성
soldier2 = Unit("보병", 40, 5) # 객체 생성
tank = Unit("탱크", 150, 35) # 객체 생성
#soldier3 = Unit("보병") # 전달값 3개 중 1개만 넘김, TypeError 발생
#soldier3 = Unit("보병", 40) # 전달값 3개 중 2개만 넘김, TypeError 발생

#%%

#9.2.2
class Unit:
    def __init__(self, name, hp, damage): # 생성자, 전달값 3개
        self.name = name # 인스턴스 변수 name
        self.hp = hp # 인스턴스 변수 hp
        self.damage = damage # 인스턴스 변수 damage
        print("{0} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 전투기: 공중 유닛, 은폐 불가
stealth1 = Unit("전투기", 80, 5) # 객체 생성, 체력 80, 공격력 5
print("유닛 이름 : {0}, 공격력 : {1}".format(stealth1.name, stealth1.damage)) # 인스턴스 변수 접근

#%%

# 은폐 가능
stealth2 = Unit("업그레이드한 전투기", 80, 5)
stealth2.cloaking = True # 업그레이드한 전투기만을 위한 특별한 인스턴스 변수 정의, 은폐 상태

if stealth2.cloaking == True: # 은폐 상태라면
    print("{0}는 현재 은폐 상태입니다.".format(stealth2.name))

# 오류 발생
# if stealth1.cloaking == True: # 다른 전투기의 은폐 여부
#    print("{0}는 현재 은폐 상태입니다.".format(stealth1.name)) 

#%%
#9.2.3
class AttackUnit: # 공격 유닛
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location): # 전달받은 방향으로 공격
        print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage)) # 공간이 좁아서 2줄로 나눔

    def damaged(self, damage): # damage만큼 유닛 피해
        # 피해 정보 출력
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage # 유닛의 체력에서 전달받은 damage만큼 감소
        # 남은 체력 출력
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0: # 남은 체력이 0 이하이면
            print("{0} : 파괴됐습니다.".format(self.name)) # 유닛 파괴 처리

# 화염방사병: 공격 유닛, 화염방사기를 사용함
flamethrower1 = AttackUnit("화염방사병", 50, 16) # 객체 생성, 체력 50, 공격력 16
flamethrower1.attack("5시") # 5시 방향으로 공격 명령

# 25만큼의 공격을 2번 받음
flamethrower1.damaged(25) # 남은 체력 25
flamethrower1.damaged(25) # 남은 체력 0


