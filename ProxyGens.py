import requests

# Kullanıcıdan proxy tipini al
proxy_type = input("Proxy tipini seçin (http/https/socks4/socks5): ")

# Kullanıcıdan proxy tipini al
ip_version = input("IP versionunu seçin (ipv4/ipv6): ")

# Proxy listesini al
proxy_list = []
try:
    response = requests.get(f"https://api.proxyscrape.com/?request=displayproxies&proxytype={proxy_type}&protocol={ip_version}")
    proxy_list = response.text.split('\r\n')
except:
    print("Proxy listesi alınamadı")

# Proxy listesini ve açık/kapalı durumlarını txt dosyasına yazdır
with open("proxy_list.txt", "w") as file:
    for proxy in proxy_list:
        try:
            response = requests.get("http://" + proxy, timeout=5)
            if response.status_code == 200:
                file.write(proxy + " - AÇIK\n")
            else:
                file.write(proxy + " - KAPALI\n")
        except:
            file.write(proxy + " - KAPALI\n")
    print("Proxy listesi ve açık/kapalı durumları txt dosyasına yazdırıldı")
