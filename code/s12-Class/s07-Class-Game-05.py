#9.5

# 건물 유닛
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0) # 지상 이동 속도 0, 건물은 지상 이동 불가
        super().__init__(name, hp, 0) # 부모 클래스 접근, self 없이 사용
        self.location = location


