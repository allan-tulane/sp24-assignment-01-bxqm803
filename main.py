"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
      return x
    else:
      return foo(x-1)+foo(x-2)

def longest_run(mylist, key):
  max=0
  count=0
  for i in mylist:
      if i==key:
          count+=1
      else:
          if count>max:
              max=count
              count=0
  return max


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
  if len(mylist)==0:
    return Result(0,0,0,True)
  if len(mylist)==1:
    if mylist[0]==key:
      return Result(1,1,1,True)
    else:
      return Result(0,0,0,False)
  mid=len(mylist)//2
  left=longest_run_recursive(mylist[:mid],key)
  right=longest_run_recursive(mylist[mid:],key)
  is_entire_range = left.is_entire_range and right.is_entire_range
  left_size = left.left_size
  right_size = right.right_size
  
  if mylist[mid-1] == key and mylist[mid] == key:
    middle = left.right_size + right.left_size
  else:
    middle = 0
    
  if left.is_entire_range:
    left_size += right.left_size
  if right.is_entire_range:
    right_size += left.right_size

  longest_run = max(left.longest_size, right.longest_size, middle)

  return Result(left_size, right_size, longest_run, is_entire_range)

  
test=[1,2,2,4,4,4,6,6,3,3,4,4,7,7,9,3,3,3,3,2,2,1,3,3,5]    
print(longest_run_recursive(test,3))


