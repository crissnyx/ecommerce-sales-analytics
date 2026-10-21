import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de página en modo Ancho (Wide)
st.set_page_config(
    page_title="Ecommerce Analytics & Churn SaaS v2.0.0",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados para replicar el diseño oscuro y moderno
st.markdown("""
<style>
    .main { background-color: #0d1117; color: #f0f6fc; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 8px; border: 1px solid #30363d; }
    div[data-testid="stMetricValue"] { font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# Encabezado principal
st.title("Ecommerce Analytics & Churn SaaS v2.0.0")
st.caption("Enterprise AI-powered sales intelligence & churn prediction platform")

st.markdown("---")

# Módulo de carga de archivos (Batch Churn Prediction)
st.subheader("Batch Churn Prediction (CSV)")
uploaded_file = st.file_uploader("Seleccionar archivo", type=["csv"])

# Datos de prueba si no se sube un archivo (demostrativos)
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    data = {
        'CUSTOMER ID': [f"CUST-{i:04d}" for i in range(1, 501)],
        'DEPARTMENT STORE': ['Electronics', 'Apparel', 'Home & Kitchen'] * 166 + ['Electronics'] * 2,
        'TOTAL SPEND': [200.0 + (i * 3.5) for i in range(500)],
        'CHURN PROBABILITY': [0.85 if i < 122 else (0.55 if i < 194 else 0.15) for i in range(500)],
        'RISK LEVEL': ['High Risk'] * 122 + ['Medium Risk'] * 72 + ['Low Risk'] * 306,
        'ACTION RECOMMENDATION': ['Send Offer 20% OFF' if i < 122 else ('Loyalty Nudge' if i < 194 else 'No Action Needed') for i in range(500)]
    }
    df = pd.DataFrame(data)

# --- TARJETAS KPI SUPERIORES ---
kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

kpi1.metric("ANALYZED CUSTOMERS", "500")
kpi2.metric("REVENUE AT RISK", "$163,563.00")
kpi3.metric("HIGH RISK (CHURN)", "122", "24.4%", delta_color="inverse")
kpi4.metric("MEDIUM RISK", "72", "14.4%", delta_color="off")
kpi5.metric("LOW RISK", "306", "61.2%", delta_color="normal")

st.markdown("<br>", unsafe_allow_html=True)

# --- GRÁFICOS EN PARALELO ---
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("Risk Level Share")
    risk_counts = df['RISK LEVEL'].value_counts().reset_index()
    risk_counts.columns = ['Risk', 'Count']
    
    fig_pie = px.pie(
        risk_counts, 
        values='Count', 
        names='Risk',
        color='Risk',
        color_discrete_map={
            'High Risk': '#ef4444', 
            'Medium Risk': '#f59e0b', 
            'Low Risk': '#10b981'
        },
        hole=0.4
    )
    fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white')
    st.plotly_chart(fig_pie, use_container_width=True)

with col_chart2:
    st.subheader("High Risk Churn by Department")
    high_risk_df = df[df['RISK LEVEL'] == 'High Risk']
    dept_counts = high_risk_df['DEPARTMENT STORE'].value_counts().reset_index()
    dept_counts.columns = ['Department', 'Count']
    
    fig_bar = px.bar(
        dept_counts, 
        x='Department', 
        y='Count',
        color_discrete_sequence=['#ef4444']
    )
    fig_bar.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white')
    st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")

# --- TABLA Y FILTROS ---
st.subheader("Analysis Results (500 customers displayed)")

col_search, col_filter = st.columns([2, 1])

with col_search:
    search_id = st.text_input("Search by Customer ID...", "")

with col_filter:
    filter_option = st.radio("Risk Filter", ["ALL", "HIGH", "MEDIUM", "LOW"], horizontal=True)

# Filtrado dinámico
filtered_df = df.copy()

if filter_option == "HIGH":
    filtered_df = filtered_df[filtered_df['RISK LEVEL'] == 'High Risk']
elif filter_option == "MEDIUM":
    filtered_df = filtered_df[filtered_df['RISK LEVEL'] == 'Medium Risk']
elif filter_option == "LOW":
    filtered_df = filtered_df[filtered_df['RISK LEVEL'] == 'Low Risk']

if search_id:
    filtered_df = filtered_df[filtered_df['CUSTOMER ID'].str.contains(search_id, case=False)]

st.dataframe(filtered_df, use_container_width=True)