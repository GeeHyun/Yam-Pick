# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from config import SQLALCHEMY_DATABASE_URI
from sqlalchemy import create_engine
import pandas as pd
from functions import func_user__nutrient

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import dash_daq as daq

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_recycle=280)


foods = pd.read_sql_query("select * from tb_user_img;", engine)

if len(foods):
    food = foods.iloc[-1]

    user_email = food['upload_user']
    user = pd.read_sql_query(f"select * from tb_user_info where user_email = '{user_email}';", engine).iloc[-1]

    user_age = func_user__nutrient.user_age(user['user_birth'])
    weight_s = func_user__nutrient.standard_weight(user['user_sex'], user['user_height'])
    weight_a = func_user__nutrient.adjusted_weight(user['user_weight'], weight_s)
    user_calorie = func_user__nutrient.calorie_counting(user['user_sex'], user_age, user['user_height'], weight_a, str(user['user_pa']))
    user_nutrient_dic = func_user__nutrient.necessary_nutrients(user['user_sex'], user_age, user['user_weight'], user_calorie)

    food_calorie = pd.read_sql_query(f"select energy from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    food_percent = food['upload_percent']

    eated_calorie = food_calorie * food_percent
    eated_calorie_per = int((eated_calorie/user_calorie) * 100)


def food_item(item):
    return pd.read_sql_query(f"select {item} from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]

# 문제 많음
def food_recomend():
    carbohydrate = pd.read_sql_query(f"select carbohydrate from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    fat = pd.read_sql_query(f"select fat from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    protein = pd.read_sql_query(f"select protein from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    moisture = pd.read_sql_query(f"select moisture from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    vitamin_A = pd.read_sql_query(f"select vitamin_A from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    vitamin_D = pd.read_sql_query(f"select vitamin_D from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    vitamin_E = pd.read_sql_query(f"select vitamin_E from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    vitamin_C = pd.read_sql_query(f"select vitamin_C from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    folic_acid = pd.read_sql_query(f"select folic_acid from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    phosphorus = pd.read_sql_query(f"select phosphorus from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    sodium = pd.read_sql_query(f"select sodium from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    potassium = pd.read_sql_query(f"select potassium from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    manganese = pd.read_sql_query(f"select manganese from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    selenium = pd.read_sql_query(f"select selenium from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    dietary_fiber = pd.read_sql_query(f"select dietary_fiber from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    thiamin = pd.read_sql_query(f"select thiamin from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    riboflavin = pd.read_sql_query(f"select riboflavin from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    niacin = pd.read_sql_query(f"select niacin from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    calcium = pd.read_sql_query(f"select calcium from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    magnesium = pd.read_sql_query(f"select magnesium from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    iron = pd.read_sql_query(f"select iron from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    zinc = pd.read_sql_query(f"select zinc from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    copper = pd.read_sql_query(f"select copper from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    linolenic_acid = pd.read_sql_query(f"select linolenic_acid from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    a_linolenic_acid = pd.read_sql_query(f"select a_linolenic_acid from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]
    unsaturated_fatty_aci = pd.read_sql_query(f"select unsaturated_fatty_aci from tb_food_img where food_name = '{food['upload_foodname']}';", engine).iloc[0, 0]

    total_dic = {'carbohydrate': carbohydrate, 'fat': fat, 'protein': protein, 'moisture': moisture,
                'vitamin_A': vitamin_A, 'vitamin_D': vitamin_D, 'vitamin_E': vitamin_E, 'vitamin_C': vitamin_C,
                'folic_acid': folic_acid, 'phosphorus': phosphorus, 'sodium': sodium, 'potassium': potassium,
                'manganese': manganese, 'selenium': selenium, 'dietary_fiber': dietary_fiber, 'thiamin': thiamin,
                'riboflavin': riboflavin, 'niacin': niacin, 'calcium': calcium, 'magnesium': magnesium, 'iron': iron,
                'zinc': zinc, 'copper': copper, 'linolenic_acid': linolenic_acid, 'a_linolenic_acid': a_linolenic_acid,
                'unsaturated_fatty_aci': unsaturated_fatty_aci}

    food_list = pd.read_sql_query("select * from tb_food_img;", engine)

    for x in user_nutrient_dic.keys():
        total_dic[x] = (total_dic[x] / user_nutrient_dic[x]) * 100

    min_nurient = min(total_dic, key=total_dic.get)

    return food_list.loc[(food_list[min_nurient].argmax(), 'food_name')]


# def food_img(food_recomend()):
#     if food_recomend() != None:



params = list(user_nutrient_dic.keys())

unit_dic = {'carbohydrate' : 'g' ,'fat' :'g' ,'protein' : 'g' ,'moisture' : 'ml' ,
'vitamin_A' : '㎍' ,'vitamin_D' : '㎍' ,'vitamin_E' : '㎎' ,'vitamin_C' : '㎎' ,
'folic_acid' : '㎍' ,'phosphorus' : '㎎' ,'sodium': '㎎' ,'potassium': '㎎' ,
'manganese' : '㎎' ,'selenium' :'㎍' ,'dietary_fiber' : 'g' ,'thiamin': '㎎' ,
'riboflavin' : '㎎' ,'niacin' : '㎍' ,'calcium' :'㎎' ,'magnesium' : '㎎' ,'iron' : '㎎' ,
'zinc' : '㎎' ,'copper' : '㎎' ,'linolenic_acid' : 'g' ,'a_linolenic_acid' : 'g' ,
'unsaturated_fatty_aci' : '㎎'}


suffix_row = "_row"
suffix_button_id = "_button"
suffix_sparkline_graph = "_sparkline_graph"
suffix_count = "_count"
suffix_ooc_n = "_OOC_number"
suffix_ooc_g = "_OOC_graph"
suffix_indicator = "_indicator"

# Colors
bgcolor = "#f3f3f1"  # mapbox light map land color
bar_bgcolor = "#b0bec5"  # material blue-gray 200

# Figure template
row_heights = [150, 500, 300]
template = {"layout": {"paper_bgcolor": bgcolor, "plot_bgcolor": bgcolor}}

# def food_recomend():

def build_banner():
    return html.Div(
        id="banner",
        className="banner",
        children=[
            html.Div(
                id="banner-text",
                children=[
                    html.H5("Yam-Pick"),
                    html.H6("Analysis"),
                ],
            ),
            html.Div(
                id="banner-logo",
                children=[
                    # html.A(
                    #     html.Img(id="logo", src=("static/plotly_logo.png")),
                    #     href="http://smooth.pythonanywhere.com/",
                    # ),
                ],
            ),
        ],
    )

def build_tabs():
    return html.Div(
        id="tabs",
        className="tabs",
        children=[
            dcc.Tabs(
                id="app-tabs",
                value="tab2",
                className="custom-tabs",
                children=[
                    dcc.Tab(
                        id="Control-chart-tab",
                        label="Control Charts Dashboard",
                        value="tab2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                ],
            )
        ],
    )

def build_tab_1():
    return [
        # Manually select metrics
        html.Div(
            id="set-specs-intro-container",
            # className='twelve columns',
            children=html.P(
                "Use historical control limits to establish a benchmark, or set new values."
            ),
        ),
        html.Div(
            id="settings-menu",
            children=[
                html.Div(
                    id="metric-select-menu",
                    # className='five columns',
                    children=[
                        html.Label(id="metric-select-title", children="Select Metrics"),
                        html.Br(),
                        dcc.Dropdown(
                            id="metric-select-dropdown",
                            options=list(
                                {"label": param, "value": param} for param in params[1:]
                            ),
                            value=params[1],
                        ),
                    ],
                ),
                html.Div(
                    id="value-setter-menu",
                    # className='six columns',
                    children=[
                        html.Div(id="value-setter-panel"),
                        html.Br(),
                        html.Div(
                            id="button-div",
                            children=[
                                html.Button("Update", id="value-setter-set-btn"),
                                html.Button(
                                    "View current setup",
                                    id="value-setter-view-btn",
                                    n_clicks=0,
                                ),
                            ],
                        ),
                        html.Div(
                            id="value-setter-view-output", className="output-datatable"
                        ),
                    ],
                ),
            ],
        ),
    ]

def generate_modal():
    return html.Div(
        id="markdown",
        className="modal",
        children=(
            html.Div(
                id="markdown-container",
                className="markdown-container",
                children=[
                    html.Div(
                        className="close-container",
                        children=html.Button(
                            "Close",
                            id="markdown_close",
                            n_clicks=0,
                            className="closeButton",
                        ),
                    ),
                ],
            )
        ),
    )

def generate_section_banner(title):
    return html.Div(className="section-banner", children=title)


def build_top_panel(stopped_interval):
    return html.Div(
        id="top-section-container",
        className="row",
        children=[
            # Metrics summary
            html.Div(
                id="metric-summary-session",
                className="eight columns",
                children=[
                    generate_section_banner("Nutrient Information"),
                    html.Div(
                        id="metric-div",
                        children=[
                            generate_metric_list_header(),
                            html.Div(
                                id="metric-rows",
                                children=[
                                    generate_metric_row_helper(0),
                                    generate_metric_row_helper(1),
                                    generate_metric_row_helper(2),
                                    generate_metric_row_helper(3),
                                    generate_metric_row_helper(4),
                                    generate_metric_row_helper(5),
                                    generate_metric_row_helper(6),
                                    generate_metric_row_helper(7),
                                    generate_metric_row_helper(8),
                                    generate_metric_row_helper(9),
                                    generate_metric_row_helper(10),
                                    generate_metric_row_helper(11),
                                    generate_metric_row_helper(12),
                                    generate_metric_row_helper(13),
                                    generate_metric_row_helper(14),
                                    generate_metric_row_helper(15),
                                    generate_metric_row_helper(16),
                                    generate_metric_row_helper(17),
                                    generate_metric_row_helper(18),
                                    generate_metric_row_helper(19),
                                    generate_metric_row_helper(20),
                                    generate_metric_row_helper(21),
                                    generate_metric_row_helper(22),
                                    generate_metric_row_helper(23),
                                    generate_metric_row_helper(24),
                                    generate_metric_row_helper(25),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            # Piechart
            html.Div(
                id="ooc-piechart-outer",
                className="four columns",
                style={"text-align": "center"},
                children=[
                    generate_section_banner("Recommended food"),
                    html.Div(
                        str(food_recomend())
                    ),
                ],
            ),
        ],
    )

# Build header
def generate_metric_list_header():
    return generate_metric_row(
        "metric_header",
        {"height": "3rem", "margin": "1rem 0", "textAlign": "center"},
        {"id": "m_header_1", "children": html.Div("Parameter")},
        {"id": "m_header_2", "children": html.Div("Count")},
        {"id": "m_header_3", "children": html.Div("Unit")},
        {"id": "m_header_4", "children": html.Div("%")},
        {"id": "m_header_5", "children": html.Div("Gauge Bar")},
        {"id": "m_header_6", "children": "Pass/Fail"},
    )


def generate_metric_row_helper(index):
    item = params[index]

    div_id = item + suffix_row
    button_id = item + suffix_button_id
    sparkline_graph_id = item + suffix_sparkline_graph
    count_id = item + suffix_count
    ooc_percentage_id = item + suffix_ooc_n
    ooc_graph_id = item + suffix_ooc_g
    indicator_id = item + suffix_indicator

    return generate_metric_row(
        div_id,
        None,
        {
            "id": item,
            "className": "metric-row-button-text",
            "children": html.Button(
                id=button_id,
                className="metric-row-button",
                children=item,
                title="Click to visualize live SPC chart",
                n_clicks=0,
            ),
        },
        {"id": count_id, "children": food_item(item)}, # 수정 -> 영양소 용량
        {
            "id": item + "_sparkline",
            "children": html.Div(
                id=sparkline_graph_id,
                style={"width": "100%"},
                children=unit_dic[item], # -> 영양소 단위
            ),
        },
        {"id": ooc_percentage_id, "children": round(food_item(item)/user_nutrient_dic[item] * 100, 2)}, # 수정 -> 영양소 퍼센트
        {
            "id": ooc_graph_id + "_container",
            "children": daq.GraduatedBar(
                id=ooc_graph_id,
                color={
                    "ranges": {
                        "#f45060": [0, 8],
                        "#f4d44d": [8, 15],
                        "#92e0d3": [15, 20],
                    }
                },
                showCurrentValue=False,
                max=20,
                value=round(food_item(item)/user_nutrient_dic[item] * 100, 2)/5, # 수정 -> 영양소 퍼센트 / 5
            ),
        },
        {
            "id": item + "_pf",
            "children": daq.Indicator(
                id=indicator_id, value=True, color="#91dfd2", size=12

            ),
        },
    )


def generate_metric_row(id, style, col1, col2, col3, col4, col5, col6):
    if style is None:
        style = {"height": "8rem", "width": "100%"}

    return html.Div(
        id=id,
        className="row metric-row",
        style=style,
        children=[
            html.Div(
                id=col1["id"],
                className="one column",
                style={"margin-right": "2.5rem", "minWidth": "50px"},
                children=col1["children"],
            ),
            html.Div(
                id=col2["id"],
                style={"textAlign": "center"},
                className="one column",
                children=col2["children"],
            ),
            html.Div(
                id=col3["id"],
                style={"textAlign": "center", "width": "5%"},
                className="four columns",
                children=col3["children"],
            ),
            html.Div(
                id=col4["id"],
                style={},
                className="one column",
                children=col4["children"],
            ),
            html.Div(
                id=col5["id"],
                style={"height": "100%", "margin-top": "5rem"},
                className="three columns",
                children=col5["children"],
            ),
        ],
    )


def build_chart_panel():
    return html.Div(
        id="control-chart-container",
        className="twelve columns",
        children=[
            generate_section_banner("Coming soon.."),
            dcc.Graph(
                id="control-chart-live",
                figure=go.Figure(
                    {
                        "data": [
                            {
                                "x": [],
                                "y": [],
                                "mode": "lines+markers",
                                "name": params[1],
                            }
                        ],
                        "layout": {
                            "paper_bgcolor": "rgba(0,0,0,0)",
                            "plot_bgcolor": "rgba(0,0,0,0)",
                            "xaxis": dict(
                                showline=False, showgrid=False, zeroline=False
                            ),
                            "yaxis": dict(
                                showgrid=False, showline=False, zeroline=False
                            ),
                            "autosize": True,
                        },
                    }
                ),
            ),
        ],
    )


def build_quick_stats_panel():
    return html.Div(
        id="quick-stats",
        className="row",
        children=[
            html.Div(
                id="card-1",
                children=[
                    html.P("Daliy Calorie"),
                    daq.LEDDisplay(
                        id="operator-led",
                        value=eated_calorie, # 수정 -> 섭취 칼로리
                        color="#92e0d3",
                        backgroundColor="#1e2130",
                        size=50,
                    ),
                ],
            ),
            html.Div(
                id="card-2",
                children=[
                    html.P("Calorie Gauge"),
                    daq.Gauge(
                        id="progress-gauge",
                        max=100,
                        units="%",
                        min=0,
                        value=eated_calorie_per, # 수정 -> 섭취 칼로리 퍼센트
                        showCurrentValue=True,  # default size 200 pixel
                    ),
                ],
            ),
        ],
    )

# Build Dash layout
def create_dashboard(server):
    dash_app = dash.Dash(
    server=server,
    url_base_pathname='/dashboard/',
    assets_folder='plotlydash/assets'
    )


    dash_app.layout = html.Div(
        id="big-app-container",
        children=[
            build_banner(),
            dcc.Interval(
                id="interval-component",
                interval=2 * 1000,  # in milliseconds
                n_intervals=50,  # start at batch 50
                disabled=True,
            ),
            html.Div(
                id="app-container",
                children=[
                    build_tabs(),
                    # Main app
                    html.Div(id="app-content"),
                ],
            ),
            dcc.Store(id="n-interval-stage", data=50),
            generate_modal(),
        ],
    )

    init_callbacks(dash_app)

    return dash_app.server


def init_callbacks(dash_app):
    @dash_app.callback(
    [Output("app-content", "children"), Output("interval-component", "n_intervals")],
    [Input("app-tabs", "value")],
    [State("n-interval-stage", "data")],
    )
    def render_tab_content(tab_switch, stopped_interval):
        if tab_switch == "tab1":
            return build_tab_1(), stopped_interval
        return (
            html.Div(
                id="status-container",
                children=[
                    build_quick_stats_panel(),
                    html.Div(
                        id="graphs-container",
                        children=[build_top_panel(stopped_interval), build_chart_panel()],
                    ),
                ],
            ),
            stopped_interval,
        )

