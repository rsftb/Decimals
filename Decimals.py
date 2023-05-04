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
    
















import numpy as np
#import itertools

#unfinished
#numpy vstack implementation
#single digit math implementation

#add:
#better "dotless" numbers support
#add minus haha
class Decimals:
  """
  Decimals class for floating-point operations.
  Implement as dec = Decimals(3.4)
  Operate as newdec = dec + otherdec
  """

  def __init__(self, n):
    self.value = str(n)

  def __str__(self):
    return self.value

  def __add__(self, other):

    self.checkInstance(other)  
    return Decimals(self.combineDecimals(other))

  def combineDecimals(self, other):
    """
    combineDecimals (only?) performs addition.
    Add (kw)args
    """

    # "a list but numpy"
    s = np.array([*self.value])
    o = np.array([*other.value])

    #if s[0] == '.':
      #s.insert(0, '0')
    #if o[0] == '.':
      #o.insert(0, '0')

    # finds the dot in the 
    si = np.where(s == '.')
    oi = np.where(o == '.')

    print("s>", s)
    print("o>", o)
    print("si>", si)
    print("oi>", oi)
    print("\n")
    
    valuesdot = [] # 00.
    dotvalues = [] # .00

    # maybe add a check if there's any number before the dot
    # if entering .72, python converts .72 to "0.72", which is okay
    # if entering ".72", it's just a string ".72" which gets unpacked without a zero later on
    # figure out if that matters though

    print("self")
    if len(si[0]):
      sb = "".join(s[:si[0][0]])
      sa = [s[i] for i in range(si[0][0]+1, s.shape[0])]
      valuesdot.append("".join(sb))
      dotvalues.append(sa)
      print(sb, sa) 
    else:
      valuesdot.append("".join(s))
      
    print("other")
    if len(oi[0]):
      ob = "".join(o[:oi[0][0]])
      oa = [o[i] for i in range(oi[0][0]+1, o.shape[0])]
      valuesdot.append("".join(ob))
      dotvalues.append(oa)
      print(ob, oa)
    else:
      valuesdot.append("".join(o))

    print("\n")
    print("valuesdot>", valuesdot)
    print("dotvalues>", dotvalues)
    print("\n")

    
    # addition goes number by number, only a self and other get processed at any time
    # no *args are needed luckily
    # appendix is defined here instead of down there
    
    appendix = []
    if any(len(dotvalues[0]) != len(dotvalues[1]) for i in range(len(dotvalues))):
      print("unequal length in dotvalues, take appendix")

      # finds longer and shorter length lists
      longest = max(len(lst) for lst in dotvalues)
      shortest = min(len(lst) for lst in dotvalues)

      # appendix holds the end piece of the decimal which is longer and doesn't get operated on either way, this gets appended in its whole to the end of the decimals at the very end
      for i, l in enumerate(dotvalues):
        if len(l) == longest:
          appendix.extend(l[shortest:])
          dotvalues[i] = dotvalues[i][:shortest]

      print("appendix>", appendix, "\n")

    else:
     print("equal length in dotvalues, good to go\n")

    # converts string numbers to integer values, easier for logic but conversions are alot either way
    # converting to int like this is faster than using a for loop apparently
    dotvalues = np.array(dotvalues)
    dotvalues = dotvalues.astype(int)

    # turns dotvalues into a vstack
    dotvalues = np.vstack(dotvalues)
    print("vstack\n", dotvalues, "\n")

    
    # working the vstack for an answer
    # calculate sum of a column, if bigger than 9, see how many times exactly and add to the result of the next column
    # doesn't seem to cycle more than once though, at most only a single 1 gets added to the whole numbers
    # maybe expand from singles to wholes
    dotanswer = []
    add = 0
    for i in range(1, len(dotvalues[0])+1):
      result = dotvalues[0][-i] + dotvalues[1][-i]

      if add:
        result += add

      cycles = 0
      while result > 9:
        result -= 10
        cycles += 1
        
      add = cycles        
      dotanswer.insert(0, result)

    if cycles:
      valuesdot.append(str(cycles))

    print("before final processing")
    print("valuesdot>", valuesdot)
    print("dotanswer>", dotanswer)
    if appendix:
      print("appendix>", appendix) 
    print("\n")
    
    answerdot = [str(sum(int(n) for n in valuesdot))]
    answerdot.append('.')
    dotanswer = [str(n) for n in dotanswer]
    
    if appendix:
      dotanswer.extend(appendix)
      
    answerdot.extend(dotanswer)
    
    print("after final processing")
    print("answer(dot)>", answerdot)
    print("dotanswer>", dotanswer)
    print("\n")

    
    final_answer = "".join(answerdot)

    print("answer from Decimals")
    print(final_answer)
    return final_answer
  
    
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
    
