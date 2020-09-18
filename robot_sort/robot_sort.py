class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # get rid of the none item first
        # while i can move right, move right
        while self.can_move_right():
            self.move_right()
            # if i can't move right, put my none item there
            if self.can_move_right() == False:
                self.swap_item()
        
        # once we've set our none item, go back to beginning
        while self.can_move_left():
            self.move_left()

        
        # while i can still move right,
        while self.can_move_right():         
            # this will be my base case check so i don't get stuck in a loop
            # if i can't move left anymore, and comparing items shows me i have None with me
            if self.can_move_left() == False and self.compare_item() == None:
                
                # I want to break out of the loop so I don't swap anymore
                break

            # i first check my light
            # if the light is turned on, i go back to the start
            if self.light_is_on():
                while self.can_move_left():
                    self.move_left()
                    # if the item i bring back is smaller than what is at the beginning
                    # swap the items
                    if self.can_move_left() == False and self.compare_item() == -1:
                        self.swap_item()
                self.set_light_off()

            # if I'm not at the end of the loop i check the item in my hands
            # if what i'm holding is bigger than what's on the table
            elif self.compare_item() == 1:
                # i need to keep moving right
                self.move_right()
                # if i move to the right and reach the end of my loop
                if self.can_move_right() == False:
                    # i want to swap my current item(which should be biggest) with my None
                    self.swap_item()
                    # and shift it one position to the left
                    self.move_left()
                    
                    #NOTE: this will protect my list when everything else is sorted
                    if self.can_move_left() == True:
                        self.swap_item()
                    # then, i turn my light back on, so i know to go back to the start
                    self.set_light_on()


            # however, if the item is smaller than the item on the table
            elif self.compare_item() == -1:

                # i want to make sure that there is space to my left
                if self.can_move_left() == False:
                    
                    # if i don't have space, and what I'm holding is smaller, then this is the smallest item so i need to put it down here
                    self.swap_item()
                # otherwise if there is space
                else:
                    # i will move to the left, and set the item down
                    self.move_left()
                    #however, to make sure i don't overwrite something i already set
                    if self.compare_item() == 1:
                        # then I will move back to the right so i can force myself to swap the items
                        self.move_right()

                    self.swap_item()
                    # then, i turn my light on, so i know i am done with this iteration
                    self.set_light_on()

            # if i reach None again
            elif self.compare_item() == None:
                # i want to swap my current item(which is the next largest) with my None again
                self.swap_item()
                # and shift it one position to the left
                self.move_left()
                
                #NOTE: this will protect my list when everything else is sorted
                if self.can_move_left() == True:
                    self.swap_item()
                # then, i turn my light back on, so i know to go back to the start
                self.set_light_on()                

            # and if i encounter numbers that are the same
            else:
                # i want to move to the right, swap the items and turn my light on
                self.move_right()
                if self.compare_item() == -1:
                    self.swap_item()
                    self.set_light_on



if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    # l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]
    l = [15, 41, 58, 49, 41, 26, 4]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)