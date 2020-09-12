import markovify


with open('LoremIpsum.txt') as f:
    text = f.read()

text_model = markovify.Text(text, state_size=3)

for i in range(18):
    print(text_model.make_short_sentence(500))

