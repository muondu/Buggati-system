import sqlite3
conn = sqlite3.connect("available_cars.db")
c = conn.cursor()


c.execute('CREATE TABLE IF NOT EXISTS car_imformation(name TEXT, price TEXT)')
print("Hello. Welcome to buggati factory")

which_person = input("Are you a customer or an employee:  ")
if which_person == "customer":
    print("Welcome to the bugatti factory.")
    print("These are the types of bugattis available with their prices")
    c.execute('SELECT * FROM car_imformation')
    def buy_car():
        which_type_car = input("Which car do you want:  ")
        if which_type_car == " ":
            print("Yu can't put spaces")
        else:
            print("You have bought the car.")
            print("Have a good time with the new car")
            c.execute('DELETE FROM car_imformation WHERE name = ?',(which_type_car))
elif which_person == "eployeee":
    def body():
        print("Get the body components and put them on the stand")
        done1 = input("Enter e if you are done:  ")
        if done1 == "e" or done1 == "E":
            def wires():
                print("Now put all the wires")
                done2 = input("If you are done enter e:  ")
                if done2 == "e" or done2 == "E":
                    def engine_stand():
                        print("Now you can put the engine on the stand")
                        done3 = input("Enter e if done:  ")
                        if done3 == "e" or done3 == "E":
                            def atomatic_shift():
                                print("Now put the automatic shift unit in front of the engine")
                                done4 = input("Enter e if you are done:  ")
                                if done4 == "e":
                                    def shasy():
                                        print("Attach the shasy on the side section of the body")
                                        done5 = input("Enter e if done:  ")
                                        if done5 == "e" or done5 == "E":
                                            def finnished_side_block_engine():
                                                print("Mount the finished side section on the engine block")
                                                done6 = input("Enter e if you are done:  ")
                                                if done6 == "e" or done6 == "E":
                                                    def equast():
                                                        print("Fit the exhaust system")
                                                        done7 = input("Enter e if done:  ")
                                                        if done7 == "e" or done7 == "E":
                                                            def brake_discs():
                                                                print("Install the brake disks")
                                                                done8 = input("Enter e if done:  ")
                                                                if done8 == "e" or done8 == "E":
                                                                    def front_back():
                                                                        print("Attach the front and the back part together")
                                                                        done9 = input("Enter e if done:  ")
                                                                        if done9 == "e" or done9 == "E":
                                                                            def body_parts():
                                                                                print("Put the body parts in the car")
                                                                                done10 = input("Enter e if done:  ")
                                                                                if done10 == "e" or done10 == "E":
                                                                                    def test_drive():
                                                                                        done11 = input("Enter e if done:  ")
                                                                                        if done11 == "e" or done11 == "E":
                                                                                            def regestiring_car():
                                                                                                name_of_bugatti = input("Enter the type name of the bugatti:  ")
                                                                                                price_of_bugatti = input("Enter the price of the buggatti:  ")
                                                                                                c.execute('INSERT INTO car_imformation VALUES(?,?)',(name_of_bugatti,price_of_bugatti))
                                                                                            regestiring_car()
                                                                                        else:
                                                                                            print("I did not understand you")
                                                                                            test_drive()
                                                                                    test_drive()
                                                                                else:
                                                                                    print("I did not understand you")
                                                                                    body_parts()
                                                                            body_parts()
                                                                        else:
                                                                            print("I did not understand you")
                                                                            front_back()
                                                                    front_back()
                                                            brake_discs()
                                                        else:
                                                            print("I did not understand you")
                                                            equast()
                                                    equast()
                                                else:
                                                    print("I did not understand you. Please try again.")
                                                    finnished_side_block_engine()
                                            finnished_side_block_engine()
                                        else:
                                            print("I did not understand you")
                                            shasy()
                                    shasy()
                                else:
                                    print("I did not understand you")
                                    atomatic_shift()
                            atomatic_shift()
                        else:
                            print("I did not understand you")
                            engine_stand()
                    engine_stand()
                else:
                    print("I did not understand you")
                    wires()
            wires()
        else:
            print("I did not understand you")
            body()
    body()