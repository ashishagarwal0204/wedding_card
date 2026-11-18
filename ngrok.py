from pyngrok import ngrok, conf
import time

ngrok.set_auth_token("3A6idFrU5sukM9EfsJkXay1ysgC_3DSiJji6RUnRvyfnJZ8Q3")

public_url = ngrok.connect(5173, pooling_enabled=True)
print("Public URL:", public_url)

try:
    # Keep the script alive
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Shutting down ngrok...")
    ngrok.disconnect(public_url)