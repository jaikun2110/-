# -*- coding: utf-8 -*-

# 클래스와 객체 생성하기 

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name # 인스턴스 변수 name에 전달값 name 저장
        self.hp = hp    # 인스턴스 변수 hp에 전달값 hp 저장
        self.damage = damage  # 인스턴스 변수 damage에 전달값 damage 저장
        print(" {0} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
        
soldier1 = Unit("보병", 40, 5)
soldier2 = Unit("보병", 40, 5)
tank = Unit("탱크", 150, 35)

#%%
# 전투기 : 공중 유닛, 은폐 불가
stealth1 = Unit("전투기", 250, 100)

print("유닛 이름 : {0}, 공격력 : {1}".format(stealth1.name, stealth1.damage))
#%%
# 은폐 가능 전투기

stealth2 = Unit("업그레이드한 전투기", 500, 250)
# 업그레이드한 전투기만을 위한 특별한 인스턴스 변수 정의, 은페 상태
stealth2.cloaking = True

if stealth2.cloaking == True: # 은폐 상태라면
    print("{0}는 현재 은페 상태입니다.".format(stealth2.name))
    
#%%

class AttackUnit: # 공격 유닛
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        
    def attack(self, location): # 전달받은 뱡향으로 공격
        print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name, location, self.damage)) # 공간이 좁아서 2줄로 나눔
            
    def damaged(self, damage): # damage 만큼 유닛 피해
    # 피해정보 출력
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage
    # 남은 체력 출력
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0: # 남은 체력이 0 이하이면
            print("{0} : 파괴됐습니다.".format(self.name))
            

#%%

# 화염방사병: 공격 유닛, 화염방사기를 사용함
flamethrower1 = AttackUnit("화염방사병", 50, 16) # 객체 생성, 체력 50, 공격력 16
flamethrower1.attack("5시") # 5시 방향으로 공격 명령

flamethrower1.damaged(25)
flamethrower1.damaged(25)