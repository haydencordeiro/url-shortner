import os

links={
    "resume":"https://drive.google.com/file/d/1TCgEaAQdyZ9icV2uduWvFi6G7mk7thI5/view?usp=sharing",
    "linkedin":"https://www.linkedin.com/in/haydencordeiro/",
    "github":"https://github.com/haydencordeiro",
    "cert":"https://drive.google.com/drive/folders/1w0mwb4AjFmX9Vk-_lQLk_F1lB1kBkPzC?usp=sharing",
    "certificates":"https://drive.google.com/drive/folders/1w0mwb4AjFmX9Vk-_lQLk_F1lB1kBkPzC?usp=sharing",
    "marksheets":"https://drive.google.com/file/d/1A1NP0Xd0sWpnIBZtvLbMHG9M9Esxy-Kn/view?usp=sharing",
    "adharpanbirth":"https://drive.google.com/file/d/1sz1-alDLg6w6JeCylwSFR_MT5xDyrVEd/view?usp=sharing",
    "assdfrec":"https://mega.nz/folder/bKBEBDKR#7-I6nZdMl9xzzjkYrZVH3g",
    "sem7":"https://mega.nz/folder/PawUALSY#XudA6PFfm34RqRYavnz-yg",
    "sem72":"https://drive.google.com/drive/folders/1MkhH6xJ3ug_Fo7cKsFL-WECCBAVhgEVQ",
    "zenscape":"https://play.google.com/store/apps/details?id=com.Teknack.Zenscape&hl=en_IN&gl=US",
    "gre":"https://mega.nz/folder/6bRCVZyK#fJ0wI9IUUP2p3Ypgtsmcdg",
    "ielts":"https://mega.nz/folder/DfIgkDLA#7st_w2l6QKSiyj8m1Zi6JQ",
    "meet":"https://meet.google.com/sac-kfod-ipt",
    "zoom":"https://us04web.zoom.us/j/7661382898?pwd=Z01xa05kcE9OR2ZVKzFEUDZZWWFXZz09"

}


def createFileContent(name,url):
    analytics=""" 
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-Y1TDP7H5C6"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
    
        gtag('config', 'G-Y1TDP7H5C6');
        </script>
    
    """
    
    return analytics+'''

 
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Redirecting to {}</title>
    <script>
        window.location.href="{}"
    </script>
    </head>
    <body>
        
    </body>
    </html>
    '''.format(name,url)

for k,v in links.items():
    if k not in ["404"]:
        print(k)
        f = open(f"{k}.html", "w")
        f.write(createFileContent(k,v))
        f.close()

os.system("git add .")
os.system('git commit -m "updated links"')
os.system("git push -f")



    