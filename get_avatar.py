import urllib.request, re
html = urllib.request.urlopen('https://www.youtube.com/@emberandghee').read().decode('utf-8')
m = re.search(r'https://yt3\.(ggpht|googleusercontent)\.com/[^\"\'\\]+', html)
print(m.group(0) if m else 'None')
