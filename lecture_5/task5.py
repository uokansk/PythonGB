link = 'https://docs.python.org/3/faq/programming.html'

prefix, *a, suffix = link.split('/')
print(f'({prefix},{a},{suffix})')
