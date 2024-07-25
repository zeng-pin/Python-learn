class Car:
    def __init__(self,car_type,car_id):
        self.car_type=car_type
        self.car_id=car_id
    def start(self):
        print('start the car')
    def stop(self):
        print('stop the car')


class Taxi(Car):
    def __init__(self,car_type,car_id,taxi_company):
        super().__init__(car_type,car_id)
        self.taxi_company=taxi_company

    def start(self):
        print('hello taxi')

    def stop(self):
        print('the taxi is stop')

class PersonalCar(Car):
    def __init__(self,car_type,car_id,ownername):
       super().__init__(car_type,car_id)
       self.ownername=ownername

    def start(self):
        print('this is my own car')

    def stop(self):
        print('my car is stop')

taxi1=Taxi('SPCAR','ZC1589','qing')
pcar=PersonalCar('XSTAR','QH4566','ppp')

print(taxi1.car_id,taxi1.car_type,taxi1.taxi_company)
print(pcar.car_id,pcar.car_type,pcar.ownername)
taxi1.start()
pcar.stop()
