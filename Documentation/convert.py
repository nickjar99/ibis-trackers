

infile = "Documentation/tutorial.md"
outfile = "Documentation/tutorial2.md"

new_lines = []
with open(infile, "r") as f:
    lines = f.readlines()

# for line in lines:
#     if line.startswith("(") and line[-2:] == ")\n":
#         print([line])

#     else:
#         new_lines.append(line)

for i, line in enumerate(lines):
    if line.startswith("(") and line[-2:] == ")\n":
        print([line])
        content = line[1:-2]
        new_line = f"<img src=\"../Images/process/{content}\" width=\"400\">\n"
        new_lines.append(new_line)
        
        if i + 1 < len(lines) and lines[i+1].startswith("[") and lines[i+1][-2:] == "]\n":
            print([lines[i+1]])
            new_line = f"<sub>{lines[i+1][1:-2]}</sub>\n"
            new_lines.append(new_line)
            
    else:
        new_lines.append(line)

with open(outfile, "w") as f:
    f.writelines(new_lines)

print('Done!')