


import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from flask import Flask, render_template, request

app = Flask(__name__)

# Define your Google Docs API credentials (replace with your own)
credentials = service_account.Credentials.from_service_account_info(
    {
        "type": "service_account",
  "project_id": "driven-heading-398505",
  "private_key_id": "596befae2fef4036f4754a12e2906bfe828e19b7",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDtYIBjwkk7M0kT\nZFoXxIKoj7JghEWQmDR6twnV2474RAzvE/wEsq5jcjMo437zB7vd8/YROeTlA57f\nd4/lRiDTrnG3CivpCYDD0JOczjOIM2tdPz7oCYqcxk0VrzU6rhv1JnFK98KYD1tm\nfgv+gKXsYu1JWBzNwxv41MvjBUTIVDft5rgtUuSXnpW62fJ9AtyOpAHNlSXRuPVI\nbXsWG27Gi83ODNVY8twsGOb+l1C2qYkEU1AxgnhDQTleB6jpSrZQyIH8snnauHKq\nStv2SKjjRQn79Wa/ds81PsktIRux22iO41xMChP3BxyC94I9MB3kNQ2pZ/BqrSuU\nc9KPLL8/AgMBAAECggEAAOdJ+nvlydauVaUwifb6odvECvAcxl2vvEd5e7oJ7zLv\nJvi4GJ1hWgV6X/dDc592KPA3YFpOnoSo3/BTNdwYztrXQLk1JHQfrqTdwUE7y8Oc\nRRd8ZeXfFZexvPFSt9hYc/lhNqCNTJrRdbM26ekQvlubM7Ago08Kh6EuiztU9UK5\nH/euU86PHXtIyjfYToIf/6230zVgbBTZ/dJalU3p+CSKQX1N0ASGKTDYKUlmb65b\n69O1Vv7C+yPFW/7+xhqlmAbRZV764gWeaki+GCCo/UqRon5WiVkvD7gCi2N4fB+k\nMO/kemhBCv+n/RxzHby4yrbuPg9Zs/l12doWDxlKQQKBgQD3EZSFiLITrwocTMRj\nMrKMLLvAS41MumkenXyQ3n7+p8wigBTaI4Nub+OuVEsqLT8YHRPmUHMCjbmiaE9b\noYNAr4HIIujs6Tfi+QZ0e2MsuJDjX1wkNj7Qemo6QP27zziX5pO0XPDhvsLXEEWP\nt3kQLC1hWpaMTGf5JGX1I507TQKBgQD19TuAPtcys0lPV9h7BjoLjmjnWVwJx6Ln\n8WPoK2KCz+1FW8wMKha0zvDzaSIXUAC2hjWi+ekVkXLIL1Ypmowg37k6Hji7DlLR\nG0yYZzvLNSqZETvEGm8cPyaN1URkc/z90idpVUEbI7cC7kdBRoEHAmSyKf0taeY9\ntNi6EhkmuwKBgQD24VNGx9whvSPeOXt4ID23wi9uLFCqXg8Sb438eMfvkR5zTwcH\nHruDjDy3gzWElKfaYZvz5Wm3IIVhWtgJmO+9oGKP6QpVSYn1vJ8NoAnusxLckPpS\nmP3Vdq1VPoIMvDkx2E65yLFO8j5hhrnrrQtE9M/32vxafzLaCtvyw76mdQKBgEqi\nmuakqwqwiutvvbo/PnfpQ/4ICLzS/qUhg+6c06zcSaTFYVrDntZJAabrXTPzy/OX\nMEl/SnKIC2uhqaTASAtluEBhkVd51jmr7gdFNEjKnl2KdDdiyhqpMxrQ/4r4A2pG\nTj1RaItCwDM8eRTevyKQYFwMD86rFvncmfOEsGsnAoGAI2ODAtmzITZo70YLwxiC\nQfthjU7mJPUGXLXKgGwiB2sWT3LviTXFOhhggg1D6D4WBwZo60qyqnO894+VUMof\ny3Ix95L4tZRqwNw5Z/a6/y0wzZy+9iNHlOeJNxcDEmJS5TEpWqrJ0Bfj+itRvOA7\nCE8WsUjXMnWWDqzcuuLRjGY=\n-----END PRIVATE KEY-----\n",
  "client_email": "legal-doc@driven-heading-398505.iam.gserviceaccount.com",
  "client_id": "116769058891939754916",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/legal-doc%40driven-heading-398505.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
    },
    scopes=['https://www.googleapis.com/auth/documents']
)

# Create a Google Docs API service object
service = build('docs', 'v1', credentials=credentials)

# Specify the document ID of your Google Doc
document_id = '1kGqiSf-u84ufxNvH6jDubPMn-7pTX9ZjddqB0UOqF1s'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission
        user_text = request.form['userText']

        # Get the content of the Google Doc
        doc = service.documents().get(documentId=document_id).execute()
        content = doc.get('body').get('content')

        # Clear the existing content of the Google Doc
        clear_requests = []
        for i in range(len(content)):
            clear_requests.append({
                'deleteContentRange': {
                    'range': {
                        'startIndex': 1,  # Start from the second element to avoid deleting the document title
                        'endIndex': len(content),
                    }
                }
            })

        # Create a new paragraph with the user's input text
        user_paragraph = {
            "paragraph": {
                "elements": [{"textRun": {"content": user_text}}]
            }
        }

        # Append the user's input text as a new paragraph to the Google Doc
        append_requests = [
            {
                'insertText': {
                    'location': {
                        'index': 1,  # Insert at the beginning of the document
                    },
                    'text': user_text,
                },
            }
        ]

        # Batch update the Google Doc to clear existing content and append the user's input text
        requests = clear_requests + append_requests
        service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()

        return render_template('result.html', result_text="User's input has replaced the existing content in the Google Doc.")

    # If it's a GET request or the form hasn't been submitted yet, render the initial HTML form
    return render_template('/Users/sandeepkg/Downloads/templates/index.html')

if __name__ == '__main__':
    app.run(debug=True)
