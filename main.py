def read_input_file(filename):
    with open(filename,'r')as file:
        content = file.read()
    return content
def decode(word):
    result=''
    for letter in word:
        if letter=='+':
            result+=' '
            continue
        result+=letter
    return result


def genarate_html(content):
    html = '''<DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<meta name='viewport' content='width=device-width, inital-scale=1.0'>
<link rel="stylesheet" href="">
'''
    for word in content.split():
        if word.upper()=='PAGE':
            lastWord='PAGE'
            continue
        if word.upper()=='TITLE':
            lastWord='TITLE'
            continue
        if word=='=':
            if lastWord=='TITLE':
                equalLastWord='TITLE'
                continue
        if equalLastWord=="TITLE":
            lastWord=None
            equalLastWord=None
            html+=f'<title>{decode(word)}</title>\n'
            continue
        if word=='{':
            html+='</head>\n<body>\n'
            continue
        if word.upper()=='P':
            lastWord='P'
            continue
        if word.upper()=='PNG':
            lastWord='PNG'
            continue
        if lastWord=='P':
            html+=f'<p>{decode(word)}</p>\n'
            lastWord=None
            continue
        if lastWord=='PNG':
            html+=f'<img src="{decode(word)}.png">\n'
            lastWord=None
            continue
        if word=='}':
            html+='</body>'
            break
    return html

def write_output_file(html_content):
    with open("index.html","w") as file:
        file.write(html_content)