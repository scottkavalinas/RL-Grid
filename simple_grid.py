import random

class agent():

  def __init__(self,horiz_limit,vert_limit):
    self.horiz_limit = horiz_limit
    self.vert_limit = vert_limit
    self.grid = []
    self.a = 'x'
    self.empty = '_'
    self.r = 'R'

  def form_grid(self):
    for i in range(vert_limit):
      self.grid.append([])
      for j in range(horiz_limit):
        self.grid[i].append('_')
    
  def start_pos(self):
    h = input('enter horizantal pos ')
    v = input('enter vertical pos ')
    self.horz = int(h)
    self.vert = int(v)
    self.pos = (self.vert,self.horz)
    self.grid[self.vert][self.horz] = self.a
    print(self.pos)
    
  def move(self,direction):
    if direction == 'up':
      self.grid[self.vert][self.horz] = self.empty
      self.horz = self.horz
      self.vert +=1
      self.grid[self.vert][self.horz] = self.a
      self.pos = (self.vert,self.horz)
      
    if direction == 'down':
      self.grid[self.vert][self.horz] = self.empty
      self.horz = self.horz
      self.vert -=1
      self.grid[self.vert][self.horz] = self.a
      self.pos = (self.vert,self.horz)
      
    if direction == 'right':
      self.grid[self.vert][self.horz] = self.empty
      self.vert = self.vert
      self.horz +=1
      self.grid[self.vert][self.horz] = self.a
      self.pos = (self.vert,self.horz)
      
    if direction == 'left':
      self.grid[self.vert][self.horz] = self.empty
      self.vert = self.vert
      self.horz -=1
      self.grid[self.vert][self.horz] = self.a
      self.pos = (self.vert,self.horz)
    print('current position' +str(self.pos))
    return self.pos

  def generate_reward(self,is_random):
    if is_random == 1:
      self.reward_horz = random.choice(range(self.horiz_limit))
      self.reward_vert = random.choice(range(self.vert_limit))
      self.grid[reward_vert-1][reward_horz-1] = self.r
      self.reward_pos = (self.reward_vert-1,self.reward_horz-1)
      print(self.reward_vert,self.reward_horz)
    else:
      self.reward_horz= self.horiz_limit
      self.reward_vert = self.vert_limit
      self.grid[self.reward_vert-1][self.reward_horz-1] = self.r
      self.reward_pos = (self.reward_vert-1,self.reward_horz-1)
      print(self.reward_pos)

  def generate_legal_moves(self):
      self.moves = []
      if self.pos[0]>0:
        self.moves.append('down')
      if self.pos[0]<self.vert_limit-1:
        self.moves.append('up')
      if self.pos[1]>0:
        self.moves.append('left')
      if self.pos[1]<self.horiz_limit-1:
        self.moves.append('right')
      print('legal moves: ' + str(self.moves))
  
  def generate_rand_move(self):
    move = random.choice(self.moves)
    print(move)
    return move
  
  def show_grid(self):
    for i in range(self.vert_limit):
      print('|{}|'.format(self.grid[i]))
    print()

  def check(self):
    if self.pos == self.reward_pos:
      print('reward has been found')
      return 1
    else:
      return 0

horiz_limit=4
vert_limit=4

test = agent(horiz_limit,vert_limit)
test.form_grid()
test.start_pos()
test.generate_reward(0)
test.show_grid()

done = test.check()
while done != 1:
  test.generate_legal_moves()
  a = test.generate_rand_move()
  test.move(a)
  test.show_grid()
  done = test.check()

