
# This is a set. Sets are unordered, unindexed, and unchangeable or immutable.
# Sets are created using curly brackets and they can't be duplicated.
# Sets are unordered, unindexed, and unchangeable or immutable.


evens = {2,4,6,8,7} 
odds = {1,3,5,7,9}
primes = {2,3,5,7}

union = evens.union(odds)
print(union)
union2 = evens & odds
print(union2)
# difference = evens.difference(odds)
# print(difference)

differ=  evens -odds
print(differ)

# set is much more efficient than list. 
#But if we need order we can't use set.
