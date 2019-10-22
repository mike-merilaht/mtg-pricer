rules = {
  'red': 4,
  'yellow': 7
}
  
def parseOutput(number, ruleDict):
  out = ''
  for name, value in ruleDict.items():
    if i % value == 0:
      out += name
  return out

print('Over engineered fizz buzz')
print('Rules')
print(rules)
for i in range(1, 101):
  out = parseOutput(i, rules)
  if out.__len__() == 0:
    out = i
  print(out)