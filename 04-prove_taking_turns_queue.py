"""
CSE212 
(c) BYU-Idaho
04-Prove - Problem 1

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online. Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class Taking_Turns_Queue:
    """
    This queue is circular.  When people are added via add_person, then they are added to the 
    back of the queue (per FIFO rules).  When get_next_person is called, the next person
    in the queue is displayed and then they are placed back into the back of the queue.  Thus,
    each person stays in the queue and is given turns.  When a person is added to the queue, 
    a turns parameter is provided to identify how many turns they will be given.  If the turns is 0 or
    less than they will stay in the queue forever.  If a person is out of turns then they will 
    not be added back into the queue.
    """

    class Person:
        """
        A person is defined with a name and a number of turns.
        """

        def __init__(self, name, turns):
            """
            Initialize the person
            """
            self.name = name
            self.turns = turns

        def __str__(self):
            """
            Support the display of single person.
            """
            if self.turns <= 0:
                result = "({}:Forever)".format(self.name)
            else:
                result = "({}:{})".format(self.name, self.turns)
            return result

    def __init__(self):
        """ 
        Start with an empty queue
        """
        self.people = []

    def add_person(self, name, turns):
        """
        Add new people to the queue with a name and number of turns
        """
        person = self.Person(name, turns)
        self.people.append(person)

    def get_next_person(self):
        """
        Get the next person in the queue and display them.  The person should
        go to the back of the queue again unless the turns variable shows that they 
        have no more turns left.  Note that a turns value of 0 or less means the 
        person has an infinite number of turns.  An error message is displayed 
        if the queue is empty.
        """
        if len(self.people) == 0:
            print("No one in the queue.")
            return
        
        person = self.people.pop(0)
        print(person.name)

        if person.turns == 0:
            person.turns = 10000

        if person.turns != 0:
            person.turns -= 1
            if person.turns != 0:
                self.people.append(person)

    def __len__(self):
        """
        Support the len() function
        """
        return len(self.people)

    def __str__(self):
        """
        Provide a string representation of everyone in the queue
        """
        result = "["
        for person in self.people:
            result += str(person)
            result += ", "
        result += "]"
        return result

print("Test 1")
players = Taking_Turns_Queue()
players.add_person("Bob", 2)
players.add_person("Tim", 5)
players.add_person("Sue", 3)
#print(players)    # This can be un-commented out for debug help
while len(players) > 0:
    players.get_next_person()
# Defect(s) Found: 
#It iterates through each person in order however many times they have turns instead of taking turns. 

print("=================")

# Test 2
# Scenario: Create a queue with the following people and turns: Bob (2), Tim (5), Sue (3)
#           After running 5 times, add George with 3 turns.  Run until the queue is empty.
# Exepcted Result: Bob, Tim, Sue, Bob, Tim, Sue, Tim, George, Sue, Tim, George, Tim, George
print("Test 2")
players = Taking_Turns_Queue()
players.add_person("Bob", 2)
players.add_person("Tim", 5)
players.add_person("Sue", 3)
for i in range(5):
    players.get_next_person()
#print(players)
players.add_person("George", 3)
#print(players)
while len(players) > 0:
    players.get_next_person()
# Defect(s) Found: It runs all their names at once besides Tim. For some reason, it breaks his turns up.

print("=================")

# Test 3
# Scenario: Create a queue with the following people and turns: Bob (2), Tim (Forever), Sue (3)
#           Run 10 times.
# Exepcted Result: Bob, Tim, Sue, Bob, Tim, Sue, Tim, Sue, Tim, Tim
print("Test 3")
players = Taking_Turns_Queue()
players.add_person("Bob", 2)
players.add_person("Tim", 0)
players.add_person("Sue", 3)
#print(players)
for i in range(10):
    players.get_next_person()
#print(players)    
# Defect(s) Found: It mixes it up and then displays that there's no one in the queue. It doesn't take into account the forever turns.

print("=================")

# Test 4
# Scenario: Try to get the next person from an empty queue
# Exepcted Result: Error message should be displayed
print("Test 4")
players = Taking_Turns_Queue()
players.get_next_person()
# Defect(s) Found: I don't see any errors.
    