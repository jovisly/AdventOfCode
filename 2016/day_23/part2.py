# The solution below comes from observing the progression of a, b, c, and d from
# part 1, using a smaller initial a such as 6 and 7 (5 doesn't work; see below).
#
# Initially, we just ran part1 for values of 6, 7, 8, 9, 10, and even 11. Of
# course for 12 we were hanging indefinitely as the problem had warned. Here are
# the values:
# 6  -      6,180
# 7  -     10,500
# 8  -     45,780
# 9  -    368,340
# 10 -  3,634,260
# 11 - 39,922,260
# We could not discern an obvious pattern to predict value for 12.
#
# Then, using the code from part 1, we ran value 6 again but printing out
# progression for a. We saw that a goes up to 30, then drops to 0, then up to
# 120, then drop to 0, then up to 360, then drop to 0 again. To understand why,
# we print out all values of a, b, c, and d. Then it became clear that a goes up
# to 360, then through d, doubles to 720, then gains 78 * 70 from instructions
# 20 and 21. So this pattern looks like 6 * 5 * 4 * 3 * 2 + 78 * 70.
# This pattern was verified to also hold for 7, and satisifies all the values we
# have seen:
# 6  -      6,180 =  6! + 78 * 70
# 7  -     10,500 =  7! + 78 * 70
# 8  -     45,780 =  8! + 78 * 70
# 9  -    368,340 =  9! + 78 * 70
# 10 -  3,634,260 = 10! + 78 * 70
# 11 - 39,922,260 = 11! + 78 * 70
# Hence the answer is simply 12! + 78 * 70
#
# Then isn't it the case that for the starting value of 5, we'd get 5! + 78 * 70?
# Actually, for 5, we are stuck. After investigation, this is because we need
# instruction 25, "inc c", to be toggled to "dec c". This line is 8 lines after
# the toggle command. And when a starts at 5 (or lower), c never gets to 8,
# therefore c will keep on increasing instead of eventually getting to 0 which
# is the required value to terminate at line 26.
import math
print(math.factorial(12) + 70 * 78)
