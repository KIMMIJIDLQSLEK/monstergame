#이름과 동물을 지정해서 인스턴스를 생성하는 동물이라는 클래스를 생성하고,
#동물을 상속받아 고양이 클래스를 망들어 야옹을 출력하는 함수를 만들고
#동물을 상속받아 강아지 클래스를 만들어 왈왈을 출력하는 함수를 만들어주세요

class animal():                        #부모클래스
    def __init__(self,name):
        self.name=name

class cat(animal):                     #자식클래스
    def __init__(self,name):
        super().__init__(name)
        print({self.name},"은 야옹소리를 냅니다")

class dog(animal):                      #자식클래스
    def __init__(self,name):
        super().__init__(name)
        print({self.name},"은 왈왈소리를 냅니다")


cat1=cat('cat1')
cat2=cat('cat2')
dog1=dog('dog1')
dog2=dog('dog2')



