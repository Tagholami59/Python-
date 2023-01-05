while True:
    line = input('print this ')
    if line[0] == '# dont print this' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')
