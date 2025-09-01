# SLC-6: Test cases for cows_and_bulls logic
from CowsAndBulls import cows_and_bulls

# Test Case 1: Exact match
assert cows_and_bulls("1234", "1234") == (4, 0)

# Test Case 2: All digits correct but wrong position
assert cows_and_bulls("1234", "4321") == (0, 4)

# Test Case 3: Some digits match
assert cows_and_bulls("1234", "1278") == (2, 0)

# Test Case 4: No digits match
assert cows_and_bulls("1234", "5678") == (0, 0)

print("✅ All SLC-6 test cases passed successfully!")
