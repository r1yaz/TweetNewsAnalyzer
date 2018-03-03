# used to plot a pie chart for the news sentiments

import matplotlib.pyplot as plot
import json

# reading each vader sentiment and appending into a list

dataNews = []
with open("NewsVADER.json") as fe:
	for line in fe:
		dataNews.append(json.loads(line))

# defining parameters

i = 0
values = ['positive', 'negative', 'neutral']
colors = ['g', 'r', 'b']

# displaying pie chart for each news

for line in dataNews:
	d = dataNews[i]['pos']
	e = dataNews[i]['neg']
	f = dataNews[i]['neu']
	slais = [d, e, f]
	plot.pie(slais, labels=values, colors=colors, startangle=90, radius=1, autopct='%1.1f%%')
	plot.legend()
	plot.title(i)
	plot.show()
	i = i+1


