import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import base64


'''
1. Wrzucam plik .csv
2. Wyświetla tabelę do zweryfikowania danych
3. Wybieram kolumnę X i kolumnę Y
4. Sprawdza regresje liniową, 2', 3' i 4'
5. Wyświetla interaktywny wykres
'''

# _______________________________________________________________________
# IMPORTOWANIE MODUŁÓW
# style
from my_module.style import external_stylesheets, style_dropdown_div, style_select_subplot, style_compared_r2, style_author

# sekcje
from my_module.sections import first_page, ComparedR2Page, WrongFilePage, TablePage, result_page

# funkcje
from my_module.functions import parse_contents, CompareR2, SelectNumberCols, MakeGraphData, MakeGraph
# _______________________________________________________________________

# przygotowanie obrazu
background = r'background1.png'
encoded_background = base64.b64encode(open(background,"rb").read())

# _______________________________________________________________________
# UKŁAD APLIKAJI
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)  # tworzenie klasy Dash
app.config.suppress_callback_exceptions=True
server = app.server

'''
                 html.Img(src=f'data:image/png;base64,{encoded_background.decode()}',
                          style={'position':'absolute', 'top':0, 'z-index':0}),
'''

background = r'background.jpg'
encoded_background = base64.b64encode(open(background,"rb").read())
style={
    'background-image': f'url(data:image/png;base64,{encoded_background.decode()}',
    'background-repeat':'no-repeat',
    'background-attachment':'fixed',
    'background-height':'100%',
    'margin':'0px',
    'padding':'0px'
}

app.layout = html.Div(id='body', children=[
    html.Div(children=first_page),
    html.Div(id='second-page', className='hidden', children=result_page)
], style=style)
# _______________________________________________________________________

# WYŚWIETLANIE PODSTRON
@app.callback(
    Output('page-content','children'),
    [
        Input('url','pathname'),
    ]
)
def display_page(pathname):
    if pathname == '/tech':
        pass
    else:
        return first_page

# SPRAWDZENIE POPRAWNOŚCI PLIKU
@app.callback(
    [
        Output('verify-file-div', 'children'),
        Output('headings-div', 'className'),
        Output('upload-data', 'className')
    ],
    Input('upload-data','contents'),
    State('upload-data','filename')
)
def VerifyUploadedFile(contents, filename):
    children = ''
    style = {'display':'none'}

    if filename.lower().endswith('.xlsx'):
        raw_data = parse_contents(contents, 'xlsx')
        children = TablePage(raw_data)

        return children, 'hidden', 'hidden'

    elif filename.lower().endswith('.csv'):
        raw_data = parse_contents(contents, 'csv')
        children = TablePage(raw_data)

        return children, 'hidden', 'hidden'

    elif len(filename) == 0:
        raise PreventUpdate
    else:
        children = WrongFilePage(filename)

        return children,'hidden', 'hidden'


# POTWIERDZENIE PLIKU
@app.callback(
    [
        Output('first-page','className'),
        Output('x-dropdown', 'options'),
        Output('y-dropdown', 'options'),
        Output('second-page', 'className')
    ],
    Input('confirm-data-button', 'n_clicks'),
    [
        State('upload-data','contents'),
        State('upload-data', 'filename')
    ]
)
def HideTable_ShowResults(n_clicks, contents, filename):
    if filename.lower().endswith('.xlsx'):
        if n_clicks >= 1:
            raw_data = parse_contents(contents, 'xlsx')
            columns = raw_data.columns
            df = SelectNumberCols(raw_data, columns)
            columns = df.columns

            print(columns)

            # lista kolumn do drop-down
            options_list = []
            for c in columns:
                option = {'label': c, 'value': c}
                options_list.append(option)

            return 'hidden', options_list, options_list, ''
        else:
            return '', [], [], 'hidden'
    elif filename.lower().endswith('.csv'):
        if n_clicks >= 1:
            raw_data = parse_contents(contents, 'csv')
            columns = raw_data.columns
            df = SelectNumberCols(raw_data, columns)
            columns = df.columns

            print(columns)

            # lista kolumn do drop-down
            options_list = []
            for c in columns:
                option = {'label': c, 'value': c}
                options_list.append(option)

            return 'hidden', options_list, options_list, ''
        else:
            return '', [], [], 'hidden'
    else:
        raise PreventUpdate

# POKAŻ WARTOŚCI R^2 + WYKRES
@app.callback(
    [
        Output('compared-r2-div', 'children'),
        Output('compared-r2-div', 'className'),
        Output('select-subplots-div', 'className'),
        Output('graph-div', 'children'),
        Output('graph-div', 'className')
    ],
    [
        Input('x-dropdown','value'),
        Input('y-dropdown','value'),
        Input('upload-data', 'contents'),
        Input('subplots-checklist', 'value'),
    ],
    State('upload-data', 'filename')
)
def ShowComparedR2(x,y, contents, selected_subplots, filename):
    raw_data = ''

    if filename.lower().endswith('.xlsx'):
        raw_data = parse_contents(contents, 'xlsx')
    elif filename.lower().endswith('.csv'):
        raw_data = parse_contents(contents, 'csv')
    else:
        raise PreventUpdate

    if x and y:
        columns = raw_data.columns
        df = SelectNumberCols(raw_data, columns)
        df[x].fillna(value=df[x].mean(), inplace=True)
        df[y].fillna(value=df[y].mean(), inplace=True)

        # dane do regresji
        X = df[x].to_numpy().reshape(-1, 1)
        Y = df[y].to_numpy().reshape(-1, 1)

        # porównanie R^2
        linear_r2, deg2_r2, deg3_r2, deg4_r2 = CompareR2(X, Y)

        # sekcja z R^2
        children = ComparedR2Page(x, y, linear_r2, deg2_r2, deg3_r2, deg4_r2)

        # dane do wykresów
        temp_df_deg1, temp_df_deg2, temp_df_deg3, temp_df_deg4 = MakeGraphData(X,Y)

        # wykres
        graph = MakeGraph(df[x], df[y], linear_r2, temp_df_deg1,
                          deg2_r2, temp_df_deg2, deg3_r2, temp_df_deg3, deg4_r2, temp_df_deg4, selected_subplots, x, y)

        return children, '', '', dcc.Graph(figure=graph), ''
    else:
        raise PreventUpdate


if __name__ == '__main__':
    app.run_server(debug=True)