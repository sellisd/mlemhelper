import click

levels ={
  1:['b','1','2'],
  2:['b','1','3'],
  3:['b','2','3'],
  4:['1','4'],
  5:['b','1','2'],
  6:['1','2','4'],
  7:['1','2'],
  8:['1','3'],
  9:['2','4'],
  10:['1','3','4'],
  11:['b','1'],
  12:['b','3'],
  13:['1','2'],
  14:['3','4'],
  15:['b','1'],
  16:['1','2','3'],
  17:['2','3','4'],
  18:['b','1','4'],
  19:['b','1'],
  20:['2','3'],
  21:['b','2'],
  22:['b','4'],
  23:['b','3'],
  24:['b','2'],
  25:['b','1']
}

def level_profile_to_counts(roll:list):
  doubles = 0
  numbers = 0
  for i in roll:
    if i == '2':
      doubles +=1
    else:
      numbers +=1
  return {'doubles':doubles,'numbers':numbers}

@click.command()
@click.argument('level', required=True, type=int)
@click.argument('roll', required=True, type=int)
def should_i(level, roll):
  """Should I get off?

  Args:
      level (int): Game level
      roll (int): Number of dice available
  """
  result = Pcrash(level_profile_to_counts(levels[level]), roll)
  click.echo(f"The probability of crashing is {result:.2f}%.")

def Pcrash(count, dice_number):
    numbers = count['numbers']
    doubles = count['doubles']
    return 100 * ((1 - 1/6)**numbers * (1 - 1/3)**doubles)**dice_number
