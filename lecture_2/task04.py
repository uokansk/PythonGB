# txt = 'Hello world!'
# txt[5] = '_'


txt = 'Hello world!'
print(txt, id(txt))
txt = txt.replace(' ', '_')
print(txt, id(txt))

