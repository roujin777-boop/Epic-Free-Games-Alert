# pip install requests
import os
import requests

def main():
    webhook = os.getenv("DISCORD_WEBHOOK_URL", "").strip()
    if not webhook:
        raise SystemExit("DISCORD_WEBHOOK_URL が未設定です")

    payload = {"content": "[PayPay] お年玉 https://pay.paypay.ne.jp/LxwBqqG4fEB0ZwUc"}  # 固定文言
    r = requests.post(webhook, json=payload, timeout=10)
    r.raise_for_status()
    print("Posted:", r.status_code)

if __name__ == "__main__":
    main()
