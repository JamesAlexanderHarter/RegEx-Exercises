import re

#https://regex.sketchengine.co.uk/cgi/ex4.cgi

txt = [
#Positive:
"assumes word senses. Within",
"does the clustering. In the",
"but when? It was hard to tell",
"he arrive.\" After she had",
"mess! He did not let it",
"it wasn't hers!' She replied",
"always thought so.) Then",
#Negative:
"in the U.S.A., people often",
"John?\", he often thought, but",
"weighed 17.5 grams",
"well ... they'd better not",
"A.I. has long been a very",
"like that\", he thought",
"but W. G. Grace never had much"]

for x in txt:
    matches = re.findall("", x)
    print(matches)