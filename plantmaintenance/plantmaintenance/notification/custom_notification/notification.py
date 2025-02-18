import frappe
import requests
import json


@frappe.whitelist()
def send_onesignal_notification(email,contents,urlm):
    url = "https://api.onesignal.com/notifications?c=push"
    formatted_contents = f"{contents} Click here to view: {urlm}"


    payload = {
        "app_id": "53a209a0-ad8d-4072-ad67-e1c1919ca14f",
         "contents": {
            "en": formatted_contents
    },
   
    "include_external_user_ids": [email],
    
    }
   
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Basic ZmFiYjJlZjgtOGRiZS00MWUzLWE1ZDktYjMxOWVlZGQ3OTNm"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(response.text)

    if response.status_code == 200:
        return "Notification sent successfully."
    else:
        frappe.throw("Failed to send notification.")
        
   