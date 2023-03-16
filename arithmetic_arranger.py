def arithmetic_arranger(problems, answer = False):
  manyproblems = "Error: Too many problems."
  operatorError = "Error: Operator must be '+' or '-'."
  digitError = "Error: Numbers must only contain digits."
  limitError = "Error: Numbers cannot be more than four digits."
  arranged_problems = ""
  line1 = list()
  line2 = list()
  line3 = list()
  line4 = list()
  if len(problems) > 5:
    return manyproblems
  for seperated in problems:
    seper = seperated.split()
    try:
      num1 = int(seper[0])
      num2 = int(seper[2])
    except ValueError:
      return digitError
    if seper[1] == 'x' or seper[1] == '/':
        return operatorError
    elif len(seper[0]) > 4:
        return limitError
    elif len(seper[2]) > 4:
        return limitError
    elif len(seper[2]) > len(seper[0]) or len(seper[2]) == len(seper[0]):
      format1 = ""
      format2 = ""
      format3 = ""
      format4 = ""
      sum = ""
      count = 0
      format1 = seper[0].rjust(len(seper[2])+2)
      line1.append(format1)
      format2 = seper[1] + seper[2].rjust(len(seper[2])+1)
      line2.append(format2)
      while count < len(seper[2]) + 2:
        format3 = format3 + "-"
        count += 1
      line3.append(format3)
      if answer is True:
        if seper[1] == '+':
          sum = num1 + num2
        else:
          sum = num1 - num2
        format4 = str(sum).rjust(len(seper[2])+2)
        line4.append(format4)
    else:
      format1 = ""
      format2 = ""
      format3 = ""
      format4 = ""
      sum = ""
      count = 0
      format1 = seper[0].rjust(len(seper[0])+2)
      line1.append(format1)
      format2 = seper[1] + seper[2].rjust(len(seper[0])+1)
      line2.append(format2)
      while count < len(seper[0]) + 2:
        format3 = format3 + "-"
        count += 1
      line3.append(format3)
      if answer is True:
        if seper[1] == '+':
          sum = num1 + num2
        else:
          sum = num1 - num2
        format4 = str(sum).rjust(len(seper[0])+2)
        line4.append(format4)
  for lines in line1:
    arranged_problems = arranged_problems + lines + "    "
  arranged_problems = arranged_problems.rstrip()
  arranged_problems = arranged_problems + "\n"
  for lines2 in line2:
    arranged_problems = arranged_problems + lines2 + "    "
  arranged_problems = arranged_problems.rstrip()
  arranged_problems = arranged_problems + "\n"
  for lines3 in line3:
    arranged_problems = arranged_problems + lines3 + "    "
  arranged_problems = arranged_problems.rstrip()
  if answer is True:
    arranged_problems = arranged_problems + "\n"
    for lines4 in line4:
      arranged_problems = arranged_problems + lines4 + "    "
    arranged_problems = arranged_problems.rstrip()
  return arranged_problems
