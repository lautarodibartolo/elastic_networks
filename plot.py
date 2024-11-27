import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("rmsd_data.csv")
df["time_us"] = df["time_ps"] / 1000000
unique_proteins = df["protein"].unique()

colors = {True: "royalblue", False: "firebrick"}
labels = {True: "Con Malla Elástica", False: "Sin Malla Elástica"}

for protein in unique_proteins:
    protein_data = df[df["protein"] == protein]

    fig = go.Figure()

    for en in [True, False]:
        data = protein_data[protein_data["elastic_network"] == en]
        fig.add_trace(
            go.Scatter(
                x=data["time_us"],
                y=data["rmsd_nm"],
                name=labels[en],
                line=dict(color=colors[en], width=2),
                mode="lines",
            )
        )

    fig.update_layout(
        height=600,
        width=800,
        xaxis_title="Tiempo (μs)",
        yaxis_title="RMSD (nm)",
        font=dict(family="Arial", size=14),
        legend=dict(
            yanchor="top",
            y=-0.15,
            xanchor="center",
            x=0.5,
            bgcolor="rgba(255,255,255,0.5)",
            bordercolor="Black",
            borderwidth=1,
            orientation="h",
        ),
        plot_bgcolor="rgba(240,240,240,0.9)",
        paper_bgcolor="white",
        margin=dict(b=100),
    )

    fig.update_xaxes(title_font=dict(size=16), tickfont=dict(size=14))
    fig.update_yaxes(title_font=dict(size=16), tickfont=dict(size=14))

    fig.write_image(f"{protein}_rmsd.png", scale=2)
