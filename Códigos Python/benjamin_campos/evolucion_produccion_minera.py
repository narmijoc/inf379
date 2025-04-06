import pandas as pd
import plotly.express as px

df = pd.read_csv("Indice_de_produccion_anual.csv", delimiter=';', decimal=',', encoding='utf-8')

df_melted = df.melt(id_vars="Periodo", var_name="Categoría", value_name="Índice")

df_melted["Periodo"] = df_melted["Periodo"].astype(str)

pivot_df = df_melted.pivot(index="Categoría", columns="Periodo", values="Índice")
pivot_df = pivot_df[sorted(pivot_df.columns, key=lambda x: int(x))]

fig = px.imshow(
    pivot_df,
    color_continuous_scale="YlOrRd",
    aspect="auto",
    labels=dict(x="Año", y="Categoría", color="Índice"),
    title="Evolución de la Producción Minera en Chile"
)

fig.update_layout(
    xaxis_title="Año",
    yaxis_title="Categoría",
    height=600,
    xaxis=dict(tickmode='array', tickvals=list(range(len(pivot_df.columns))), ticktext=pivot_df.columns)
)

fig.show()
