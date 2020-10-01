import time
print("Hello. Welcome to buggati factory")

which_person = input("Are you a customer or an employee:  ")
if which_person == "customer":
    print("The feature will be added soon")
elif which_person == "eployeee":
    print("You can now get the body component")
    done_body_component = input("After your done press e:  ")
    if done_body_component == "e":
        print("Put the body on the stands")
        done_stands_wires = input("Enter e if your done:  ")
        if done_stands_wires == "e":
            print("Put the engine on the stand")
            done_stands_engine = input("Enter e if your done:  ")
            if done_stands_engine == "e":
                print("Put the automatic shift unit in front of the engine")
                done_atomatic_shif = input("Enter e if your done:  ")
                if done_atomatic_shif == "e":
                    print("Attach the shasy on the side section of the body")
                    done_shasy = input("Enter e if you are done")
                    if done_shasy == "e":
                        print("Mount the finished side section on the engine block")
                        done_mount_engine_block = input("Enter e if you are done.")
                        if done_mount_engine_block == "e":
                            print("Fit the exhaust system")
                            done_exaust_system = input("Enter e if you are done.")
                            if done_exaust_system == "e":
                                print("Install the brake disks")
                                done_brake_discs = input("Enter e if you are done:  ")
                                if done_brake_discs == "e":
                                    print("Attach the front and the back part together")
                                    front_back_together = input("Enter e if you are done:  ")
                                    if front_back_together == "e":
                                        print("Fill the car with its operative fluids")
                                        fill_car_builds = input("Enter e if you are done: ")
                                        if fill_car_builds == "e":
                                            print("Take it for a test drive")
                                            done_test_drive = input("Enter e if you are done:  ")
                                            if done_test_drive == "e":
                                                print("The bugatti is teady for the customer")
                                            else:
                                                print("I did not understand you")
                                        else:
                                            print("I did not understand you")
                                    else:
                                        print("I did not understand you")
                                else:
                                    print("I did not understand you")
                            else:
                                print("I did not understand you")

                        else:
                            print("I did not understand you")
                    else:
                        print("I did not understand you")
                else:
                    print("I did not understand you")
            else:
                print("I did not understand you")
        else:
            print("I did not understand you")

