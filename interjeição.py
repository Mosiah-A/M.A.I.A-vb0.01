from random import uniform


inter = ['Oi', 'Ola', 'Eai', 'Ei', '']

r = int(uniform(0, 100))
if (r < 48):
    s = inter[0]
elif (r < 52 ):
    s = inter[1]
elif (r < 84):
    s = inter[2]
elif (r < 92):
    s = inter[3]
elif (r > 100):
    s = inter[4]
print('{} Eu sou M.A.I.A '.format(s))
