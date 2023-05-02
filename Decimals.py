import numpy as np
#import functools

# unfinished / w.i.p
# only does addition
class Decimals:
  """
  Decimals class for floating-point operations.
  Implement as dec = Decimals("3.4")
  Operate as newdec = dec + otherdec
  """

  def __init__(self, n):
    self.value = str(n)

  def __str__(self):
    return self.value

  # the __add__ magic method allows for + operator overloading, so this is what happens when you do + 
  def __add__(self, other):
    self.checkInstance(other)
    return Decimals(self.additionDecimals(other))

  def __sub__(self, other):
    self.checkInstance(other)
    return Decimals(self.subtractionDecimals(other))

  def additionDecimals(self, other):
    """
    combineDecimals (only?) performs addition.
    """

    print("New Decimals operation\n")

    
    # makes numpy arrays of the unpacked value strings
    s = np.array([*self.value])
    o = np.array([*other.value])

    # numpy function to find all indices of all '.' occurences. maybe unnecessary
    si = np.where(s == '.')
    oi = np.where(o == '.')

    #print(si, oi)

    # lists for holding the resulting numbers their components, either before or after the dot
    valuesdot = [] # 00.
    dotvalues = [] # .00
  
    # if xi[0] holds anything ('.' is found), separates whole and decimal values into two lists
    # slicing is used with a stop parameter with the number of the index the '.' has. `si` is a tuple with with a nested numpy array storing the index
    # .shape is similar to len() but for numpy arrays
    print("\nself")
    if len(si[0]):
      sb = s[:si[0][0]]
      sa = [s[i] for i in range(si[0][0]+1, s.shape[0])]
      valuesdot.append("".join(sb))
      dotvalues.append("".join(sa))
      print(sb,'.',sa) 
    else:
      valuesdot.append("".join(s))
      print(valuesdot[0],'.')
      
    print("\nother")
    if len(oi[0]):
      ob = o[:oi[0][0]]
      oa = [o[i] for i in range(oi[0][0]+1, o.shape[0])]
      valuesdot.append("".join(ob))
      dotvalues.append("".join(oa))
      print(ob,'.',oa)
    else:
      valuesdot.append("".join(o))
      print(valuesdot[1],'.')

    # if any of the dotvalues indices do not match the length of index [0], meaning not all indices are of the same length, execute code that adds zeros to the shorter indices
    #! or, remove overflowing indices and add at the end, no calculation has to be performed on them anyway (implemented in other Decimals replit)
    #! '12' and '345', '5' overflows, pop that, do the maths on '12' and '35', and reinsert '5' at the end
    if any(len(dotvalues[i]) != len(dotvalues[0]) for i in range(len(dotvalues))):

      print("\nadding zeroes to equalize lengths")

      longest = 0
      for decimal in dotvalues:
        if len(decimal) > longest:
          longest = len(decimal)

      for i in range(len(dotvalues)):
        length = len(dotvalues[i])
        if length < longest:
          for _ in range(longest-length):
            dotvalues[i] += '0'  

      print(dotvalues, "new\n")
    # else longest is just whatever the length of the first index is
    else: 
      print("\nsame length decimals, no extra zeroes needed\n")
      longest = len(dotvalues[0])

    # convert values before the dot and after the dot to new formats
    newwhole = sum([int(i) for i in valuesdot])
    newdec = [*str(sum([int(i) for i in dotvalues]))]

    print(newwhole,"newwhole")
    print(newdec,"newdec")
    
    # if the length of the new decimal list is longer than the longest (longest is 2 but len(newdec) is 3, slice the remainder off of newdec and add that to newwhole)
    # could be done easier probably since the 
    if len(newdec) > longest:
      newwhole += int("".join(newdec[:len(newdec)-longest]))
      newdec = newdec[len(newdec)-longest:]

    # finally, add everything together
    final_value = str(newwhole)
    final_value += "."
    final_value += "".join(newdec)

    print("End of Decimals operation\n")
    print("\nanswer from Decimals\n" + final_value)
    return final_value

 
  def subtractionDecimals(self, other):
    """
    For the - operator
    Poorly implemented so far 
    """
    # makes numpy arrays of the unpacked value strings
    s = np.array([*self.value])
    o = np.array([*other.value])

    # numpy function to find all indices of all '.' occurences. maybe unnecessary
    si = np.where(s == '.')
    oi = np.where(o == '.')

    #print(si, oi)

    # lists for holding the resulting numbers their components, either before or after the dot
    valuesdot = [] # 00.
    dotvalues = [] # .00
  
    # if xi[0] holds anything ('.' is found), separates whole and decimal values into two lists
    # slicing is used with a stop parameter with the number of the index the '.' has. `si` is a tuple with with a nested numpy array storing the index
    # .shape is similar to len() but for numpy arrays
    print("self")
    if len(si[0]):
      sb = s[:si[0][0]]
      sa = [s[i] for i in range(si[0][0]+1, s.shape[0])]
      valuesdot.append("".join(sb))
      dotvalues.append("".join(sa))
      print(sb,'.',sa) 
    else:
      valuesdot.append("".join(s))
      print(valuesdot[0],'.')
      
    print("other")
    if len(oi[0]):
      ob = o[:oi[0][0]]
      oa = [o[i] for i in range(oi[0][0]+1, o.shape[0])]
      valuesdot.append("".join(ob))
      dotvalues.append("".join(oa))
      print(ob,'.',oa)
    else:
      valuesdot.append("".join(o))
      print(valuesdot[1],'.')

    if not valuesdot:
      valuesdot[0] = "0"
      
    # if any of the dotvalues indices do not match the length of index [0], meaning not all indices are of the same length, execute code that adds zeros to the shorter indices
    #! or, remove overflowing indices and add at the end, no calculation has to be performed on them anyway
    #! '12' and '345', '5' overflows, pop and reinsert later
    if any(len(dotvalues[i]) != len(dotvalues[0]) for i in range(len(dotvalues))):

      longest = 0
      for decimal in dotvalues:
        if len(decimal) > longest:
          longest = len(decimal)

      for i in range(len(dotvalues)):
        length = len(dotvalues[i])
        if length < longest:
          for _ in range(longest-length):
            dotvalues[i] += '0'  

      print(dotvalues, "new")
    # else longest is just whatever the length of the first index is
    else: 
      longest = len(dotvalues[0])

    # convert values before the dot and after the dot to new formats
    newwhole = [int(valuesdot[0])-int(valuesdot[1])]
    newdec = [int(i) for i in dotvalues]

    print(newwhole,"newwhole")
    print(newdec,"newdec")

    
  def checkInstance(self, other):
    """
    Checks if other argument is also of Decimals
    Add int/float support
    Add (kw)args
    """
    if isinstance(other, Decimals):
      pass
   #elif isinstance(other, int)
    else:
      yield TypeError # obtuse?
    
