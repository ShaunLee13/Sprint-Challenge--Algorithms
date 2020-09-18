#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
    This snippet would be O(n) because its linear in function. a increases by a specified constant amount each iteration (n*n), but because it relies on the value of n to determine # loops run and complexity, it would be a linear (n) instead of a constant (1)


b) O(n log n)
    The outer for loop would be an O(n) complexity, as it relies on the size of n. The inner while loop increments by a constant multiplied amount which would make it an O(log n) complexity. Combined they would make a function with O(n log n) time complexity

c) O(n)
    This snippet is a linear recursion. Each iteration of the recursion call subtracts 1 from the value originally passed into it, and it will continue down until theres none left in that value. Since each recursive loop decrements by a set amount until complete, it is linear.

## Exercise II
    One implementation of this algorithm would be to use a binary search to locate the floor the egg breaks on. Since this would reduce the size of the input by half of its original amount each time, this would be a O(log n) complexity. 

    def eggdrop(stories (n)):
        instantiate a new variable, eggs_broken, and start at 0 to track how many eggs used in the process

        instantiate 2 variables:
        start is 0, this will be our bottom floor
        end is length of n - 1, this represents our top floor

        first thing we want to check is if the length of n is equal to 1:
            if it is, it's the only floor, so we want to return start

        next, we check if end is equivalent to breaks_on:
            if it is, increment eggs_broken by 1
            and we can return end and don't have to check the remaining floors.

        otherwise:
            midpoint will be the floored amount between our start divided by our end
            set end to end - 1 (as we've already now checked the top floor)

            next, create a while loop to check our remaining floors
            while the start of our drop area is less than our endpoint:

                we want to check if the difference between our start and end is == 1:
                    if it is, our next floor is where eggs start breaking, so we can return start
                otherwise:

                    drop an egg from midpoint

                    if egg breaks:
                        increment eggs_broken by 1
                        set our endpoint to our midpoint; we know our midpoint is currently the highest point where eggs break.
                    if it doesn't break:
                        set start to midpoint; since we know that midpoint is currently safe, we will set that as the start of our search area and ignore all the floors below it