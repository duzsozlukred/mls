import socket

def web_sitesi_ip_bul(web_sitesi):
  """
  Web sitesinin IP adresini ping atarak bulan fonksiyon.

  Parametreler:
    web_sitesi: Web sitesinin URL'si.

  Dönüş Değeri:
    Web sitesinin IP adresi.
  """

  try:
    # Web sitesinin IP adresini alır.
    ip_adresi = socket.gethostbyname(web_sitesi)

    # Ping atarak IP adresinin geçerli olup olmadığını kontrol eder.
    socket.gethostbyaddr(ip_adresi)

    return ip_adresi

  except socket.gaierror:
    # Web sitesi bulunamadı.
    return None

# Kullanıcıdan web sitesini ister.
web_sitesi = input("Web sitesinin URL'sini girin: ")

# IP adresini bulur.
ip_adresi = web_sitesi_ip_bul(web_sitesi)

# Sonucu yazdırır.
if ip_adresi is None:
  print(f"{web_sitesi} web sitesi bulunamadı.")
else:
  print(f"{web_sitesi} web sitesinin IP adresi: {ip_adresi}")
