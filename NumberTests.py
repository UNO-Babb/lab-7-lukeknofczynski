#NumberTests.py

def isThreeOrFive(n):
  """Returns boolean determination if number is multiple of 3 or 5"""

  if n % 3 == 0 or n % 5 == 0:
    return True
  else:
    return False

def isPrime(p):
  """Returns boolean (True/False) if the value given is prime."""
  if p == 2:
    return True
  for num in range(2, p):
    if p % num == 0:
      return False
  else:
    return True

def isEven(n):
  """Returns boolean about given value being even."""

  if n % 2 == 0:
    return True
  else:
    return False

def addNum(numList, num):
  """Adds the given number to the given list. Does not add duplicate values."""

  numList.append(num)


def fibonacciSequence(value):
  """Returns a list of numbers in the fibonacci sequence up to the given value"""

  nums = [1, 2]
  size = 2
  n = nums[size - 1] + nums[size - 2]

  while n < value:
    addNum(nums, n)
    size = len(nums)
    n = nums[size - 1] + nums[size - 2]

  return nums

#Test your new functions in this main
def main():
  knownPrimes = [3, 7, 11, 13, 17]
 
 #problem 10
 
  total = 0
  for i in range(0, 2000000):
    if isPrime(i):
      total += i
  print(total)
 
  #Problem 7
 
  primeNumbers = 0
  allNumbers = 2
  while primeNumbers < 10001:
    if isPrime(allNumbers):
      primeNumbers = primeNumbers + 1
    allNumbers = allNumbers + 1
  print(allNumbers - 1)

if __name__ == '__main__':
    main()
  