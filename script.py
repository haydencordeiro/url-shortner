import os

links={
    "resume":"https://drive.google.com/file/d/1Sohx0qy4tHLIrBEXZ8vL7mi-Q0-5Cej4/view?usp=sharing",
    "meet":"https://meet.google.com/sac-kfod-ipt",
    "linkedin":"https://www.linkedin.com/in/haydencordeiro/",
    "github":"https://github.com/haydencordeiro",
    "marksheets":"https://drive.google.com/file/d/1A1NP0Xd0sWpnIBZtvLbMHG9M9Esxy-Kn/view?usp=sharing",
    "adharpanbirth":"https://drive.google.com/file/d/1sz1-alDLg6w6JeCylwSFR_MT5xDyrVEd/view?usp=sharing",
}


def createFileContent(url):
    
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Redirecting</title>
    <script>
        window.location.href="{}"
    </script>
    </head>
    <body>
        
    </body>
    </html>
    '''.format(url)

for k,v in links.items():
    f = open(f"{k}.html", "w")
    f.write(createFileContent(v))
    f.close()

os.system("git add .")
os.system('git commit -m "updated links"')
os.system("git push -f")

