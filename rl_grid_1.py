import random

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

  def update_path(self,direction):
    self.path.append(direction)
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

horiz_limit=7
vert_limit=7

def generate_rand_path():
  initial_path = []
  test = agent(horiz_limit,vert_limit)
  test.form_grid()
  test.start_pos()
  test.generate_reward()
  test.show_grid()
  done = test.check()
  while done != 1:
    test.generate_legal_moves()
    a = test.generate_rand_move()
    initial_path.append(a)
    test.move(a)
    test.show_grid()
    path = test.update_path(a)
    path_len = test.update_path_length()
    done = test.check()
  return initial_path

epsilon = 0.2
initial_path = generate_rand_path()
iterations = 1000

def path_optimizer(x,epsilon):
  
  best = x
  current_path = []
  test = agent(horiz_limit,vert_limit)
  test.form_grid()
  test.start_pos()
  test.generate_reward()
  test.show_grid()
  for i in best:
    threshold = random.random()
    print(threshold)
    if threshold<= epsilon: #take a rand exploration step
      done = test.check()
      while done != 1: 
        print('making random move')
        test.generate_legal_moves()
        a = test.generate_rand_move()
        initial_path.append(a)
        test.move(a)
        test.show_grid()
        path = test.update_path(a)
        path_len = test.update_path_length()
        current_path.append(a)
        done = test.check()
        print('path length:')
        print(str(len(current_path)))
        print('path:')
        print(current_path)
      if len(current_path) < len(best):
        return current_path
      else:
        return best 
        
        
    else:  
      print('making move previously known')
      test.move(i)
      test.show_grid()
      path = test.update_path(i)
      current_path.append(i)
      path_len = test.update_path_length()
      done = test.check()
  return current_path

def run(old,iterations):
  best = old
  for i in range(iterations):
    new_path = path_optimizer(initial_path,0.05)
    if len(new_path) < len(best):
      best = new_path
  return best

trial = run(initial_path,1000)

print(trial)
print(str(len(trial)))

