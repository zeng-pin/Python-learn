class Circle:
    def __init__(self,r):
        self.r=r

    def get_area(self):
        return 3.141*pow(self.r,2)

    def get_perimeter(self):
         return 2*3.141*self.r


r_input=eval(input('请输入圆的半径: '))
r=Circle(r_input)
area=r.get_area()
perimeter=r.get_perimeter()

print(f'圆的面积是{area:.2f},圆的周长是{perimeter:.2f}',end='')