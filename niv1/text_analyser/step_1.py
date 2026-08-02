text = """Hello world.
Hello Python.
Hello code.
This is a test.
Testing one two three."""

words = text.split()
lines = text.split('\n')

print(f'Words: {len(words)}\nLines: {len(lines)}\nCharacters: {len(text)}')
