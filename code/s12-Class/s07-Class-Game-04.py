
#9.4

# 건물 유닛
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

# 보급고: 건물 유닛, 1개 건물 유닛 = 8유닛
supply_depot = BuildingUnit("보급고", 500, "7시") # 체력 500, 생성 위치 7시

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()


