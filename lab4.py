# ООП

class Cars():
    def __init__(self):
        self.lst = []
        
        
    def add(self):
        vvod = ''
        while vvod != "стоп":
                print("Введите цвет, объем двигателя и производителя автомобиля через пробел(если машин больше нет, пишите команду 'стоп':")
                avt = input().split()
                if avt != []:
                    vvod = avt[0]
                else:
                    continue
                if vvod != 'стоп':
                    self.lst.append(avt)
        return True
          
          
    def edit(self):
        n = len(self.lst)   
        #print("Для изменения параметров нажмите 'Enter'")
        vvod = ""
        
        while vvod != "0":
            
            self.show_spisok()
                
            print("Для изменения параметров машины выберите номер введенной машины от 1 до", n, ", если изменение параметров закончено - введите цифру '0'")
            ch = int(input())
            
            if ch == 0:
                return True
            
            print("Введите какой параментр хотите изменить[цвет, объем двигателя, производитель]")
            vvod = input()
            if ch == 0:
                return True
            
            if vvod == 'цвет':
                print("Введите замену цвета")
                a = input()
                self.lst[ch-1][0] = a
                        
            elif vvod == 'объем двигателя':
                print("Введите замену объема двигателя")
                a = input()
                self.lst[ch-1][1] = a
                        
            elif vvod == 'производитель':
                print("Введите замену производителя")
                a = input()
                self.lst[ch-1][2] = a
                    
            else:
                print("Введите корректное значение")
                 
                 
                        
    def delete(self):
        
        self.show_spisok()
                
        n = len(self.lst)
        print("Введите номер автомобиля который хотите удалить, число от 1 до", n)
        a = int(input())
        self.lst.remove(self.lst[a-1])
        return True
    
    
    def show_spisok(self):
        for i in range(len(self.lst)):
            print(' '.join(self.lst[i]))



prog = "run"
car = Cars()
while prog != "закончить":
    print("Введите то, что хотите сделать: 'добавить','изменить','удалить','закончить', 'показать список'")
    vvod = input()
    if vvod == "добавить":
        car.add()
            
    elif vvod == "изменить":
        car.edit()
        
    elif vvod == "удалить":
        car.delete()
    
    elif vvod == "закончить":
        car.show_spisok()
        prog == "закончить"
        break
    
    elif vvod == "показать список":
        car.show_spisok()