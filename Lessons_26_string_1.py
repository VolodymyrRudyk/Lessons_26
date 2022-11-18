S = 'a+b+c'
x = S.replace('+', 'spam')
print(x)

print('That is %d %s bird!' % (1, 'dead'))      #вираження формату

exclamation = 'Ni'
print('The knights who say %s!' % exclamation)  #підстановка строки
print('%d %s %g you' % (1, 'spam', 4.0))        #підстановка, специфічні для типів
print('%s -- %s -- %s' % (42, 3.14159, [1,2,3]))#всі типи відповідають цілі %s

x = 1234
res = 'integers: ...%d...%-6d...%06d' % (x, x, x)
print(res)
x = 1.23456789
print(x)
print('%e | %f | %g' % (x, x, x))
print('%E' % x)

print('%-6.2f | %05.2f | %+06.1f' % (x, x, x))
print('%s' % x, str(x))
print('%f, %.2f, %.*f' % (1/3.0, 1/3.0, 4, 1/3.0))