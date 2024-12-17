with open('input.txt', 'r') as f:
  r_inp = f.read()

inp = r_inp

##################################
# PART 1
##################################

robots = []
for l in inp.split("\n"):
  problem = []
  eq_split = l.split("=")
  
  p_split = eq_split[1].split(",")
  problem.append(int(p_split[0].strip()))
  problem.append(int(p_split[1].split(" ")[0].strip()))
  
  v_split = eq_split[2].split(",")
  problem.append(int(v_split[0].strip()))
  problem.append(int(v_split[1].strip()))
  
  robots.append(tuple(problem))


quad_counts = [[0, 0], [0, 0]]
for px, py, vx, vy in robots:
  xf, yf = (px + 100 * vx) % 101, (py + 100 * vy) % 103
  
  if xf == 50 or yf == 51:
    continue
  
  xq = 1 if xf < 50 else 0
  yq = 1 if yf < 51 else 0
  
  quad_counts[xq][yq] += 1
ans = quad_counts[0][0] * quad_counts[0][1] * quad_counts[1][0] * quad_counts[1][1]
print("PART 1:", ans)


##################################
# PART 2
##################################

# parse input
robots = []
for l in inp.split("\n"):
  problem = []
  eq_split = l.split("=")
  
  p_split = eq_split[1].split(",")
  problem.append(int(p_split[0].strip()))
  problem.append(int(p_split[1].split(" ")[0].strip()))
  
  v_split = eq_split[2].split(",")
  problem.append(int(v_split[0].strip()))
  problem.append(int(v_split[1].strip()))
  
  robots.append(tuple(problem))

for t in range(10000):
  
  # Find robots close to each other
  next_set = set()
  matching = set()
  for px, py, vx, vy in robots:
    xf, yf = (px + t * vx) % 101, (py + t * vy) % 103
    if (xf, yf) in next_set:
      matching.add((xf, yf))
    for dx in [-1, 0, 1]:
      for dy in [-1, 0, 1]:
        next_set.add((xf + dx, yf + dy))
        
  # print matching board
  if len(matching) > 256:
    for x in range(100):
      for y in range(101):
        if (x, y) in next_set:
          print("*", end="")
        else:
          print(".", end="")
      print("")
    print("t:", t)
    