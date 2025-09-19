"""
    here a class is created and constructor is also created, empty list is created as storage system, and other attributes are also created here,
    and register_member is created to input datas on attributes, and counter is also created to track thhe count 
"""




# create a class named Membership
class Membership():

    def __init__(self ):
        """Clean code > clever code as normal empty variables are created for future use without complex method"""
        self.member_list = [] # empty list stores all member records
        self.total_num_member = 0 #counts current members
        self.total_diploma_member= 0 #track program type
        self.total_bachelor_member = 0 #track program type
        self.total_withdrawn_member = 0 #counts how many left the club

    #create a method to register member
    """kiss is used here as this takes input and checks if student id start with W hence keeping it simple and stupid"""
    def register_member(self): #Asks for student ID, last name, and program
        while True:
            student_id = input("Enter your student id") 
            if not student_id.startswith("W"): #validates that Student ID must start with "W" (Whitecliffe students only) hence error validation
                print("Registration failed: Only Whitecliffe students (ID starting with 'W'")
                return 
            
            last_name = input("Enter your last name:") 
            programme = input("Enter your program:") 

            if programme not in ["Diploma", "Bachelor"]: #validates that - Program must be "Diploma" or "Bachelor", error validation again
                print("Invalid programme. Please enter 'Diploma' or 'Bachelor'.")
                return
            
            self.total_num_member += 1 
            membership_id= (f"WCCS{self.total_num_member}") # Assigns a unique Membership_id like "WCCS1", "WCCS2", etc.

            #create a dictionary of member details
            member_details = {
                    "Membership_id" : membership_id,
                    "Student_id" : student_id,
                    "last_name" : last_name,
                    "Programme" : programme
                } 
            """KISS, as simple dictionary is used instead of complex storage system"""
            self.member_list.append(member_details) #- Adds the member to member_list

            #Updates counters based on the program
            if programme.title() == "Diploma": 
                self.total_diploma_member += 1   

            if programme.title() == "Bachelor":
                self.total_bachelor_member += 1     

            # Displays success message and current member list
            print(f"{last_name} registered successfully with Membership ID: {membership_id}")
            print(self.member_list)
            break


    # create a method to withdraw member
    """ KISS principle is used as normal input method is used """
    def withdraw_member(self): #- Asks for their Membership_id and last name
        membership_id = input("Enter Membership ID to withdraw: ").strip().upper() #gets input id and removes excess space and makes whole thing uppercase
        last_name = input("Enter Last Name: ").strip()      

        #Searches for a match in member_list
        for member in self.member_list : 
            print(self.member_list, "memid=", membership_id, "lastname=", last_name) 

            if member["Membership_id"] == membership_id and member["last_name"] == last_name: #If found
                self.member_list.remove(member)#Removes the member
                
                #Updates counters (including withdrawn count)
                self.total_withdrawn_member  += 1 
                self.total_num_member -= 1 

                if member["Programme"] == "Diploma": 
                    self.total_diploma_member -= 1 
                else:
                    self.total_bachelor_member-= 1

                print(f"Member {membership_id} ({last_name}) successfully withdrawn.")
                print(self.member_list)
                return
            else:
                print(" Error: Member not found or details do not match.")

    #create a method to display members 
    """SRP is used in this method as this funciton only displays output"""
    def display_members(self):

        
        if not self.member_list:
            print(" No active members to display.")
        else:
            print("\nRegistered Members:")
            for member in self.member_list: #Lists each member’s ID, student ID, name, and program via looping
                print(f"ID: {member['Membership_id']}, Student ID: {member['Student_id']}, " 
                    f"Name: {member['last_name']}, Programme: {member['Programme']}")

        #Shows club statistics     
        print("\n Club Statistics:") 
        print(f"Total Members: {self.total_num_member}") 
        print(f"Diploma Students: {self.total_diploma_member}")
        print(f"Bachelor Students: {self.total_bachelor_member}")
        print(f"Withdrawn Members: {self.total_withdrawn_member}")

    """YAGNI is used in this method normal input is uised instead of complex ones so YAGNI"""
    def show_member_details(self): #Looks up one member by their Membership_id
        membership_id = input("Enter Membership ID to view details: ").strip().upper() #gets input id and removes excess space and makes whole thing uppercase

        #If member found, prints their details
        for member in self.member_list:
            if member["Membership_id"] == membership_id:
                print(f"\nMember Details for {membership_id}:")
                print(f"Student ID: {member['Student_id']}")
                print(f"Last Name: {member['last_name']}")
                print(f"Programme: {member['Programme']}")
                return

        #If member not found, shows an error
        print(" No member found with that Membership ID.")

    """KISS and SRP is used in this main_menu as this is a simple funciton calling based on users input"""
    def main_menu(self):
        #Displays a menu with 5 options
        while True:
            print("\nWhitecliffe Students Club Membership System")
            print("1. Register a new member")
            print("2. Withdraw a member")
            print("3. Display all members and statistics")
            print("4. Show specific member details")
            print("5. Quit")

            choice = input("Select an option (1-5): ").strip()


            #Based on user input, it calls the appropriate method
            if choice == "1":
                self.register_member()
            elif choice == "2":
                self.withdraw_member()
            elif choice == "3":
                self.display_members()
            elif choice == "4":
                self.show_member_details()
            #Keeps running until the user chooses to quit
            elif choice == "5":
                ("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 5.")

#program starts by creating a Membership object and launching the menu
if __name__ == "__main__":
    system = Membership() #object called system is created here
    system.main_menu()















