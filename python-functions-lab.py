def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum



def largest(list):
  largest = list[0]
  for n in list:
    if n > largest:
      largest = n
  return largest

def largest(nums):
  nums.sort()
  return nums[-1]



def occurances(string, letter):
    count = 0
    for char in string:
      if char == letter:
        count += 1
    return count

def product(*args):
  product = 1
  for num in args:
    product *= num
  return product