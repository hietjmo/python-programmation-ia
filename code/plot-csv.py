
import csv
import matplotlib.pyplot as plt


csvfile = "freq-collection-1.csv"

ltrs = []
amount = []

with open (csvfile) as f:
  reader = csv.reader (f,delimiter='\t')
  for row in reader:
    ltrs.append (row [0].upper())
    amount.append (int (row [1]))

total = sum (amount)
ratios = [n / total for n in amount]

# x_pos = range (len (ltrs))

f = plt.figure (figsize=(5.66,2.5))
bars = plt.bar (
  x=ltrs, height=ratios, color=(1,1,1,0), linewidth=1.0, 
  edgecolor='black')

# Make some labels.
# labels = ["%d" % i for i in range(len(rects))]

# print (labels)
# https://matplotlib.org/3.1.1/gallery/ticks_and_spines/spine_placement_demo.html

for rect, label in zip (bars, ltrs):
  height = rect.get_height()
  x = rect.get_x() + rect.get_width() / 2
  y = height
  plt.text(x,y, label, ha='center', va='bottom')

#plt.xticks (x_pos, ltrs)
plt.tick_params (bottom=False,labelbottom=False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
f.savefig ("freq-collection-1.pdf", dpi=96, bbox_inches='tight')
plt.show ()



