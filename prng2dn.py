#!/usr/bin/env python

from sys import argv
def parse(filename, input, ind1, ind2):
  output = [[],[]]
  with open(filename, 'r') as f:
    for line in f:
      linelist = line.split(',')
      if type(input) == str:
        if linelist[ind1] == '\'' + input + '\'':
          output[0].append(linelist[ind2])
      else:
        for item in input[0]:
          if linelist[ind1] == item:
            output[0].append(linelist[ind2])
            output[1].append(linelist[ind1+1])
  return output

group = parse('group_member.dat', argv[1], 3, 1)
subscriber = parse('subscriber.dat', group, 35, 1)
status = subscriber[1]
dn = parse('subs_dn_sn_conv.dat', subscriber, 1, 3)

for index in range(len(status)):
  dn[1][index] = status[index]

for i in range(len(dn[0])):
  print(dn[0][i][1:-1] + ' ' + dn[1][i][1:-1])
