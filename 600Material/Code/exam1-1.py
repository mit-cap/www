
words  = ['arc', 'boat', 'falter', 'gadget', 'gangrene', 'java', 'keratin', 'lantern', 'morbid', 'nullify', 'out', 'question', 'rough', 'staid', 'use', 'van', 'waffle', 'xylene', 'yodeler', 'zymology']

def find1(words, target):
   for x in words:
        if x == target:
              return True
   return False

def find2(words, target):
     pos = len(words)/2
     if(words[pos] > target):
        return find2(words[pos:len(words)], target)
     else:
        return find2(words[0:pos], target)

def find3(words, target):
      low = 0;
      high = len(words)
      while( low < high):
        pos = (low + high)/2
        if (words[pos] > target):
                high = pos
        if( words[pos]< target):
                low = pos + 1
        if( words[pos] ==target):
                return True
      return False
