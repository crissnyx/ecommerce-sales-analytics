from __future__ import annotations
<<<<<<< HEAD
=======

>>>>>>> origin/feat/project-structure
import joblib
import pandas as pd
import plotly.express as px
import streamlit as st
<<<<<<< HEAD
=======

>>>>>>> origin/feat/project-structure
from app.config import MODEL_PATH
from app.data.loader import load_csv, validate_columns
from app.data.preprocess import clean_customer_data, create_features
from app.models.predict import predict_churn
from app.models.train import train_churn_model

<<<<<<< HEAD
=======

>>>>>>> origin/feat/project-structure
def render_dashboard():
    st.set_page_config(page_title="Ecommerce Analytics & Churn SaaS", layout="wide")
    st.title("Ecommerce Analytics & Churn SaaS")
    st.caption("Enterprise AI-powered sales intelligence & churn prediction platform")
<<<<<<< HEAD
    
    uploaded_file = st.file_uploader("Upload a customer CSV", type=["csv"])
    
=======

    uploaded_file = st.file_uploader("Upload a customer CSV", type=["csv"])

>>>>>>> origin/feat/project-structure
    if uploaded_file is not None:
        df = load_csv(uploaded_file)
        validate_columns(
            df,
            {
                "CUSTOMER ID",
                "DEPARTMENT STORE",
                "TOTAL SPEND",
                "PURCHASES",
                "AVG ORDER VALUE",
                "TENURE DAYS",
                "LAST PURCHASE DAYS",
                "RETURNS",
                "CANCELLATIONS",
            },
        )
<<<<<<< HEAD
        cleaned = clean_customer_data(df)
        features_df = create_features(cleaned)
        
        if "CHURN_LABEL" not in features_df.columns:
            features_df["CHURN_LABEL"] = (features_df["CHURN_SCORE"] >= 70).astype(int)
            
        model = train_churn_model(features_df, model_path=MODEL_PATH)
        results = predict_churn(model, features_df)
        
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        counts = results["RISK_LEVEL"].value_counts().to_dict()
        
=======

        cleaned = clean_customer_data(df)
        features_df = create_features(cleaned)

        if "CHURN_LABEL" not in features_df.columns:
            features_df["CHURN_LABEL"] = (features_df["CHURN_SCORE"] >= 70).astype(int)

        model = train_churn_model(features_df, model_path=MODEL_PATH)
        results = predict_churn(model, features_df)

        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        counts = results["RISK_LEVEL"].value_counts().to_dict()

>>>>>>> origin/feat/project-structure
        kpi1.metric("Customers", str(len(results)))
        kpi2.metric("Revenue at Risk", f"${results['TOTAL SPEND'].sum():,.2f}")
        kpi3.metric("High Risk", str(counts.get("High Risk", 0)))
        kpi4.metric("Low Risk", str(counts.get("Low Risk", 0)))
<<<<<<< HEAD
        
        risk_counts = results["RISK_LEVEL"].value_counts().reset_index()
        risk_counts.columns = ["Risk", "Count"]
        
=======

        risk_counts = results["RISK_LEVEL"].value_counts().reset_index()
        risk_counts.columns = ["Risk", "Count"]

>>>>>>> origin/feat/project-structure
        pie_chart = px.pie(
            risk_counts,
            values="Count",
            names="Risk",
            color="Risk",
            color_discrete_map={
                "High Risk": "#ef4444",
                "Medium Risk": "#f59e0b",
                "Low Risk": "#10b981",
            },
            hole=0.4,
        )
<<<<<<< HEAD
        
        st.subheader("Risk Distribution")
        st.plotly_chart(pie_chart, use_container_width=True)
        
=======

        st.subheader("Risk Distribution")
        st.plotly_chart(pie_chart, use_container_width=True)

>>>>>>> origin/feat/project-structure
        st.subheader("Predicted Results")
        st.dataframe(
            results[["CUSTOMER ID", "DEPARTMENT STORE", "TOTAL SPEND", "CHURN_PROBABILITY", "RISK_LEVEL"]],
            use_container_width=True,
        )
    else:
        st.info("Upload a CSV to run churn prediction.")

<<<<<<< HEAD
if __name__ == "__main__":
    render_dashboard()
=======

if __name__ == "__main__":
    render_dashboard()
>>>>>>> origin/feat/project-structure
