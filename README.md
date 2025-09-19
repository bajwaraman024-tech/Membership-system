
**PURPOSE**

This python application handles the membership of the Whitecliffe Students Club. It is written in a class known as Membership which has variables, methods and menu system to do the functions like adding members, removing members and showing information. Most of the comments and docstrings are also present in the program and tell how this or that principle of software design is implemented.

**Clean code > Clear code**

The first program is formed at the start of the program is the Membership class. In the constructor method (init), Clean code > clever code is used as normal empty variables are created to be used later without a messy method. This is the fact that rather than adopting an elaborate configuration, the programmer opted to maintain cleanliness and simplicity. The storage of all member records is done in a list called member_list and counters are set to monitor the total number of the members, diploma students, bachelor students and the withdrawn members. The section of the code demonstrates the concept of clean is better than clever since it does not use sophisticated or complex methods and instead uses simplistic and straightforward solutions..

**KISS(Keep it Simple, Stupid)**

The register_member method is defined. KISS is used in this method which means that instead of creating a very complex validation system, the program just checks if the student ID starts with “W” to confirm they are Whitecliffe students. This is a very simple way to solve the problem, which is exactly what the KISS principle (Keep It Simple, Stupid) is about. The method also checks if the program is either “Diploma” or “Bachelor.” If the inputs are correct, the program creates a unique membership ID such as “WCCS1,” stores the details in a dictionary, and adds it to the member_list. Additionally, KISS is used  as simple dictionary is used instead of complex storage system. This means that the programmer chose a dictionary to store member details because it is the simplest way to keep track of attributes like student ID, last name, and program. The method ends by updating counters and printing a success message, which also shows a clean and easy-to-understand design.

After that, the withdraw_member method is defined. KISS principle is used as normal input method. This again shows the focus on simplicity. The program asks the user for their membership ID and last name, then looks through the list to find a match. If a member is found, they are removed, and the counters are updated. If not, an error is printed. This method is an example of the Single Responsibility Principle (SRP) as well, because it only does one thing withdrawing members.

The next method is display_members. The SRP is used in this method as this function only displays output. This means the method does not try to change the data or handle registration, it only shows information. If the list is empty, it prints a message saying no members are available. Otherwise, it loops through the list and prints each member’s details. After that, it displays the total number of members, the number of diploma and bachelor students, and the number of withdrawn members. This method is a clear example of SRP (Single Responsibility Principle) because it only focuses on displaying information.

**YAGNI(You Aren’t Gonna Need It)**

In show_member_details method, YAGNI is used, as normal input is used instead of complex ones. YAGNI stands for You Aren’t Gonna Need It, which means not adding unnecessary features. This method keeps things very simple: it asks for a membership ID, looks it up in the list, and either shows the details or prints an error. The programmer could have added extra search methods or advanced ways to look up members, but those were not needed. By keeping the method small and direct, the program follows the YAGNI principle.

**SRP( Single Responsibility Principle)**

In main_menu method, both KISS and SRP are  used, as this is a simple function calling based on the user's input. The method just displays five menu options and calls the correct method based on what the user chooses. It does not mix responsibilities for example, it does not handle registration itself. Instead, it simply directs the user to the right method. This is both simple (KISS) and focused on one responsibility (SRP).

**CONCLUSION**

To sum up, the KISS principle is used in places like input checking, storing data in dictionaries, and writing simple menus. The YAGNI principle is shown in the show_member_details method, where only the needed feature is written instead of adding unnecessary ones. The SRP principle is used in many methods like display_members, where the method only does one clear task. Finally, the idea of clean > clever is shown in the constructor and the main part of the program, where the programmer keeps the setup straightforward and easy to understand. These choices make the program beginner-friendly, simple to follow, and easy to maintain.
