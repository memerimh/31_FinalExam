"""
Final exam, problem 4.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Mattias Memering.  May 2018.

"""  # TDO: 1. PUT YOUR NAME IN THE ABOVE LINE.


###############################################################################
# TDO: 2.
#   In this problem, you will go through the methods of the  Pig  class
#   that is defined below, one by one, in the order that they appear.
#   For each method:
#      (a) Read the method's doc-string (i.e., specification in double-quotes).
#            If you do not understand WHAT the method is to do,
#            ask your instructor to clarify it.
#      (b) Implement the method.
#      (c) Write at least SOME code  in  main  that tests your code.
#
###############################################################################

def main():
    """ Tests the  Pig  class. """
    # -------------------------------------------------------------------------
    # WRITE CODE HERE AS NEEDED to TEST the code that you write
    #   in the  Pig  class.  At the least, you must:
    #     -- Construct two Pig objects
    #     -- Call each method that you implement below.
    # -------------------------------------------------------------------------
    wilbur = Pig(5)
    print(wilbur.get_weight())
    wilbur.eat(10)
    print(wilbur.get_weight())
    wilbur.eat_for_a_year()
    print(wilbur.get_weight())
    whately = Pig(3)
    heavy = wilbur.heavier_pig(whately)
    print(heavy.get_weight())
    yog = whately.new_pig(wilbur)
    print(yog.get_weight())


class Pig(object):
    def __init__(self, weight):
        """
        What comes in:  The Pig's weight (in pounds).
        Side effects: Sets instance variables as needed by the other methods.
        """
        self.weight = weight
        # TDO: Implement and test this method.

    def get_weight(self):
        """ Returns this Pig's weight. """
        return self.weight
        # ODO: Implement and test this method.

    def eat(self, pounds_of_slop):
        """
        Increments this Pig's weight by the given pounds_of_slop.
        """
        self.weight = self.weight + pounds_of_slop
        # TDO: Implement and test this method.

    def eat_for_a_year(self):
        """
        Calls the   eat   method as many times as needed to make this Pig:
          -- eat 1 pound of slop, then
          -- eat 2 pounds of slop, then
          -- eat 3 pounds of slop, the
          -- eat ... [4 pounds, then 5, then 6, then ... ]
          -- eat 364 pounds of slop, then
          -- eat 365 pounds of slop.
        """
        for k in range(364):
            self.eat(k + 1)
        # TOO: Implement and test this method.

    def heavier_pig(self, other_pig):
        """
        Returns either this Pig object or the other given Pig object,
        whichever is heavier.
        """
        if self.get_weight() >= other_pig.get_weight():
            return self
        else:
            return other_pig
        # TDO: Implement and test this method.

    def new_pig(self, other_pig):
        """
        Returns a new Pig whose weight is the weight of the heavier
          of this Pig and the other_Pig.
        """
        heavy = self.heavier_pig(other_pig)
        newpig = Pig(heavy.get_weight())
        return (newpig)
        # ODO: Implement and test this method.


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
