import streamlit as st
import pandas as pd

st.set_page_config(page_title= "Finanças", page_icon="💰")

st.markdown("""
# Boas Vindas!
            
## Nosso APP :)

Espero que Curta a experiência.
"""
)

# widget de upload de dados
file_upload = st.file_uploader(label= "Faça o upload dos dados aqui", type=['csv'])

# verifica o upload dos dados
if file_upload :
    
    # leitura dos dados
    df = pd.read_csv(file_upload)
    df["Data"] = pd.to_datetime(df['Data'], format="%d/%m/%Y").dt.date

    

    # exibição dos dados no APP
    exp1 = st.expander("Dados Brutos")
    columns_fmt = {"Valor":st.column_config.NumberColumn("Valor", format="R$ %f")}
    exp1.dataframe(df, hide_index=True, column_config=columns_fmt)

    # visão instituição
    exp2 = st.expander("Dados Brutos")
    df_instituicao = df.pivot_table(index="Data", columns="Instituição", values="Valor")

# abas para diferente vizualizações
    tab_data, tab_history, tab_share = exp2.tabs(["Dados", "Histórico", "Distribuição"])

    # Exibe o DF
    tab_data.dataframe(df_instituicao)

    # Exibe gráfico de linhas (histórico)
    with tab_history:
        st.line_chart(df_instituicao)

    # Exibe a distribuição
    with tab_share:

        # Filtro de data
        date = st.selectbox("Filtro Data", options=df_instituicao.index)

        # Gráfico de distribuição
        st.bar_chart(df_instituicao.loc[date])
        


# Não tem arquivo
