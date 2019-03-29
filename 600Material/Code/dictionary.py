D = { 'are': 'estas',
        'car': 'coche',
        'dog':'perro',
        'hello':'hola',
        'how':'como',   
    'is' : 'es',
   'the' : 'el',      
    'yellow': 'amarillo',
    'you' : 'tu'
}

x = ("the dog is yellow").split()

result =''
for word in x:
    result = result + D[word] + ' '

print result
