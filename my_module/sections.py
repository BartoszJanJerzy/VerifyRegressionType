import dash_core_components as dcc
import dash_html_components as html

# biblioteka do tabel
import dash_table


#style
from my_module.style import style_h3, style_h4,style_graph,style_dropdown


# PODSTRONY
first_page = html.Div(id='first-page', children=[
    html.Div(id='headings-div', children=[
        html.H1(className='blue', children=['Hi, my dear  ', html.I(className='far fa-smile-beam')]),
        html.H2(children=[
            "Please, give me your data in ",
            html.Span(className='green', children="'.csv'"),
            html.Span(" or "),
            html.Span(className='green', children="'.xlsx'"),
            html.Span(" format.")
        ]),
        html.H2("I will show you what is the relation between chosen variables."),
        html.H2("Maybe, it has a curvilinear shape? Let's check it!"),
        html.H3(children=[
            html.I(className='fas fa-exclamation-triangle red'),
            " Remember - the bigger is your file, the longer I will work on it. ",
            html.I(className='fas fa-exclamation-triangle red')
        ]),
    ]),

    dcc.Upload(
        id='upload-data',
        children=html.I(className='fas fa-10x fa-file-upload button blue'),
        filename=''
    ),

    html.A(children=html.I(id='down-1', className='hidden'), href='#table-div'),

    html.Div(id='verify-file-div')
])

def ComparedR2Page(x, y, linear, deg2, deg3, deg4):
    return html.Div(id='compared-r2',
                    children=[
                        html.H3(f"Predyktor X: {x}    Zmienna zależna Y: {y}", style=style_h3),
                        html.H4(f"R^2 regresji liniowej wynosi {linear}", style=style_h4),
                        html.H4(f"R^2 regresji stopnia 2' wynosi {deg2}", style=style_h4),
                        html.H4(f"R^2 regresji stopnia 3' wynosi {deg3}", style=style_h4),
                        html.H4(f"R^2 regresji stopnia 4' wynosi {deg4}", style=style_h4),
                    ])

def TablePage(raw_data):
    return html.Div(id='upload-data-div',
                 children=[
                 html.Br(),
                 html.Div(id='button-div',
                          children=[
                              html.H3(id='confirm-quest', children=[
                                  'Is it your data? ',
                                  html.A(html.Button(id='confirm-data-button',
                                                     children=html.I(className='far fa-3x fa-thumbs-up button green'),
                                                     n_clicks=0, ),
                                         href='#refresh-button-2'),
                                  html.A(html.Button(id='refresh-button',
                                                     children=html.I(className='far fa-3x fa-thumbs-down button red')
                                                     ),
                                         href='/', ),
                              ])
                          ]),
                 html.Br(),
                 dcc.Loading(children=html.Div(id='table-div',
                                               children=[
                                                  dash_table.DataTable(
                                                      id='table',
                                                      columns=[{'name': col, 'id': col} for col in raw_data.columns],
                                                      data=raw_data.to_dict('records')
                                                  )],
                                               style={'overflowX': 'auto', 'overflowY': 'auto'}),
                             style={'margin':'200px auto',
                                    'transform':'scale(2)'}
                             )
                 ]),

result_page = html.Div(id='result-page', children=[
    html.Div(id='choose-data-div',
             children=[
                 html.Div(className='variable-div', id='x-div', children=[
                     html.H3('Choose predictor X'),
                     dcc.Dropdown(className='variable-dropdown', id='x-dropdown'),
                 ]),
                 html.Div(className='variable-div', id='y-div', children=[
                     html.H3('Choose dependent variable Y'),
                     dcc.Dropdown(className='variable-dropdown', id='y-dropdown')
                 ])
             ]),

    html.Div(id='compared-r2-div'),

    html.Div(id='select-subplots-div',
             children=[
                 html.H3('Wybierz regresję do zilustrowania', style=style_h3),
                 dcc.Checklist(id='subplots-checklist',
                               options=[
                                    {'label': 'Regresja liniowa', 'value': 'linear'},
                                    {'label': "Regresja stopnia 2'", 'value': 'deg2'},
                                    {'label': "Regresja stopnia 3'", 'value': 'deg3'},
                                    {'label': "Regresja stopnia 4'", 'value': 'deg4'}
                               ],
                               labelStyle={'display': 'block', 'font-size': 20},
                               value=[]
                               )],
             style={'display': 'none'}),

    html.Div(id='graph-div', style=style_graph),

    html.A(html.Button(id='refresh-button-2',
                       children='Może chcesz dac inny plik?'),
           href='/')
])

def WrongFilePage(filename):
    return html.Div(id='wrong-page', children=[
        html.I(className='far fa-9x fa-frown red'),
        html.H3(f"I'm sorry... I can't analyze your data named '{filename}'."),
        html.H3(children=[
            f"Try one of the following formats: ",
            html.Span(className='green', children="'.csv'"),
            html.Span(" or "),
            html.Span(className='green', children="'.xlsx'")
        ]),
        html.A(children=html.I(className='fas fa-3x fa-undo-alt button blue'), href='/'),
    ])