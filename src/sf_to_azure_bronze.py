import os
import pandas as pd
import numpy as np
from simple_salesforce import Salesforce
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
from io import StringIO
from datetime import datetime


load_dotenv()

try:
    # 1. Salesforce Extraction
    sf = Salesforce(username=os.getenv('SF_USER'), password=os.getenv('SF_PASS'), security_token=os.getenv('SF_TOKEN'))
    query = "SELECT Name, Amount, StageName, CloseDate, Probability FROM Opportunity"
    results = sf.query_all(query)
    df = pd.DataFrame(results['records']).drop(columns='attributes')

    # 2. Scramble Logic (Vectorized with NumPy)
    # Amount Variance: +/- 10%
    amt_variance = np.random.uniform(0.9, 1.1, size=len(df))
    df['Amount'] = (df['Amount'] * amt_variance).round(2)
    
    # Probability Variance: +/- 5% (capped at 100)
    prob_variance = np.random.uniform(-5, 5, size=len(df))
    df['Probability'] = (df['Probability'] + prob_variance).clip(lower=0, upper=100).round(1)
    
    print(f"🎲 Scrambled {len(df)} records (Revenue +/-10%, Prob +/-5%).")

    # 3. Azure Cloud Ingestion (Bronze Layer)
    timestamp = datetime.now().strftime('%Y-%m-%d_%H%M')
    blob_name = f"{timestamp}_revenue_bronze.csv"
    
    blob_service_client = BlobServiceClient.from_connection_string(os.getenv('AZURE_CONNECTION_STRING'))
    blob_client = blob_service_client.get_blob_client(container="bronze", blob=blob_name)

    output = StringIO()
    df.to_csv(output, index=False)
    blob_client.upload_blob(output.getvalue(), overwrite=True)

    print(f"☁️ Success! Uploaded to Azure: bronze/{blob_name}")

except Exception as e:
    print(f"❌ Pipeline failed: {e}")