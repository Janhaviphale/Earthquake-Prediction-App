from sklearn.ensemble import IsolationForest

def detect_anomalies(df):

    features = df[['magnitude', 'depth']]

    model = IsolationForest(
        contamination=0.05
    )

    df['anomaly'] = model.fit_predict(features)

    return df