# 9.3
# 클래스 상속

#9.3.1
class Unit:
    def __init__(self, name, hp):
        self.name = name 
        self.hp = hp 

class AttackUnit(Unit): # Unit 클래스 상속
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 부모 클래스의 생성자 호출
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

flamethrower1 = AttackUnit("화염방사병", 50, 16)
flamethrower1.attack("5시") # 5시 방향으로 공격 명령

# 25만큼의 공격을 2번 받음
flamethrower1.damaged(25) # 남은 체력 25
flamethrower1.damaged(25) # 남은 체력 0


#%%

#9.3.2
class Unit:
    def __init__(self, name, hp):
        self.name = name 
        self.hp = hp 

class AttackUnit(Unit): # Unit 클래스 상속
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 부모 클래스의 생성자 호출
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

# 비행 기능
class Flyable:
    def __init__(self, flying_speed): # 비행 속도
        self.flying_speed = flying_speed
    
    def fly(self, name, location): # 유닛 이름, 비행 방향
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
            .format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed): # 유닛 이름, 체력, 공격력, 비행 속도
        AttackUnit.__init__(self, name, hp, damage) # 유닛 이름, 체력, 공격력
        Flyable.__init__(self, flying_speed) # 비행 속도

# 요격기: 공중 공격 유닛, 미사일 여러 발을 한 번에 발사
interceptor = FlyableAttackUnit("요격기", 200, 6, 5) # 유닛 이름, 체력, 공격력, 비행 속도
interceptor.fly(interceptor.name, "3시") # 3시 방향으로 이동


#9.3.3
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed): # speed 추가
        self.name = name
        self.hp = hp
        self.speed = speed # 지상 이동 속도

    def move(self, location): # 이동 동작 정의
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
            .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit): # Unit 클래스 상속
    def __init__(self, name, hp, damage, speed): # speed 추가
        Unit.__init__(self, name, hp, speed) # speed 추가
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

# 비행 기능
class Flyable:
    def __init__(self, flying_speed): # 비행 속도
        self.flying_speed = flying_speed
    
    def fly(self, name, location): # 유닛 이름, 비행 방향
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
            .format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0) # 지상 이동 속도 0
        Flyable.__init__(self, flying_speed) # 비행 속도

    def move(self, location): # Unit 클래스의 move() 메서드를 오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 호버 바이크: 지상 유닛, 기동성 좋음
hoverbike = AttackUnit("호버 바이크", 80, 20, 10) # 지상 이동 속도 10

# 우주 순양함: 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
spacecruiser = FlyableAttackUnit("우주 순양함", 500, 25, 3) # 비행 속도 3

hoverbike.move("11시")
#spacecruiser.fly(spacecruiser.name, "9시")
spacecruiser.move("9시") # 오버라이딩한 move() 메서드 호출


