import json
import yfinance as yf

def lambda_handler(event, context):
    #get request body
    body = json.loads(event["body"])
    
    #create ticker
    ticker = yf.Ticker(body["symbol"])
    
    #get price history
    history = ticker.history(period=body["period"], interval=body["interval"])
    
    #convert df to json
    result = history.to_json(orient="index", date_format="iso")
    
    return {
        'statusCode': 200,
        'body': result,
        'headers': {
            "Access-Control-Allow-Origin" : "*", # Required for CORS support to work
            "Access-Control-Allow-Credentials" : bool(True) # Required for cookies, authorization headers with HTTPS
        },
    }
