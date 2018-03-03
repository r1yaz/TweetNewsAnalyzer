# used to depict the vader sentiments via a pie chart for tweets

import matplotlib.pyplot as plot
import json

# reading each vader sentiment and appending into a list

dataText = []
with open("TextsVADER.json") as f:
	for line in f:
		dataText.append(json.loads(line))

# defining parameters

i = 0
values = ['positive', 'negative', 'neutral']
colors = ['g', 'r', 'b']

# displaying pie chart for each tweet

for line in dataText:
	a = dataText[i]['pos']
	b = dataText[i]['neg']
	c = dataText[i]['neu']
	slice = [a, b, c]
	plot.pie(slice, labels=values, colors=colors, startangle=90, radius=1, autopct='%1.1f%%', shadow=True)
	plot.legend()
	plot.title(i)
	plot.show()
	i = i+1

