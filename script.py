import os

links={
    "resume":"https://drive.google.com/file/d/1Rjd07Nazmr3-Je-kKLuH0X0ICTjbudtN/view?usp=sharing",
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
    "dsip":"meet.google.com/uvu-oftc-drf",
    "assdf":"https://us02web.zoom.us/j/7487113416?pwd=NXdUYVpXdGdnY3lMbkhHZjFyYm5vZz09"
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
    if k not in ["assdf"]:
        print(k)
        f = open(f"{k}.html", "w")
        f.write(createFileContent(v))
        f.close()

os.system("git add .")
os.system('git commit -m "updated links"')
os.system("git push -f")

