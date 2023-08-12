import pyshorteners

link = input("Enter the link here: ")
shortner = pyshorteners.Shortener()

x = shortner.tinyurl.short(link)

print(x)