#
# Safecracker 50 solver by Wade Brainerd <wadetb@gmail.com>
#
#     A B C D
#   P         E
#   O         F
#   N         G
#   M         H
#     L K J I
#
# There are five rings.
#
# The first ring has 16 outer numbers and 16 inner numbers.
# The second-fourth rings have 8 outer numbers and 16 inner numbers each.
# The fifth ring has 8 outer numbers.
#
# The second through fifth rings can rotate to 16 positions.
# Each ring after the first shows its outer number for even slots, and reveals the prior ring's inner number for odd slots.
#
# To open, the rings are rotated such that sum of the shown number from the five rings for each slot must equal 50.
#
# The implementation plan is to recursively cycle through all possible positions of the four movable wheels- (16^4=65536).
# As an optimization, branches can be pruned if the sum exceeds 50 before reaching the final ring.
#
# Start at the outer ring, and proceed inwards, recursing using functions or a stack.  
# At each level, all the earlier rings are fixed, and their slot sums are pre-calculated.
# All rotation possibilities for the current ring are tried.  
# For each rotation, numbers are drawn from the master array given the current and prior rings' rotation.  If none of the slot sums exceeds 50,
# the next ring is evaluated recursively, given the prior numbers, current sums and rotation.
# When the final ring is evaluated an all sums equal 50, all shown numbers are printed to the console with a success message.
#
# Example of covering:
#
# rotation=0
# Ring 0 inner:  A B C D E F G H I J K L M N O P
# Ring 1 outer:  a   b   c   d   e   f   g   h
# Shown:         a B b D c F d H e J f L g N h P
#
# rotation=1
# Ring 0 inner:  A B C D E F G H I J K L M N O P
# Ring 1 outer:    a   b   c   d   e   f   g   h
# Shown:         A a C b E c G d I e K f M g O h
#
# On my board, starting slot 0 rotation 0 is 0 6 0 3 6, using smallest least-CW-degrees digit on each row.
#

firstRing = [ 0, 16,  8,  4, 15,  7, 10,  1, 10,  4,  5,  3, 15, 16,  4,  7]

outerRings = [
	[ 6, 10,  8, 10,  9,  8,  8,  9],
	[ 0, 11,  8,  8,  8, 10, 11, 10],
	[ 3,  8, 10, 14, 11,  8, 12, 11],
	[ 6,  6,  8,  8, 16, 19,  8, 17]
]

innerRings = [
	[13, 11, 13, 10, 18, 10, 10, 10, 10, 15,  7, 19, 18,  2,  9, 27],
	[ 5,  1, 24,  8, 10, 20,  7, 20, 12,  1, 10, 12, 22,  0,  5,  8],
	[20,  8, 19, 10, 15, 29, 12, 20, 13, 13,  0, 22, 19, 10,  0,  5],
	[10, 17, 10,  5,  6, 18,  8, 17,  4, 20,  4, 14,  4,  5,  1, 14],
]

rotations = [0 for i in range(4)]
shown = [[0 for i in range(16)] for j in range(4)]

def solve(ring, sums, priorRotation):
	if ring == 4:
		return all([s == 50 for s in sums])

	for rotation in range(0, 16):
		def shownNumber(slot):
			if rotation & 1 == slot & 1:
				return outerRings[ring][((slot + 16 - rotation) & 15)/2]
			else:
				return innerRings[ring][(slot + 16 - priorRotation) & 15]

		rotations[ring] = rotation
		shown[ring] = [shownNumber(s) for s in range(16)]
		nextSums = [sums[s] + shown[ring][s] for s in range(16)]

		if max(nextSums) > 50:
			return False

		if solve(ring + 1, nextSums, rotation):
			return True

	return False

if solve(0, firstRing, 0):
	print "rotations: %r" % rotations
	print "rings: %r" % shown
