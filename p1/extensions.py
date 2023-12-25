## File Extensions
from helper import test

def main():
    user_input = input("File name: ")
    print(extensions(user_input))

def extensions(file_name):
  file_name_clean = file_name.strip().lower()

  suffix = file_name_clean.split(".")[-1]

  match suffix:
     case "jpg" :
        return "image/jpeg"
     case "gif" | "jpeg" | "png":
        return f"image/{suffix}"
     case "pdf" | "zip":
        return f"application/{suffix}"
     case "txt":
        return f"text/{suffix}"
     case _:
        return "application/octet-stream"

# Run test
success = test(extensions, ["happy.jpg", "document.pdf", "", "mario.png", "recover.zip"], ["image/jpeg", "application/pdf", "application/octet-stream", "image/png", "application/zip"])

# Run main if test was successful
if success:
  main()