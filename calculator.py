
def tokenize(exp):
  operators = ["*" , "+", "-", "/", "%", "(", ")"]
  tokens = []
  number = ""
  for ch in exp:
    if ch.isdigit() or ch == ".":
      number+=ch
    elif ch in operators:
      if number != "":
        tokens.append(("operand", number))
        number = ""
      tokens.append(("operator", ch))
    elif ch == "=":
      compute(tokens)
    elif ch == " ":
      continue
    else:
      print("ERROR")
  if number != "":
    tokens.append(("operand", number))
    number = ""

  return tokens

def compute(tokens):
  values = []
  for type, op in tokens:
    if type == "operand":
      values.append(float(op))
    else:
      values.append(op)
  print(values)

  while "(" in values:
    c_ind = values.index(")")
    o_ind = c_ind
    while values[o_ind] != "(":
      o_ind -= 1

    inner_exp = values[o_ind + 1: c_ind]
    inner_exp_token = []

    for item in inner_exp:
        if isinstance(item, float):
            inner_exp_token.append(("operand", str(item)))
        else:
            inner_exp_token.append(("operator", item))
    inner_exp_result = compute(inner_exp_token)
    values[o_ind:c_ind + 1] = [inner_exp_result]
  

  i = 0
  while i < len(values):
    if values[i] == "*":
      result = values[i-1] * values[i+1]
      values[i-1:i+2] = [result]
      i = 0
    elif values[i] == "/":
      try:
        result = values[i-1] / values[i+1]
        values[i-1:i+2] = [result]
        i = 0
      except ZeroDivisionError:
        print("Division by 0 is not valid")

    elif values[i] == "%":
      result = values[i-1] % values[i+1]
      values[i-1:i+2] = [result]
      i = 0

    else :
      i += 1

  i = 0
  while i < len(values):
    if values[i] == "+":
      result = values[i-1] + values[i+1]
      values[i-1:i+2] = [result]
      i = 0
    elif values[i] == "-":
      result = values[i-1] - values[i+1]
      values[i-1:i+2] = [result]
      i = 0
    else :
      i += 1

  
  print(values[0])
  return values[0]
    