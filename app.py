import streamlit as st

from src.predict import predict_churn

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>

    .stApp {
        background: linear-gradient(
            135deg,
            #06111f 0%,
            #0a1f38 50%,
            #0e2a4a 100%
        );
        color: white;
    }

    [data-testid="stHeader"]{
      display:none;
      }

    [data-testid="stToolbar"]{
       display:none;
       }


    .block-container {
        max-width: 1200px;
        padding-top: 0rem;
        padding-bottom: 3rem;
        margin-top: -2 rem;
    }


    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #050d18 0%,
            #0a1c32 100%
        );

        border-right: 1px solid #1e4f80;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    .main-title {
        text-align: center;
        font-size: 44px;
        font-weight: 700;
        color: #60a5fa;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #cbd5e1;
        font-size: 18px;
        margin-bottom: 35px;
    }

    .section-title {
        font-size: 25px;
        font-weight: 600;
        color: #60a5fa;
        margin-top: 15px;
        margin-bottom: 18px;
    }

    .info-card {
        background: rgba(20, 48, 79, 0.75);
        border: 1px solid #2563a6;
        border-radius: 15px;
        padding: 22px;
        margin-bottom: 20px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.25);
    }

    label {
        color: #e2e8f0 !important;
        font-weight: 500 !important;
    }


    /* ================================
       SELECT BOX
       ================================ */

    div[data-baseweb="select"] > div {
        background-color: #162f4d !important;
        border: 1px solid #315d88 !important;
        border-radius: 8px !important;
        color: white !important;
    }


    /* Dropdown text */
    div[data-baseweb="select"] span {
        color: white !important;
    }

    input {
        background-color: #162f4d !important;
        color: white !important;
        border: 1px solid #315d88 !important;
        border-radius: 8px !important;
    }


    .stButton > button {
        width: 100%;
        height: 52px;

        border-radius: 10px;
        border: none;

        background: linear-gradient(
            90deg,
            #2563eb,
            #3b82f6
        );

        color: white;

        font-size: 18px;
        font-weight: 600;

        transition: all 0.3s ease;
    }


    .stButton > button:hover {
        background: linear-gradient(
            90deg,
            #1d4ed8,
            #2563eb
        );

        transform: translateY(-2px);

        box-shadow:
            0 8px 20px rgba(37, 99, 235, 0.35);
    }



    .churn-result {
        background: rgba(127, 29, 29, 0.25);

        border: 1px solid #ef4444;

        border-radius: 15px;

        padding: 28px;

        text-align: center;

        margin-top: 25px;

        box-shadow:
            0 8px 25px rgba(239, 68, 68, 0.15);
    }

    .stay-result {
        background: rgba(22, 101, 52, 0.25);

        border: 1px solid #22c55e;

        border-radius: 15px;

        padding: 28px;

        text-align: center;

        margin-top: 25px;

        box-shadow:
            0 8px 25px rgba(34, 197, 94, 0.15);
    }


   
    .result-title {
        font-size: 29px;
        font-weight: 700;
        margin-bottom: 10px;
    }


    
    .result-text {
        font-size: 17px;
        color: #cbd5e1;
    }


    hr {
        border-color: #2563a6;
    }


    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 14px;
        padding-top: 20px;
    }

</style>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="main-title">📊 Customer Churn Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine Learning Based Customer Retention System'
    '</div>',
    unsafe_allow_html=True
)



st.markdown(
    '<div class="section-title">👤 Customer Information</div>',
    unsafe_allow_html=True
)

left_column, right_column = st.columns(2)

with left_column:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    SeniorCitizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    Partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    Dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.number_input(
        "Tenure (months)",
        min_value=0,
        max_value=100,
        value=12
    )

    PhoneService = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    MultipleLines = st.selectbox(
        "Multiple Lines",
        [
            "Yes",
            "No",
            "No phone service"
        ]
    )

    InternetService = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )

    OnlineSecurity = st.selectbox(
        "Online Security",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    OnlineBackup = st.selectbox(
        "Online Backup",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )



with right_column:

    DeviceProtection = st.selectbox(
        "Device Protection",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    TechSupport = st.selectbox(
        "Tech Support",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    StreamingTV = st.selectbox(
        "Streaming TV",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    StreamingMovies = st.selectbox(
        "Streaming Movies",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    Contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    PaperlessBilling = st.selectbox(
        "Paperless Billing",
        [
            "Yes",
            "No"
        ]
    )

    PaymentMethod = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    MonthlyCharges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

    TotalCharges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=850.0
    )


st.markdown("---")

button_left, button_middle, button_right = st.columns(
    [1, 2, 1]
)

with button_middle:

    predict_button = st.button(
        "🔮 Predict Customer Churn"
    )


if predict_button:

    customer = {

        "gender": gender,

        "SeniorCitizen": SeniorCitizen,

        "Partner": Partner,

        "Dependents": Dependents,

        "tenure": tenure,

        "PhoneService": PhoneService,

        "MultipleLines": MultipleLines,

        "InternetService": InternetService,

        "OnlineSecurity": OnlineSecurity,

        "OnlineBackup": OnlineBackup,

        "DeviceProtection": DeviceProtection,

        "TechSupport": TechSupport,

        "StreamingTV": StreamingTV,

        "StreamingMovies": StreamingMovies,

        "Contract": Contract,

        "PaperlessBilling": PaperlessBilling,

        "PaymentMethod": PaymentMethod,

        "MonthlyCharges": MonthlyCharges,

        "TotalCharges": TotalCharges
    }


    try:

        result = predict_churn(customer)


        st.markdown("### Prediction Result")
        result_text=str(result)

        if "churn" in result_text.lower():
            st.warning(
                "⚠️ " + result_text
            )

            st.info(
                "💡 This customer may require a retention strategy."
            )

        else:

            st.success(
                "✅ " + result_text
            )

            st.info(
                "👍 This customer has a lower predicted churn risk."
            )
            

    except Exception as e:

        st.error(
            "Something went wrong while making the prediction."
        )

        st.exception(e)


