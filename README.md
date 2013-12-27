safecracker50
=============

Safecracker 50 solver by Wade Brainerd <wadetb@gmail.com>

       A B C D
     P         E
     O         F
     N         G
     M         H
       L K J I

There are five rings.

The first ring has 16 outer numbers and 16 inner numbers.
The second-fourth rings have 8 outer numbers and 16 inner numbers each.
The fifth ring has 8 outer numbers.

The second through fifth rings can rotate to 16 positions.
Each ring after the first shows its outer number for even slots, and reveals the prior ring's inner number for odd slots.

To open, the rings are rotated such that sum of the shown number from the five rings for each slot must equal 50.

### Algorithm

Recursively cycle through all possible positions of the four movable wheels- (16^4=65536).
As an optimization, branches can be pruned if the sum exceeds 50 before reaching the final ring.

Start at the outer ring, and proceed inwards, recursing using functions or a stack.  
At each level, all the earlier rings are fixed, and their slot sums are pre-calculated.
All rotation possibilities for the current ring are tried.  
For each rotation, numbers are drawn from the master array given the current and prior rings' rotation.  If none of the slot sums exceeds 50,
the next ring is evaluated recursively, given the prior numbers, current sums and rotation.
When the final ring is evaluated an all sums equal 50, all shown numbers are printed to the console with a success message.

### Covering example

     rotation=0
     Ring 0 inner:  A B C D E F G H I J K L M N O P
     Ring 1 outer:  a   b   c   d   e   f   g   h
     Shown:         a B b D c F d H e J f L g N h P

     rotation=1
     Ring 0 inner:  A B C D E F G H I J K L M N O P
     Ring 1 outer:    a   b   c   d   e   f   g   h
     Shown:         A a C b E c G d I e K f M g O h

On my board, starting slot 0 rotation 0 is 0 6 0 3 6, using smallest least-CW-degrees digit on each row.
