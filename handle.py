import re 
import pprint
pp = pprint.PrettyPrinter(indent=4)

with open("transcript.txt", "r") as f:
  transcript = f.read()
  f.close()

participants = ["User", "ChatGPT"]
languages = ["javascript", "html", "css"]
ignore = ["Copy code"]

output = ""
lines = transcript.split("\n")
code = ""
coding = False
for line in lines:
  line = line.replace("<", "&lt;").replace(">", "&gt;")
  if line in ignore:
    continue
  if line in participants:
    output += ("<h3>"+line+"</h3>")
  elif line in languages:
    if (coding):
      output += "</pre>"
    output += ("<h4>"+line+"</h4>")
    output += ("<pre class='code'>")
    print("------ [ CODE --------------")
    coding = line
  else:
    if (coding and (len(line)>120)):
      print("------ / CODE ]-------------")
      coding = False
      output += ("</pre>")
    print(len(line), line)
    if (coding):
      output += (line+"<br />")
    else:
      output += (line+"\n")


with open("template.html", "r") as f:
  template = f.read()
  output = template.replace("{{content}}", output)
  f.close()
  with open("index.html", "w+") as ff:
    ff.write(output)
    ff.close()

print(output)