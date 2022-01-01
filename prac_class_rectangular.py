# #직사각형의 가로, 세로만 지정해서 직사각형을 생성
# #멤버 메소드를 이용해서 넓이와 둘레를 구할 수 있는 클래스를 생성
# #(생성자, 넓이, 둘레 함수 총 세가지가 포함되어야함)

class nemo:                                #한 클래스안에 여러 메서드 넣기
    def __init__(self,row,column):         #클래스 실행시 반드시 실행됨
        self.row=row                       #객체생성
        self.column=column                 #객체생성

    def area(self):
        result=self.row*self.column
        return result
    def circum(self):
        result=2*(self.row+self.column)
        return result

a=int(input('가로를 입력하세요:'))
b=int(input('세로를 입력하세요:'))

n=nemo(a,b)                               #입력받은값 클래스에 넣기
print(n.area())
print(n.circum())









# class element():
#     def __init__(self,row,column):
#         self.row=row
#         self.column=column
#
# class area(element):
#     def __init__(self,row,column):
#         super().__init__(row,column)
#         print('직사각형의 넓이는',self.row*self.column)
#
# class circumference(element):
#     def __init__(self,row,column):
#         super().__init__(row,column)
#         print('직사각형의 둘레는',(self.row+self.column)*2)
#
#
# row=int(input('직사각형의 가로는:'))
# column=int(input('직사각형의 세로는:'))
#
# area(row,column)
# circumference(row,column)


