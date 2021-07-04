webData = {
    "header": '''<!DOCTYPE >
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title></title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="">
    </head>
    <body>''',
    "footer": '''<script src="" async defer></script>
    </body>
</html>'''
    }

nameList = ["header","footer"]

with open("final.html", "w+") as f:
    finalString = ""
    for k,v in webData.items():
        if(k in nameList):
            finalString+=v
    f.write(finalString)