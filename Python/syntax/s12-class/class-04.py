class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
class AttackUnit:
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)#Unit클래스의 생성자를 참조함
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향 적군을 공격합니다. [공력력 {2}]".format(self.name, location, self damage))