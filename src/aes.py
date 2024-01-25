def encrypt():
  import datetime  


  # this initialization to replace hex characters with their numbers which used in s-box

  A, B, C, D, E, F = 10, 11, 12, 13, 14, 15


  """ this initialization for empty list is used to store the numbers as separated elements
  from the string of time and date which produced from the called method (datetime.now())
  which called from the imported module (datetime). """

  x = []


  # this initialization to make list to store the changes in the round key of the cipher

  roundKey = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]


  # this initialization to store the matrix numbers of the multiplier which used to mix columns of a matrix

  mix = [[2, 3, 1, 1],
         [1, 2, 3, 1],
         [1, 1, 2, 3],
         [3, 1, 1, 2]]


  # this initialization to store the key of the cipher

  key = [[1, 0, 0, 0],
         [6, 7, 3, 3],
         [6, 7, 3, 4],
         [4, 7, 9, 5]]

  ################################################################################################################

  """this initialization to store the string of time and date which produced from 
  the called method (datetime.now()) which called from the imported module (datetime)."""

  currenTime = datetime.datetime.now()


  #this initialization to split the datetime string to 2 strings

  ti = str(currenTime).split() 


  #this function is used to get time & date as separated numbers

  def getTime(x): 
     for i in range(0, 2):
         for j in range(len(ti[i])):
             if ti[i][j] != ":" and ti[i][j] != "." and ti[i][j] != "-":
                 x.append(int(ti[i][j]))
     return x

  t = getTime(x)        
          

  """this initialization to store the desired numbers from the string of time and date
  like this 2020-11-23 16:11:44.729304, we will take the 2 0, 1 1, 2 3, 1 6, 1 1, 4 4, 7 2 9 3"""

  plainText = [[t[17], t[14], t[13], t[12]],
               [t[6], t[7], t[8], t[9]],
               [t[10], t[11], t[5], t[4]],
               [t[3], t[15], t[16], t[2]]]


  #this initialization to store the data of the substitution box table

  sbox = [[(6, 3), (7, C), (7, 7), (7, B), (F, 2), (6, B), (6, F), (C, 5),
           (3, 0), (0, 1), (6, 7), (2, B), (F, E), (D, 7), (A, B), (7, 6)],
          [(C, A), (8, 2), (C, 9), (7, D), (F, A), (5, 9), (4, 7), (F, 0),
           (A, D), (D, 4), (A, 2), (A, F), (9, C), (A, 4), (7, 2), (C, 0)],
          [(B, 7), (F, D), (9, 3), (2, 6), (3, 6), (3, F), (F, 7), (C, C),
           (3, 4), (A, 5), (E, 5), (F, 1), (7, 1), (D, 8), (3, 1), (1, 5)],
          [(0, 4), (C, 7), (2, 3), (C, 3), (1, 8), (9, 6), (0, 5), (9, A),
           (0, 7), (1, 2), (8, 0), (E, 2), (E, B), (2, 7), (B, 2), (7, 5)],
          [(0, 9), (8, 3), (2, C), (1, A), (1, B), (6, E), (5, A), (A, 0),
           (5, 2), (3, B), (D, 6), (B, 3), (2, 9), (E, 3), (2, F), (8, 4)],
          [(5, 3), (D, 1), (0, 0), (E, D), (2, 0), (F, C), (B, 1), (5, B),
           (6, A), (C, B), (B, E), (3, 9), (4, A), (4, C), (5, 8), (C, F)],
          [(D, 0), (E, F), (A, A), (F, B), (4, 3), (4, D), (3, 3), (8, 5),
           (4, 5), (F, 9), (0, 2), (7, F), (5, 0), (3, C), (9, F), (A, 8)],
          [(5, 1), (A, 3), (4, 0), (8, F), (9, 2), (9, D), (3, 8), (F, 5),
           (B, C), (B, 6), (D, A), (2, 1), (1, 0), (F, F), (F, 3), (D, 2)],
          [(C, D), (0, C), (1, 3), (E, C), (5, F), (9, 7), (4, 4), (1, 7),
           (C, 4), (A, 7), (7, E), (3, D), (6, 4), (5, D), (1, 9), (7, 3)],
          [(6, 0), (8, 1), (4, F), (D, C), (2, 2), (2, A), (9, 0), (8, 8),
           (4, 6), (E, E), (B, 8), (1, 4), (D, E), (5, E), (0, B), (D, B)],
          [(E, 0), (3, 2), (3, A), (0, A), (4, 9), (0, 6), (2, 4), (5, C),
           (C, 2), (D, 3), (A, C), (6, 2), (9, 1), (9, 5), (E, 4), (7, 9)],
          [(E, 7), (C, 8), (3, 7), (6, D), (8, D), (D, 5), (4, E), (A, 9),
           (6, C), (5, 6), (F, 4), (E, A), (6, 5), (7, A), (A, E), (0, 8)],
          [(B, A), (7, 8), (2, 5), (2, E), (1, C), (A, 6), (B, 4), (C, 6),
           (E, 8), (D, D), (7, 4), (1, F), (4, B), (B, D), (8, B), (8, A)],
          [(7, 0), (3, E), (B, 5), (6, 6), (4, 8), (0, 3), (F, 6), (0, E),
           (6, 1), (3, 5), (5, 7), (B, 9), (8, 6), (C, 1), (1, D), (9, E)],
          [(E, 1), (F, 8), (9, 8), (1, 1), (6, 9), (D, 9), (8, E), (9, 4),
           (9, B), (1, E), (8, 7), (E, 9), (C, E), (5, 5), (2, 8), (D, F)],
          [(8, C), (A, 1), (8, 9), (0, D), (B, F), (E, 6), (4, 2), (6, 8),
         (4, 1), (9, 9), (2, D), (0, F), (B, 0), (5, 4), (B, B), (1, 6)]]
          
  ################################################################################################################
   
  #this function is used to test the output of matrices by printing them
          
  def matrixPrint(X):
      for r in X:
         print(r)
         
         
  #this function is used to xor two matrices
         
  def xor(x, y, result):
      for i in range(4):
         for j in range(4):
             result[i][j] = x[i][j] ^ y[i][j]
      return result
             
           
  #this function is used to substitute the elements of the round key with numbers from the s-box
      
  def sub(result):   
      for i in range(4):
          for j in range(0, 3, 2):
              result[i][j] = sbox[result[i][j]][result[i][j + 1]][0]
              result[i][j + 1] = sbox[result[i][j]][result[i][j + 1]][1]
      return result
              
              
  """this function is used to make shift by rows for the round key as we put the first element, we will shift 
  into a temp variable then the other elements overwrite the next element with their values"""

  def shift(result): 
      for i in range(1, 4):
          for n in range(i):
              temp = result[i][3]
              for j in range(4):
                  result[i][j - 1] = result[i][j]
              result[i][2] = temp 
      return result


  """this function is used to mix columns by multiply the round key within the special marrix 'mix' 
  and get the product of this operation then store it as the new plaintext"""

  def mixColms(result):
      out = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
      # iterate through rows of X
      for i in range(4):
         # iterate through columns of Y
         for j in range(4):
             # iterate through rows of Y
             for k in range(4):
                 out[i][j] += mix[i][k] * result[k][j]
      return out


  #this function is used to get the bit of a number and ignore the rest of it
      
  def rBit(result):   
      for i in range(4):
          for j in range(4):
              result[i][j] %= 10
      return result
              

  #this function is used to transform the matrix of the cipher text into a string  
            
  def getNum(k):
      x = ""
      for i in range(4):
          for j in range(4):
              x += str(k[i][j])
      return x


  def main():
      b = []
      k = xor(plainText, key, roundKey)
      for i in range(9):
          s = sub(k)
          sft = shift(s)
          mx = mixColms(sft)
          k = xor(mx, key, roundKey)
          b = rBit(k)
              
      s = sub(b)
      sft = shift(s)
      k = xor(sft, key, roundKey)
      b = rBit(k)
      return b

  roundKey = main()


  def encrypto():
      num = getNum(roundKey)
      return num
  return encrypto()
