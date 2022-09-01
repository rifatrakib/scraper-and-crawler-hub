import requests
from hyper.contrib import HTTP20Adapter


def include_page_headers():
    headers = {
        ":authority": "formsdss-v3.uk.barclays",
        ":method": "POST",
        ":path": "/dss/service/co.uk/mortgages/costcalculator/productservice",
        ":scheme": "https",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,ar-AE;q=0.6,ar;q=0.5,bn-BD;q=0.4,bn;q=0.3",
        "action": "default",
        "content-length": "203",
        "content-type": "application/json",
        "currentstate": "default_current_state",
        "referer": "https://www.barclays.co.uk/",
        "origin": "https://www.barclays.co.uk",
        "sec-ch-ua": '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    }
    return headers


def create_http2_session(url):
    session = requests.Session()
    adapter = HTTP20Adapter(headers=include_page_headers())
    session.mount(url, adapter=adapter)
    return session


def get_mortgage_information(estimated_property_value, repayment_amount, months):
    url = "https://formsdss-v3.uk.barclays/dss/service/co.uk/mortgages/costcalculator/productservice"
    session = create_http2_session(url)
    
    data = {
        "header": {"flowId": "0"},
        "body":{
            "wantTo": "FTBP",
            "estimatedPropertyValue": estimated_property_value,
            "borrowAmount": repayment_amount,
            "interestOnlyAmount": 0,
            "repaymentAmount": repayment_amount,
            "ltv": round(repayment_amount / estimated_property_value * 100),
            "totalTerm": months,
            "purchaseType": "Repayment"
        }
    }
    
    r = session.post(url, json=data)
    results = r.json()
    
    return results


estimated_property_value = 200000
repayment_amount = 150000
months =240

data = get_mortgage_information(estimated_property_value, repayment_amount, months)
print(data)
