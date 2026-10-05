import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Climate Intelligence Command Center",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# PREMIUM PASTEL UI
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

* {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
    radial-gradient(circle at 5% 5%, rgba(225,214,246,.45), transparent 28%),
    radial-gradient(circle at 95% 8%, rgba(215,240,231,.50), transparent 25%),
    linear-gradient(135deg,#fbf9fd,#f7f8fc,#f3faf7);
}

.block-container {
    max-width: 1500px;
    padding-top: 1.8rem;
    padding-bottom: 3rem;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#f0eafa,#edf7f3);
    border-right: 1px solid #e4ddea;
}

.hero {
    background:
    linear-gradient(
        135deg,
        rgba(235,226,249,.96),
        rgba(250,232,234,.96),
        rgba(225,245,238,.96)
    );
    border-radius: 30px;
    padding: 35px 40px;
    border: 1px solid rgba(255,255,255,.9);
    box-shadow: 0 15px 45px rgba(70,60,100,.08);
    margin-bottom: 24px;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 44px;
    font-weight: 700;
    color: #40394f;
}

.hero-subtitle {
    color: #756d80;
    font-size: 16px;
    margin-top: 7px;
}

.status {
    display: inline-block;
    padding: 7px 14px;
    border-radius: 30px;
    background: rgba(255,255,255,.72);
    color: #67587e;
    font-size: 12px;
    font-weight: 700;
}

.section {
    color: #494254;
    font-size: 23px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 15px;
}

.card {
    background: rgba(255,255,255,.86);
    border: 1px solid #e5dfea;
    border-radius: 22px;
    padding: 21px;
    box-shadow: 0 8px 28px rgba(70,60,90,.055);
}

.card-label {
    color: #8b8293;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: .5px;
}

.card-value {
    color: #433b4f;
    font-size: 29px;
    font-weight: 700;
    margin-top: 7px;
}

.card-small {
    color: #918996;
    font-size: 12px;
    margin-top: 5px;
}

.risk-low {
    background: linear-gradient(135deg,#e5f5ec,#dcefe7);
    border: 1px solid #cbe5d7;
}

.risk-moderate {
    background: linear-gradient(135deg,#fff3dc,#ffead1);
    border: 1px solid #f1ddbd;
}

.risk-high {
    background: linear-gradient(135deg,#ffe5e4,#f9dcdc);
    border: 1px solid #efcaca;
}

.risk-extreme {
    background: linear-gradient(135deg,#f4dddd,#ecd1d9);
    border: 1px solid #e4c0ca;
}

.risk-box {
    border-radius: 25px;
    padding: 27px;
    text-align: center;
    min-height: 220px;
}

.risk-score {
    font-size: 55px;
    font-weight: 700;
    color: #48404f;
}

.risk-name {
    font-size: 22px;
    font-weight: 700;
}

.info {
    background: linear-gradient(135deg,#eee9fb,#e8f0fb);
    border-radius: 18px;
    padding: 19px;
    color: #625a73;
}

.alert {
    background: linear-gradient(135deg,#fff0e4,#ffebdf);
    border-left: 6px solid #d89a69;
    border-radius: 17px;
    padding: 20px;
}

.alert-red {
    background: linear-gradient(135deg,#ffe7e7,#fbdede);
    border-left: 6px solid #c97979;
    border-radius: 17px;
    padding: 20px;
}

.success {
    background: linear-gradient(135deg,#e5f5ed,#ddf0e7);
    border-radius: 18px;
    padding: 19px;
    color: #567966;
}

.ai-box {
    background: linear-gradient(135deg,#f1ebfb,#edf4f5);
    border: 1px solid #ded6e9;
    border-radius: 23px;
    padding: 25px;
}

.footer {
    text-align: center;
    color: #9991a4;
    font-size: 12px;
    margin-top: 40px;
}

.stButton > button {
    width: 100%;
    border-radius: 14px;
    border: none;
    padding: 13px;
    background: linear-gradient(135deg,#9586b9,#b395bd);
    color: white;
    font-weight: 700;
    font-size: 15px;
}

.stButton > button:hover {
    color: white;
    background: linear-gradient(135deg,#8878ad,#a684af);
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# CITY DATA
# ============================================================

locations = {
    "Mumbai": {
        "lat": 19.0760,
        "lon": 72.8777,
        "base": 32,
        "humidity": 72
    },
    "Delhi": {
        "lat": 28.6139,
        "lon": 77.2090,
        "base": 35,
        "humidity": 54
    },
    "Ahmedabad": {
        "lat": 23.0225,
        "lon": 72.5714,
        "base": 37,
        "humidity": 48
    },
    "Surat": {
        "lat": 21.1702,
        "lon": 72.8311,
        "base": 34,
        "humidity": 68
    },
    "Nagpur": {
        "lat": 21.1458,
        "lon": 79.0882,
        "base": 36,
        "humidity": 50
    },
    "Jaipur": {
        "lat": 26.9124,
        "lon": 75.7873,
        "base": 37,
        "humidity": 43
    },
    "Pune": {
        "lat": 18.5204,
        "lon": 73.8567,
        "base": 31,
        "humidity": 58
    },
    "Bengaluru": {
        "lat": 12.9716,
        "lon": 77.5946,
        "base": 29,
        "humidity": 62
    },
    "Hyderabad": {
        "lat": 17.3850,
        "lon": 78.4867,
        "base": 34,
        "humidity": 56
    },
    "Kolkata": {
        "lat": 22.5726,
        "lon": 88.3639,
        "base": 33,
        "humidity": 74
    }
}


# ============================================================
# RISK ENGINE
# ============================================================

def calculate_risk(temp, humidity, wind=10):

    heat_index = temp + (0.05 * humidity)

    temperature_factor = min(
        max((temp - 30) * 4, 0),
        45
    )

    humidity_factor = min(
        max((humidity - 40) * 0.45, 0),
        25
    )

    heat_factor = min(
        max((heat_index - 32) * 2, 0),
        20
    )

    wind_factor = max(
        0,
        (12 - wind) * 0.8
    )

    score = (
        temperature_factor +
        humidity_factor +
        heat_factor +
        wind_factor
    )

    score = int(
        min(
            max(score, 0),
            100
        )
    )

    if score >= 85:
        level = "EXTREME"
    elif score >= 70:
        level = "HIGH"
    elif score >= 45:
        level = "MODERATE"
    else:
        level = "LOW"

    return score, level, heat_index


# ============================================================
# HISTORICAL DATA
# ============================================================

def generate_history(location):

    np.random.seed(
        sum(ord(x) for x in location)
    )

    dates = pd.date_range(
        start="2020-01-01",
        end="2026-09-01",
        freq="MS"
    )

    base = locations[location]["base"]

    seasonal = (
        3 *
        np.sin(
            np.arange(len(dates))
            * 2
            * np.pi
            / 12
        )
    )

    trend = np.linspace(
        0,
        2.8,
        len(dates)
    )

    noise = np.random.normal(
        0,
        1.4,
        len(dates)
    )

    temperature = (
        base +
        seasonal +
        trend +
        noise
    )

    humidity = (
        locations[location]["humidity"]
        +
        np.random.normal(
            0,
            4,
            len(dates)
        )
    )

    humidity = np.clip(
        humidity,
        20,
        95
    )

    risk_scores = []

    for t, h in zip(
        temperature,
        humidity
    ):

        score, _, _ = calculate_risk(
            t,
            h
        )

        risk_scores.append(score)

    return pd.DataFrame({
        "Date": dates,
        "Temperature": temperature,
        "Humidity": humidity,
        "Risk": risk_scores
    })


# ============================================================
# FORECAST
# ============================================================

def generate_forecast(
    location,
    current_temperature
):

    np.random.seed(20)

    rows = []

    for i in range(1, 8):

        temp = (
            current_temperature
            +
            np.random.uniform(
                -1.2,
                2.8
            )
        )

        humidity = (
            locations[location]["humidity"]
            +
            np.random.uniform(
                -6,
                7
            )
        )

        score, level, heat_index = calculate_risk(
            temp,
            humidity
        )

        probability = int(
            min(
                97,
                max(
                    5,
                    score +
                    np.random.randint(
                        -8,
                        8
                    )
                )
            )
        )

        rows.append({
            "Date":
                datetime.now()
                + timedelta(days=i),

            "Day":
                (
                    datetime.now()
                    + timedelta(days=i)
                ).strftime("%a"),

            "Temperature":
                round(temp, 1),

            "Humidity":
                round(humidity),

            "Heat Index":
                round(heat_index, 1),

            "Risk":
                level,

            "Probability":
                probability
        })

    return pd.DataFrame(rows)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <h2 style="
        font-family:Playfair Display;
        color:#51475f;">
        🌿 Climate AI
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.caption(
        "Climate Intelligence Command Center"
    )

    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "🏠 Command Center",
            "🔮 Predictive Analytics",
            "📈 Historical Intelligence",
            "🗺️ Climate Risk Map",
            "🧠 Explainable AI",
            "🧪 What-If Simulator",
            "🚨 Alert Center"
        ]
    )

    st.divider()

    selected_location = st.selectbox(
        "📍 Monitoring Location",
        list(locations.keys())
    )

    st.divider()

    st.markdown(
        "### 📡 SYSTEM STATUS"
    )

    st.success(
        "● Data Engine Online"
    )

    st.success(
        "● Risk Engine Online"
    )

    st.success(
        "● Prediction Engine Online"
    )

    st.success(
        "● Alert Engine Online"
    )

    st.caption(
        "Last synchronization: Just now"
    )


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="hero">

<div class="status">
● SYSTEM ONLINE
&nbsp; | &nbsp;
AI ANALYTICS ACTIVE
&nbsp; | &nbsp;
EARLY WARNING READY
</div>

<div class="hero-title">
🌿 Climate Intelligence
</div>

<div class="hero-subtitle">
Enterprise Heatwave Monitoring, Predictive Analytics
& Early Warning Decision Support Platform
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# CURRENT CONDITIONS
# ============================================================

history = generate_history(
    selected_location
)

current_temperature = round(
    history["Temperature"].iloc[-1] + 4,
    1
)

current_humidity = (
    locations[selected_location]["humidity"]
)

current_wind = 9

risk_score, risk_level, heat_index = calculate_risk(
    current_temperature,
    current_humidity,
    current_wind
)


# ============================================================
# COMMAND CENTER
# ============================================================

if page == "🏠 Command Center":

    st.markdown(
        '<div class="section">🌤️ Current Environmental Intelligence</div>',
        unsafe_allow_html=True
    )

    columns = st.columns(5)

    metrics = [
        (
            "🌡️",
            "TEMPERATURE",
            f"{current_temperature}°C",
            "Current reading"
        ),
        (
            "💧",
            "HUMIDITY",
            f"{current_humidity}%",
            "Atmospheric moisture"
        ),
        (
            "🔥",
            "HEAT INDEX",
            f"{heat_index:.1f}°C",
            "Thermal stress"
        ),
        (
            "💨",
            "WIND SPEED",
            f"{current_wind} km/h",
            "Current wind"
        ),
        (
            "⚠️",
            "RISK SCORE",
            f"{risk_score}/100",
            risk_level
        )
    ]

    for col, item in zip(
        columns,
        metrics
    ):

        with col:

            st.markdown(
                f"""
                <div class="card">

                <div style="font-size:24px;">
                {item[0]}
                </div>

                <div class="card-label">
                {item[1]}
                </div>

                <div class="card-value">
                {item[2]}
                </div>

                <div class="card-small">
                {item[3]}
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )


    # ========================================================
    # INDIA MAP
    # ========================================================

    st.markdown(
        '<div class="section">🗺️ India Climate Risk Overview</div>',
        unsafe_allow_html=True
    )

    city_rows = []

    for city, data in locations.items():

        temp = data["base"] + 4

        score, level, hi = calculate_risk(
            temp,
            data["humidity"]
        )

        city_rows.append({
            "City": city,
            "Latitude": data["lat"],
            "Longitude": data["lon"],
            "Temperature": round(temp, 1),
            "Humidity": data["humidity"],
            "Heat Index": round(hi, 1),
            "Risk Score": score,
            "Risk": level
        })

    city_df = pd.DataFrame(
        city_rows
    )

    fig = px.scatter_geo(
        city_df,
        lat="Latitude",
        lon="Longitude",
        color="Risk Score",
        size="Risk Score",
        hover_name="City",
        hover_data=[
            "Temperature",
            "Humidity",
            "Heat Index",
            "Risk"
        ],
        projection="natural earth",
        color_continuous_scale=[
            "#dcefe7",
            "#fff0d7",
            "#f8d9d9",
            "#d99aa5"
        ]
    )

    fig.update_geos(
        showcountries=True,
        countrycolor="#d7d1dd",
        showland=True,
        landcolor="#f7f5f8",
        showocean=True,
        oceancolor="#eef5f7",
        center={
            "lat": 22,
            "lon": 78
        },
        projection_scale=4.2
    )

    fig.update_layout(
        height=500,
        margin=dict(
            l=0,
            r=0,
            t=10,
            b=0
        ),
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ========================================================
    # RISK + TREND
    # ========================================================

    left, right = st.columns(2)

    with left:

        st.markdown(
            '<div class="section">🔥 Heatwave Risk Intelligence</div>',
            unsafe_allow_html=True
        )

        risk_class = {
            "LOW": "risk-low",
            "MODERATE": "risk-moderate",
            "HIGH": "risk-high",
            "EXTREME": "risk-extreme"
        }[risk_level]

        st.markdown(
            f"""
            <div class="risk-box {risk_class}">

            <div class="card-label">
            CURRENT COMPOSITE RISK
            </div>

            <div class="risk-score">
            {risk_score}
            </div>

            <div class="risk-name">
            {risk_level} RISK
            </div>

            <div>
            {selected_location}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with right:

        st.markdown(
            '<div class="section">📈 Recent Risk Trend</div>',
            unsafe_allow_html=True
        )

        recent = history.tail(18)

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=recent["Date"],
                y=recent["Risk"],
                mode="lines+markers",
                line={
                    "color": "#9d8ab7",
                    "width": 3
                },
                fill="tozeroy",
                fillcolor="rgba(157,138,183,.10)"
            )
        )

        fig.add_hline(
            y=70,
            line_dash="dash",
            annotation_text="High Risk"
        )

        fig.update_layout(
            height=250,
            margin=dict(
                l=10,
                r=10,
                t=20,
                b=10
            ),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(255,255,255,.4)"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ========================================================
    # ALERT
    # ========================================================

    if risk_level in [
        "HIGH",
        "EXTREME"
    ]:

        st.markdown(
            f"""
            <div class="alert-red">

            <b>🚨 EARLY HEATWAVE WARNING</b>

            <br><br>

            Elevated heatwave conditions detected for
            <b>{selected_location}</b>.

            <br><br>

            Composite Risk:
            <b>{risk_score}/100</b>

            <br>

            Heat Index:
            <b>{heat_index:.1f}°C</b>

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <div class="success">

            <b>✓ ENVIRONMENTAL CONDITIONS STABLE</b>

            <br><br>

            No critical heatwave alert is currently active.

            </div>
            """,
            unsafe_allow_html=True
        )


    # ========================================================
    # ANALYTICS
    # ========================================================

    st.markdown(
        '<div class="section">📊 Climate Analytics Dashboard</div>',
        unsafe_allow_html=True
    )

    g1, g2 = st.columns(2)

    with g1:

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=history["Date"],
                y=history["Temperature"],
                mode="lines",
                name="Temperature",
                line={
                    "color": "#b58b9c",
                    "width": 3
                }
            )
        )

        fig.add_hline(
            y=40,
            line_dash="dash",
            annotation_text="Heatwave Threshold"
        )

        fig.update_layout(
            title="🌡️ Long-Term Temperature",
            height=350,
            paper_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with g2:

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=history["Date"],
                y=history["Humidity"],
                mode="lines",
                name="Humidity",
                line={
                    "color": "#8ca7b7",
                    "width": 3
                }
            )
        )

        fig.update_layout(
            title="💧 Humidity Trend",
            height=350,
            paper_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ========================================================
    # CITY COMPARISON
    # ========================================================

    st.markdown(
        '<div class="section">🏙️ City Risk Comparison</div>',
        unsafe_allow_html=True
    )

    sorted_city = city_df.sort_values(
        "Risk Score",
        ascending=False
    )

    fig = px.bar(
        sorted_city,
        x="City",
        y="Risk Score",
        color="Risk Score",
        color_continuous_scale=[
            "#dcefe7",
            "#fff0d7",
            "#f8d9d9",
            "#d99aa5"
        ]
    )

    fig.update_layout(
        height=350,
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# PREDICTIVE ANALYTICS
# ============================================================

elif page == "🔮 Predictive Analytics":

    st.markdown(
        '<div class="section">🔮 Predictive Heatwave Analytics</div>',
        unsafe_allow_html=True
    )

    forecast_df = generate_forecast(
        selected_location,
        current_temperature
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Peak Temperature",
        f"{forecast_df['Temperature'].max():.1f}°C"
    )

    c2.metric(
        "Peak Probability",
        f"{forecast_df['Probability'].max()}%"
    )

    c3.metric(
        "High-Risk Days",
        int(
            forecast_df["Risk"]
            .isin(
                ["HIGH", "EXTREME"]
            )
            .sum()
        )
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=forecast_df["Day"],
            y=forecast_df["Temperature"],
            mode="lines+markers",
            line={
                "color": "#b48b9c",
                "width": 4
            }
        )
    )

    fig.add_hline(
        y=40,
        line_dash="dash",
        annotation_text="Heatwave Threshold"
    )

    fig.update_layout(
        title="7-Day Temperature Forecast",
        height=400,
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    fig2 = px.bar(
        forecast_df,
        x="Day",
        y="Probability",
        color="Probability",
        color_continuous_scale=[
            "#dcefe7",
            "#fff0d7",
            "#e8b9c1"
        ],
        title="🔥 Heatwave Probability"
    )

    fig2.update_layout(
        height=350,
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.dataframe(
        forecast_df.drop(
            columns=["Date"]
        ),
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# HISTORICAL INTELLIGENCE
# ============================================================

elif page == "📈 Historical Intelligence":

    st.markdown(
        '<div class="section">📈 Historical Climate Intelligence</div>',
        unsafe_allow_html=True
    )

    avg = history["Temperature"].mean()
    maximum = history["Temperature"].max()
    minimum = history["Temperature"].min()

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Average",
        f"{avg:.1f}°C"
    )

    c2.metric(
        "Maximum",
        f"{maximum:.1f}°C"
    )

    c3.metric(
        "Minimum",
        f"{minimum:.1f}°C"
    )

    fig = px.line(
        history,
        x="Date",
        y="Temperature",
        title="🌡️ 2020–2026 Temperature Evolution"
    )

    fig.update_layout(
        height=430,
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    history["Year"] = (
        history["Date"].dt.year
    )

    annual = (
        history
        .groupby("Year")
        ["Temperature"]
        .mean()
        .reset_index()
    )

    fig2 = px.bar(
        annual,
        x="Year",
        y="Temperature",
        title="📊 Annual Average Temperature"
    )

    fig2.update_layout(
        height=350,
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    monthly = (
        history
        .assign(
            Month=history["Date"].dt.month
        )
        .groupby("Month")
        ["Temperature"]
        .mean()
        .reset_index()
    )

    fig3 = px.line(
        monthly,
        x="Month",
        y="Temperature",
        markers=True,
        title="📅 Seasonal Temperature Pattern"
    )

    fig3.update_layout(
        height=350,
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )


# ============================================================
# CLIMATE RISK MAP
# ============================================================

elif page == "🗺️ Climate Risk Map":

    st.markdown(
        '<div class="section">🗺️ India Climate Risk Intelligence</div>',
        unsafe_allow_html=True
    )

    city_rows = []

    for city, data in locations.items():

        temp = data["base"] + 4

        score, level, hi = calculate_risk(
            temp,
            data["humidity"]
        )

        city_rows.append({
            "City": city,
            "Latitude": data["lat"],
            "Longitude": data["lon"],
            "Temperature": round(temp, 1),
            "Humidity": data["humidity"],
            "Heat Index": round(hi, 1),
            "Risk Score": score,
            "Risk": level
        })

    df = pd.DataFrame(
        city_rows
    )

    fig = px.scatter_geo(
        df,
        lat="Latitude",
        lon="Longitude",
        color="Risk Score",
        size="Risk Score",
        hover_name="City",
        hover_data=[
            "Temperature",
            "Humidity",
            "Heat Index",
            "Risk"
        ],
        projection="natural earth",
        color_continuous_scale=[
            "#dcefe7",
            "#fff0d7",
            "#f8d9d9",
            "#d99aa5"
        ]
    )

    fig.update_geos(
        showcountries=True,
        countrycolor="#d7d1dd",
        showland=True,
        landcolor="#f7f5f8",
        showocean=True,
        oceancolor="#eef5f7",
        center={
            "lat": 22,
            "lon": 78
        },
        projection_scale=4.2
    )

    fig.update_layout(
        height=600,
        margin=dict(
            l=0,
            r=0,
            t=10,
            b=0
        ),
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown(
        '<div class="section">📊 Regional Risk Ranking</div>',
        unsafe_allow_html=True
    )

    ranking = df.sort_values(
        "Risk Score",
        ascending=False
    )

    st.dataframe(
        ranking,
        use_container_width=True,
        hide_index=True
    )


    # ========================================================
    # MAHARASHTRA MAP
    # ========================================================

    st.markdown(
        '<div class="section">📍 Maharashtra Regional View</div>',
        unsafe_allow_html=True
    )

    maharashtra = df[
        df["City"].isin(
            [
                "Mumbai",
                "Pune",
                "Nagpur",
                "Surat",
                "Ahmedabad"
            ]
        )
    ]

    fig2 = px.scatter_geo(
        maharashtra,
        lat="Latitude",
        lon="Longitude",
        size="Risk Score",
        color="Risk Score",
        hover_name="City",
        hover_data=[
            "Temperature",
            "Humidity",
            "Risk"
        ],
        projection="natural earth",
        color_continuous_scale=[
            "#dcefe7",
            "#fff0d7",
            "#f8d9d9",
            "#d99aa5"
        ]
    )

    fig2.update_geos(
        showcountries=True,
        showland=True,
        landcolor="#f7f5f8",
        showocean=True,
        oceancolor="#eef5f7",
        center={
            "lat": 20,
            "lon": 75
        },
        projection_scale=12
    )

    fig2.update_layout(
        height=450,
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )


# ============================================================
# EXPLAINABLE AI
# ============================================================

elif page == "🧠 Explainable AI":

    st.markdown(
        '<div class="section">🧠 Explainable Risk Intelligence</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="ai-box">

        <h3>Why is the current risk at this level?</h3>

        The risk engine breaks the composite score into
        interpretable environmental factors.

        </div>
        """,
        unsafe_allow_html=True
    )

    factors = {
        "Temperature": 32,
        "Humidity": 18,
        "Heat Index": 21,
        "Historical Anomaly": 15,
        "Recent Trend": 14
    }

    fig = px.bar(
        x=list(factors.values()),
        y=list(factors.keys()),
        orientation="h",
        title="🧠 Risk Contribution by Factor"
    )

    fig.update_layout(
        height=400,
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown(
        """
        <div class="ai-box">

        <h3>🔍 Model Interpretation</h3>

        <br>

        <b>Temperature:</b>
        Current temperature is above the historical baseline.

        <br><br>

        <b>Humidity:</b>
        Elevated humidity increases perceived thermal stress.

        <br><br>

        <b>Heat Index:</b>
        Combined temperature and humidity indicate increased
        human heat exposure.

        <br><br>

        <b>Historical Anomaly:</b>
        Current conditions differ from expected historical
        conditions.

        <br><br>

        <b>Recent Trend:</b>
        Recent temperature movement contributes to increasing
        heatwave risk.

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# WHAT-IF
# ============================================================

elif page == "🧪 What-If Simulator":

    st.markdown(
        '<div class="section">🧪 Climate Scenario Simulator</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info">

        Modify environmental conditions and observe how
        the heatwave risk changes.

        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        scenario_temp = st.slider(
            "🌡️ Temperature",
            20.0,
            55.0,
            float(
                current_temperature + 2
            ),
            .5
        )

    with c2:

        scenario_humidity = st.slider(
            "💧 Humidity",
            10,
            100,
            int(
                current_humidity + 5
            )
        )

    with c3:

        scenario_wind = st.slider(
            "💨 Wind Speed",
            0,
            40,
            6
        )

    if st.button(
        "🧪 RUN SCENARIO"
    ):

        new_score, new_level, new_hi = calculate_risk(
            scenario_temp,
            scenario_humidity,
            scenario_wind
        )

        difference = (
            new_score -
            risk_score
        )

        a, b, c = st.columns(3)

        a.metric(
            "Current Risk",
            f"{risk_score}/100"
        )

        b.metric(
            "Simulated Risk",
            f"{new_score}/100",
            f"{difference:+d}"
        )

        c.metric(
            "Simulated Heat Index",
            f"{new_hi:.1f}°C"
        )

        if new_level in [
            "HIGH",
            "EXTREME"
        ]:

            st.markdown(
                f"""
                <div class="alert-red">

                <b>🚨 SIMULATED WARNING</b>

                <br><br>

                The simulated conditions increase
                heatwave risk to <b>{new_level}</b>.

                <br><br>

                Score:
                <b>{new_score}/100</b>

                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class="success">

                <b>✓ SIMULATION COMPLETE</b>

                <br><br>

                Simulated Risk:
                <b>{new_level}</b>

                <br>

                Score:
                <b>{new_score}/100</b>

                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# ALERT CENTER
# ============================================================

elif page == "🚨 Alert Center":

    st.markdown(
        '<div class="section">🚨 Early Warning & Alert Center</div>',
        unsafe_allow_html=True
    )

    if risk_level in [
        "HIGH",
        "EXTREME"
    ]:

        st.markdown(
            f"""
            <div class="alert-red">

            <h3>🔴 ACTIVE {risk_level} ALERT</h3>

            <b>Location:</b>
            {selected_location}

            <br>

            <b>Risk Score:</b>
            {risk_score}/100

            <br>

            <b>Heat Index:</b>
            {heat_index:.1f}°C

            <br><br>

            <b>Recommended Actions</b>

            <br><br>

            • Increase monitoring<br>
            • Notify authorities<br>
            • Prepare public warning<br>
            • Monitor vulnerable populations

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <div class="success">

            <b>✓ NO CRITICAL ALERT</b>

            <br><br>

            Current environmental conditions do not
            require a high-severity warning.

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="section">📋 Alert History</div>',
        unsafe_allow_html=True
    )

    alert_history = pd.DataFrame({
        "Timestamp": [
            "05 Oct 2026 10:30",
            "04 Oct 2026 15:20",
            "03 Oct 2026 12:45",
            "02 Oct 2026 14:10",
            "01 Oct 2026 11:35"
        ],
        "Location": [
            "Mumbai",
            "Delhi",
            "Ahmedabad",
            "Nagpur",
            "Jaipur"
        ],
        "Severity": [
            "HIGH",
            "MODERATE",
            "HIGH",
            "EXTREME",
            "MODERATE"
        ],
        "Risk Score": [
            82,
            61,
            78,
            91,
            57
        ]
    })

    st.dataframe(
        alert_history,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

    🌿 Climate Intelligence for Heatwave Monitoring,
    Prediction & Early Warning System

    <br><br>

    OOSE Functional Requirement Demonstration
    &nbsp; • &nbsp;
    Climate Risk Decision Support Platform

    </div>
    """,
    unsafe_allow_html=True
)
