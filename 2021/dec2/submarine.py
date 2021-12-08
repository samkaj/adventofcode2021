class Submarine():
  def __init__(self) -> None:
      self.x = 0
      self.y = 0
      self.aim = 0
      self.depth = 0
  
  def move(self, direction, delta):
    delta = int(delta)
    if direction == 'forward':
      self.forward(delta)
    elif direction == 'up':
      self.up(delta)
    elif direction == 'down':
      self.down(delta)

  def up(self, dy):
    self.y -= dy
    self.aim -= dy
  
  def down(self, dy):
    self.y += dy
    self.aim += dy 

  def forward(self, dx):
    self.x += dx
    self.depth += dx * self.aim

  
  def pos(self) -> tuple:
    return (self.x, self.y)
  
  def horizontal_depth_product(self) -> int:
    return self.depth * self.x

  def pos_product(self) -> int:
    pos = self.pos()
    return pos[0] * pos[1]