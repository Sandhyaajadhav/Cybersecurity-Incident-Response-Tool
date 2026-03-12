def detect_threat(activity):

    if "Phishing" in activity:
        return "High Risk Threat Detected"

    elif "Malware" in activity:
        return "Critical Threat Detected"

    elif "Brute Force" in activity:
        return "Unauthorized Access Attempt"

    elif "Suspicious" in activity:
        return "Network Anomaly Detected"

    else:
        return "Safe"