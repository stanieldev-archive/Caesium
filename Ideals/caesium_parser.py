





def remove_comments():
    pass











with open("example.ce", "r") as file:
    content = [line.strip() for line in file]


content = [i for i in content if i != ""]


content_str = "\n".join(content)

print(content_str)