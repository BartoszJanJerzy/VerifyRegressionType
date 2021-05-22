import base64

#zewnetrzny styl wizualny
external_stylesheets = [
    {
        'href': 'https://use.fontawesome.com/releases/v5.8.1/css/all.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf',
        'crossorigin': 'anonymous'
    },
    {
        'href': '"https://fonts.googleapis.com/css2?family=Spartan:wght@200&display=swap',
        'rel': 'stylesheet'
    },
]
# a ciemny: https://codepen.io/chriddyp/pen/LYpwVWm

# przygotowanie obrazu
background = r'background1.png'
encoded_background = base64.b64encode(open(background,"rb").read())

style_whole = {
    'width':1875,
    'height':930,
    'margin':'0px auto',
}

style_first = {
    'width':1875,
    'height':925,
    # 'border':'5px solid black',
    'background-image':f'url(data:image/png;base64,{encoded_background.decode()}'
}
style_second = {
    'width':1875,
    'height':925,

    # 'border':'5px solid black',
    'background-image': f'url(data:image/png;base64,{encoded_background.decode()}',

    'position':'relative',
    'color':'#46494C'
}


# ----------------------------------------
# UPLOAD
style_uplaod_page = {
    'text-align':'center',
    'padding-top':20,
    'color':'#46494C',
}

style_upload = {
    'width': '300px',
    'margin': '10px auto',
    'padding':'50px 100px',

    'border':'1px dashed black',
    'borderRadius': '5px',
}

# ----------------------------------------
# TABLE
style_verify = {
}

style_table = {
    'overflowX': 'auto',
    'overflowY': 'auto',
    'width': '1300px',
    'height': '250px',
    'margin':'0px auto',
    'box-shadow':'0px 0px 30px 0px rgba(29, 51, 84, 0.5)'
}

style_table_div = {
    'width':1300,
    'margin':'0px auto',
}

# ----------------------------------------
# DROPDOWN
style_dropdown_div = {
    'width':'350px',
    'position':'absolute',
    'top':75,
    'left':75,
    'padding': '5px 20px',
    # 'border':'1px solid red',
    'text-align':'left',
}
style_dropdown = {
    'width':'300px',
    'font-size':20,
}

# ----------------------------------------
# BUTTON

# ----------------------------------------
# RESULTS
style_select_subplot = {
    'width': '350px',
    'position':'absolute',
    'top':340,
    'left':75,
    'padding': '5px 20px',
    # 'border':'1px solid red',
    'text-align': 'left',
}

style_compared_r2 = {
    'width': '700px',
    'position':'absolute',
    'top':550,
    'left':75,
    'padding':'5px 20px',
    # 'border': '1px solid red',
    'text-align': 'left',
}

style_graph = {
    'position':'absolute',
    'top':75,
    'right':75,
    'box-shadow':'0px 0px 30px 0px rgba(35, 61, 77, 0.5)'
}

# ----------------------------------------
# HEADINGS
style_h1 = {'font-size':50}
style_h2 = {'font-size':30}
style_h3 = {'font-size':20}
style_comment = {'font-size':16, 'font-style':'italic'}
style_h4 = {'font-size':16,}

style_author = {
    'width':500,
    'color':'grey',
}