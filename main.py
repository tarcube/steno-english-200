import sys
import pygame
from pygame.locals import *
import json
pygame.init()
pygame.font.init()

fps = 60
fpsClock = pygame.time.Clock()
width, height = 400, 225
screen = pygame.display.set_mode((width, height))
timer = 0

steno = []
english = []

file = open('words.json')
words = json.load(file)
for i in words:
    steno.append(i)
    english.append(words.get(i))
file.close()

font = pygame.font.SysFont('Splatfont 2', 50)
running = False

def render_text():
  text = font.render(english[int(timer/500)], False, "#FFFFFF")
  screen.blit(text, (25, -10))
  text = font.render(steno[int(timer/500)], False, "#FFFFFF")
  screen.blit(text, (25, 65))
  render_board(steno[int(timer/500)]+" ")

def render_board(string):
  begin_s = pygame.Rect(160, 160, 15, 35)
  begin_t = pygame.Rect(180, 160, 15, 15)
  begin_p = pygame.Rect(200, 160, 15, 15)
  begin_h = pygame.Rect(220, 160, 15, 15)
  begin_k = pygame.Rect(180, 180, 15, 15)
  begin_w = pygame.Rect(200, 180, 15, 15)
  begin_r = pygame.Rect(220, 180, 15, 15)
  vowel_a = pygame.Rect(210, 200, 15, 15)
  vowel_o = pygame.Rect(230, 200, 15, 15)
  mid_ast = pygame.Rect(240, 160, 35, 35)
  vowel_e = pygame.Rect(270, 200, 15, 15)
  vowel_u = pygame.Rect(290, 200, 15, 15)
  end_f = pygame.Rect(280, 160, 15, 15)
  end_p = pygame.Rect(300, 160, 15, 15)
  end_l = pygame.Rect(320, 160, 15, 15)
  end_t = pygame.Rect(340, 160, 15, 15)
  end_d = pygame.Rect(360, 160, 15, 15)
  end_r = pygame.Rect(280, 180, 15, 15)
  end_b = pygame.Rect(300, 180, 15, 15)
  end_g = pygame.Rect(320, 180, 15, 15)
  end_s = pygame.Rect(340, 180, 15, 15)
  end_z = pygame.Rect(360, 180, 15, 15)
  #
  begin = ""
  end = ""
  for i in range(len(string)):
    if string[i] != "A" and string[i] != "O" and string[i] != "E" and string[i] != "U" and string[i] != "*" and string[i] != "-":
      begin += string[i]
    else:
      end += string[i+1:-1]
      break
  if "S" in begin: pygame.draw.rect(screen, "#FFFF00", begin_s)
  else: pygame.draw.rect(screen, "#808080", begin_s)
  if "T" in begin: pygame.draw.rect(screen, "#FFFF00", begin_t)
  else: pygame.draw.rect(screen, "#808080", begin_t)
  if "P" in begin: pygame.draw.rect(screen, "#FFFF00", begin_p)
  else: pygame.draw.rect(screen, "#808080", begin_p)
  if "H" in begin: pygame.draw.rect(screen, "#FFFF00", begin_h)
  else: pygame.draw.rect(screen, "#808080", begin_h)
  if "K" in begin: pygame.draw.rect(screen, "#FFFF00", begin_k)
  else: pygame.draw.rect(screen, "#808080", begin_k)
  if "W" in begin: pygame.draw.rect(screen, "#FFFF00", begin_w)
  else: pygame.draw.rect(screen, "#808080", begin_w)
  if "R" in begin: pygame.draw.rect(screen, "#FFFF00", begin_r)
  else: pygame.draw.rect(screen, "#808080", begin_r)
  if "A" in string: pygame.draw.rect(screen, "#FFFF00", vowel_a)
  else: pygame.draw.rect(screen, "#808080", vowel_a)
  if "O" in string: pygame.draw.rect(screen, "#FFFF00", vowel_o)
  else: pygame.draw.rect(screen, "#808080", vowel_o)
  if "*" in string: pygame.draw.rect(screen, "#FFFF00", mid_ast)
  else: pygame.draw.rect(screen, "#808080", mid_ast)
  if "E" in string: pygame.draw.rect(screen, "#FFFF00", vowel_e)
  else: pygame.draw.rect(screen, "#808080", vowel_e)
  if "U" in string: pygame.draw.rect(screen, "#FFFF00", vowel_u)
  else: pygame.draw.rect(screen, "#808080", vowel_u)
  if "F" in end: pygame.draw.rect(screen, "#FFFF00", end_f)
  else: pygame.draw.rect(screen, "#808080", end_f)
  if "P" in end: pygame.draw.rect(screen, "#FFFF00", end_p)
  else: pygame.draw.rect(screen, "#808080", end_p)
  if "L" in end: pygame.draw.rect(screen, "#FFFF00", end_l)
  else: pygame.draw.rect(screen, "#808080", end_l)
  if "T" in end: pygame.draw.rect(screen, "#FFFF00", end_t)
  else: pygame.draw.rect(screen, "#808080", end_t)
  if "D" in end: pygame.draw.rect(screen, "#FFFF00", end_d)
  else: pygame.draw.rect(screen, "#808080", end_d)
  if "R" in end: pygame.draw.rect(screen, "#FFFF00", end_r)
  else: pygame.draw.rect(screen, "#808080", end_r)
  if "B" in end: pygame.draw.rect(screen, "#FFFF00", end_b)
  else: pygame.draw.rect(screen, "#808080", end_b)
  if "G" in end: pygame.draw.rect(screen, "#FFFF00", end_g)
  else: pygame.draw.rect(screen, "#808080", end_g)
  if "S" in end: pygame.draw.rect(screen, "#FFFF00", end_s)
  else: pygame.draw.rect(screen, "#808080", end_s)
  if "Z" in end: pygame.draw.rect(screen, "#FFFF00", end_z)
  else: pygame.draw.rect(screen, "#808080", end_z)

while True:
  screen.fill("#804080")
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == KEYDOWN:
      running = True
  if running:
    timer += 2000/(fpsClock.get_fps()+1)
  render_text()
  pygame.display.flip()
  fpsClock.tick(fps)