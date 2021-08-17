import os

links={
    "resume":"https://drive.google.com/file/d/1TCgEaAQdyZ9icV2uduWvFi6G7mk7thI5/view?usp=sharing",
    "meet":"https://meet.google.com/sac-kfod-ipt",
    "linkedin":"https://www.linkedin.com/in/haydencordeiro/",
    "github":"https://github.com/haydencordeiro",
    "marksheets":"https://drive.google.com/file/d/1A1NP0Xd0sWpnIBZtvLbMHG9M9Esxy-Kn/view?usp=sharing",
    "adharpanbirth":"https://drive.google.com/file/d/1sz1-alDLg6w6JeCylwSFR_MT5xDyrVEd/view?usp=sharing",
    "pinelabs":"https://drive.google.com/file/d/1qb4B0LaH26OoS26k_7da5XcydmCOlktM/view?usp=sharing",
    "nss":"https://drive.google.com/file/d/116l58Woj2uwf8ARL7u7yN0BwKA4dR2D9/view?usp=sharing",
    "tpc":"https://drive.google.com/file/d/1wg6CSQMSbBcIByR1RKA3XM_P4Yaj6NmX/view?usp=sharing",
    "yif":"https://drive.google.com/file/d/1qmw0kzT3zaDIO-VbdO80U4PbMT5GvM9m/view?usp=sharing",
    "teknack2021":"https://drive.google.com/file/d/1M5l1H28-eCANaCmfDHKw_zz9jKE_1fPS/view?usp=sharing",
    "teknack2020":"https://drive.google.com/file/d/1_h0LNVKDclN4B73DllhZqRlVS_iTnE20/view?usp=sharing",
    "dsip":"https://meet.google.com/obk-kjzx-ago",
    "assdf":"https://us02web.zoom.us/j/7487113416?pwd=NXdUYVpXdGdnY3lMbkhHZjFyYm5vZz09",
    "assdfrec":"https://mega.nz/folder/bKBEBDKR#7-I6nZdMl9xzzjkYrZVH3g",
    "zoom":"https://us04web.zoom.us/j/7661382898?pwd=Z01xa05kcE9OR2ZVKzFEUDZZWWFXZz09",
    "csl":"https://us04web.zoom.us/j/5434127356?pwd=eDBCaDRZbHdoaDRteHo2b1V5djFYdz09",
    "sem7":"https://mega.nz/folder/PawUALSY#XudA6PFfm34RqRYavnz-yg",
    "sem72":"https://drive.google.com/drive/folders/1MkhH6xJ3ug_Fo7cKsFL-WECCBAVhgEVQ"
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
    if k not in ["assdf","404"]:
        print(k)
        f = open(f"{k}.html", "w")
        f.write(createFileContent(k,v))
        f.close()

os.system("git add .")
os.system('git commit -m "updated links"')
os.system("git push -f")



    