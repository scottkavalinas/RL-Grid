import random

# Function to do insertion sort https://www.geeksforgeeks.org/insertion-sort/
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
  for i in range(1, len(arr)): 
  
    key = arr[i]
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
    j = i-1
    while j >= 0 and key[0] < arr[j][0] : 
      arr[j + 1] = arr[j] 
      j -= 1
    arr[j + 1] = key 

class agent():

  def __init__(self,horiz_limit,vert_limit):
    self.horiz_limit = horiz_limit
    self.vert_limit = vert_limit
    self.grid = []
    self.a = 'x'
    self.empty = '_'
    self.r = 'R'
    self.path = []
    

  def form_grid(self):
    for i in range(vert_limit):
      self.grid.append([])
      for j in range(horiz_limit):
        self.grid[i].append('_')
    
  def start_pos(self):
    self.horz = int(0)
    self.vert = int(0)
    self.pos = (self.vert,self.horz)
    self.grid[self.vert][self.horz] = self.a
    print(self.pos)
    
  def move(self,direction):
    if direction == 'u':
      self.grid[self.vert][self.horz] = self.empty
      self.horz = self.horz
      self.vert +=1
      self.grid[self.vert][self.horz] = self.a
      self.pos = (self.vert,self.horz)
      
    if direction == 'd':
      self.grid[self.vert][self.horz] = self.empty
      self.horz = self.horz
      self.vert -=1
      self.grid[self.vert][self.horz] = self.a
      self.pos = (self.vert,self.horz)
      
    if direction == 'r':
      self.grid[self.vert][self.horz] = self.empty
      self.vert = self.vert
      self.horz +=1
      self.grid[self.vert][self.horz] = self.a
      self.pos = (self.vert,self.horz)
      
    if direction == 'l':
      self.grid[self.vert][self.horz] = self.empty
      self.vert = self.vert
      self.horz -=1
      self.grid[self.vert][self.horz] = self.a
      self.pos = (self.vert,self.horz)
    print('current position' +str(self.pos))
    return self.pos

  def generate_reward(self):
    self.reward_horz= self.horiz_limit
    self.reward_vert = self.vert_limit
    self.grid[self.reward_vert-1][self.reward_horz-1] = self.r
    self.reward_pos = (self.reward_vert-1,self.reward_horz-1)
    print(self.reward_pos)

  def generate_legal_moves(self):
      self.moves = []
      if self.pos[0]>0:
        self.moves.append('d')
      if self.pos[0]<self.vert_limit-1:
        self.moves.append('u')
      if self.pos[1]>0:
        self.moves.append('l')
      if self.pos[1]<self.horiz_limit-1:
        self.moves.append('r')
      print('legal moves: ' + str(self.moves))
  
  def generate_rand_move(self):
    self.rand_move = random.choice(self.moves)
    print(self.rand_move)
    return self.rand_move
  
  def show_grid(self):
    for i in range(self.vert_limit):
      print('|{}|'.format(self.grid[i]))
    print()

  def update_path(self):
    self.path.append(self.rand_move)
    return self.path

  def update_path_length(self):
    self.path_length = len(self.path)
    print('length of current path: '+ str(self.path_length))
    return self.path_length

  def check(self):
    if self.pos == self.reward_pos:
      print('reward has been found')
      return 1
    else:
      return 0

horiz_limit=4
vert_limit=4

paths_taken = []
iterations = 0

for i in range(0,100):
  test = agent(horiz_limit,vert_limit)
  test.form_grid()
  test.start_pos()
  test.generate_reward()
  test.show_grid()
  done = test.check()
  while done != 1:
    test.generate_legal_moves()
    a = test.generate_rand_move()
    test.move(a)
    test.show_grid()
    path = test.update_path()
    path_len = test.update_path_length()
    done = test.check()
  paths_taken.append([path_len,path])
  iterations +=1
print('after ' +str(iterations)+' iterations the paths taken were \n: ')
for i in paths_taken:
  print('path ' +'length ' + str(i[0]))
  print('path taken ' + str(i[1]))

insertionSort(paths_taken)
print('shortest path length:')
print(paths_taken[0][0])
print('path:')
print(paths_taken[0][1])



