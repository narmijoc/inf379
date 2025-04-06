import pandas as pd
import plotly.graph_objects as go
import matplotlib.colors as mcolors

df = pd.read_csv("Produccion_mundial_cobre.csv", sep=";", decimal=",", skiprows=0, encoding='utf-8')

df = df.dropna()
df = df[~df.iloc[:, 0].str.contains("TOTAL|;;;;;;", regex=True)]

df = df.rename(columns={df.columns[0]: "País"})

for col in df.columns[1:]:
    df[col] = df[col].str.replace(".", "", regex=False).str.replace(",", ".", regex=False).astype(float)

year = "2023"

top_paises = df.nlargest(10, year)

source = list(range(10))
target = [10] * 10   
labels = top_paises["País"].tolist() + [f"Producción {year}"]
values = top_paises[year].tolist()


colores = list(mcolors.TABLEAU_COLORS.values())[:10] 

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=2),
        label=labels,
        color="lightgray",
    ),
    link=dict(
        source=source,
        target=target,
        value=values,
        color=colores
    )
)])

fig.update_layout(title_text=f"Producción minera a nivel mundial en {year}", font_size=12)
fig.show()
