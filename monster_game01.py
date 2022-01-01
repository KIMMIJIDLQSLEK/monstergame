import random
from time import sleep
#object클래스-이름,HP,공격력/'공격'메소드
class object():
    def __init__(self,name,hp,attack_power):
        self.name=name
        self.hp=hp
        self.attack_power=attack_power
    def attack(self,target):
        print(f'{self.name}가 {target.name}을 공격했다')
        target.hp-=self.attack_power

        if target.hp>0:
            print(f'{target.name}의 hp는 {target.hp}입니다')

#player클래스-object상속/'마법'메소드
class player(object):
    def __call__(self):
        print(f'name: {self.name}, hp: {self.hp}, attack_power: {self.attack_power} 인 참가자가 등장')
    def magic(self,target):
        print(f'{self.name}가 {target.name}을 공격했다')
        target.hp-=50
        print(f'{target.name}의 hp는 {target.hp}입니다')

#monster클래스-object상속/'대기','치료'메소드
class monster(object):
    def __call__(self):
        print(f'name: {self.name}, hp: {self.hp}, attack_power: {self.attack_power} 인 몬스터 출현')
    def wait(self):
        print(f'{self.name}가 대기했습니다')
    def cure(self):
        self.hp+=10
        print(f'{self.name}가 자신의 체력을 10만큼 회복했습니다')



monster_alive={}
#전사등장
print('\n--------참가자가 들어왔습니다--------')
player1=player('미지',100,10)
player1()
#몬스터 3마리 등장-딕셔너리에 몬스터의 상태 저장
print('\n--------몬스터 세마리 등장--------')
monster_alive['m1']=monster('m1',10,10)
monster_alive['m2']=monster('m2',30,30)
monster_alive['m3']=monster('m3',50,50)

for key,value in monster_alive.items():
    monster_alive[key]()
sleep(1)
def now_hp(player,monster_alive): #다시
    print('\n--------현재 상황--------')
    print(f'player의 hp: {player.hp}')
    for key,value in monster_alive.items():
        print(f'{value.name}의 hp: {value.hp}')

def player_turn():
    print('\n--------player의 차례입니다.--------')
    action=input('attack? magic?')
    who=input('어느 몬스터?')

    if action=='attack':
        player1.attack(monster_alive[who]);
    else:
        player1.magic(monster_alive[who]);

def monster_check(monster_alive):
    dead=[] #질문
    for key,value in monster_alive.items():
        if value.hp<=0:
            print(f'{value.name}이 죽었습니다')
            dead.append(key)
            #del monster_alive[key]

    for i in dead:            #질문
        del monster_alive[i]

    if len(monster_alive)==0:
        return len(monster_alive)

def monster_turn():
    print('\n--------몬스터들의 차례입니다.--------')
    for key,value in monster_alive.items():
        command=['cure','wait','attack']
        action=random.choice(command)
        if action=='cure':
            monster_alive[key].cure()
        elif action=='wait':
            monster_alive[key].wait()
        else:
            monster_alive[key].attack(player1)

def player_check(player1):
    if player1.hp<=0:
        return 0

#while문시작
while True:

    now_hp(player1,monster_alive);  #전사와 고블린의 체력 표시함수
    player_turn(); #플레이어 턴함수-공격,마법 입력/누구 공격할지 입력
    sleep(2)
    if monster_check(monster_alive) == 0: #몬스터 사망여부체크 함수-딕셔너리를 돌며 hp<0인 몬스터는 딕셔너리에서 제거/모두제거되면 플레이어 승 출력/while문 빠져나오기
        print('플레이어 승!')
        break;

    #print(monster_alive)
    sleep(2)
    monster_turn() #몬스터 턴함수-치료,대기,공격 랜덤(각각)
    sleep(2)
    if player_check(player1)==0:#플레이어 사망여부체크 함수-플레이어 hp<=0일경우 몬스터 승/while문 빠져나오기
        print('몬스터 승!')
        break;

#여기서 몰랐던 개념
#1. for key,value in monster_alive.items():=>딕셔너리의 값을 for문으로 돌리고 싶을때
#2. sleep =>일시정지
#3. del monster_alive[i]  =>del함수  / 굳이 list를 따로 만들어서 삭제해야하나