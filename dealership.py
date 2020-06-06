
from car import Car, ElectricCar, PetrolCar, HybridCar, DieselCar
from customer import Customer
import sys
import pickle
import json


class Dealership(object):

    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.hybrid_cars = []

    def create_current_stock(self):
        for i in range(10):
           self.diesel_cars.append(DieselCar())
        for i in range(4):
           self.hybrid_cars.append(HybridCar())
        for i in range(6):
           self.electric_cars.append(ElectricCar())
        for i in range(40):
           self.petrol_cars.append(PetrolCar())

           

    def stock_count(self):
        stock_count=[]
        print('petrol cars in stock ' + str(len(self.petrol_cars)))
        stock_count.append(str(len(self.petrol_cars)))
        print('electric cars in stock ' + str(len(self.electric_cars)))
        stock_count.append(str(len(self.electric_cars)))
        print('diesel cars in stock ' + str(len(self.diesel_cars)))
        stock_count.append(str(len(self.diesel_cars)))
        print('hybrid cars in stock ' + str(len(self.hybrid_cars)))
        stock_count.append(str(len(self.hybrid_cars)))
        
        # write stock to text file
        # stock_count[0]= petrol car stock.
        # stock_count[1]= electric car stock.
        # stock_count[2]= diesel car stock.
        # stock_count[0]= hybrid car stock.
        
        # These lines open a file and write the current number of 
        # car of each type. 
        f = open('current_stock.txt', 'w')
        json.dump(stock_count, f)
        f.close()

        return stock_count
        
    
    def rent(self, car_list, amount):

        if len(car_list) < amount:
            print('Not enough cars in stock')
            return
        total = 0
        while total < amount:
           car_list.pop()
           total = total + 1
           
    def return_car(self, car_list, return_amount):
        
        # At the moment this function allow the user to return more car than
        # the rental company has stock of.
        # to add some sort of limit, i.e. can't return more than 40 petrol cars.
        ##################################################################
        # above in rent module stock was written as [] 
        # stock_count[0]= petrol car stock.
        # stock_count[1]= electric car stock.
        # stock_count[2]= diesel car stock.
        # stock_count[0]= hybrid car stock.
        
        
        # opens the file and read in the current stock of each car type
        
        with open ('current_stock.txt', 'r') as fp:
            stock_count = json.load(fp)
            print(stock_count[0]+ 'petrol cars in stock')
            print(stock_count[1]+ 'electric cars in stock')
            print(stock_count[2]+ 'diesel cars in stock')
            print(stock_count[3]+ 'hybrid cars in stock')

            
            
        if len(car_list) < return_amount:
            print('Not enough cars rented out')
            return

        total = 0
        while total < return_amount:
           car_list.append(1)
           total = total + 1
           
        # writes the current stock to a file. 
        f = open('current_stock.txt', 'w')
        json.dump(stock_count, f)
        f.close()
          

    def process_rental(self):
        option = input('''
                           
            Please select what you would like to do:
                               
                To hire a car enter '1' 
                To return a car enter '2' 
                To exit car menu a car enter '3' 
                               ''')
            
            
        if option == '1':
            
            
            answer = input('''
                           
            Please select the type of car you would like to hire:
                               
                for electric type 'e' 
                for petrol type 'p' 
                for diesel type 'd' 
                for hybrid type 'h' 
                ''')
            amount = int(input('how many would you like?'))
            if answer == 'p':
                self.rent(self.petrol_cars, amount)
            if answer == 'd':
                self.rent(self.diesel_cars, amount)
            if answer == 'h':
                self.rent(self.hybrid_cars, amount)
            else:
                self.rent(self.electric_cars, amount)
                self.stock_count()
        
        
        if option == '2':
            
            
            answer = input('''
                           
            Please select the type of car you would like to return:
                               
                for electric type 'e' 
                for petrol type 'p' 
                for diesel type 'd' 
                for hybrid type 'h' 
                ''')
            return_amount = int(input('how many would you like to return?'))
            print(return_amount)
            if answer == 'p':
                self.return_car(self.petrol_cars, return_amount)
            if answer == 'd':
                self.return_car(self.diesel_cars, return_amount)
            if answer == 'h':
                self.return_car(self.hybrid_cars, return_amount)
            if answer == 'e':
                self.return_car(self.electric_cars, return_amount)
            else:
                self.stock_count()
        if option =='3':
           print("exiting program, goodbye for now") 
           sys.exit

           

dealership = Dealership()
dealership.create_current_stock()
proceed = 'y'
while proceed == 'y':
    dealership.process_rental()
    proceed = input('continue? y/n')
    




