import os

with open('hello.js', 'w') as js:
    js.write("console.log('hello')")

js.close()

os.remove('hello.js')

