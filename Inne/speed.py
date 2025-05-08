import speedtest
import speedtest_cli

def speed_test():
    try:
        # Inicjalizacja testera prędkości
        test = speedtest.speedtest()

        # Pobieranie listy serwerów i wyboru najlepszego
        test.get_best_server()

        # Testowanie prędkości pobierania
        download_speed = round(test.download() / 10**6, 2)  # konwersja na Mbps

        # Testowanie prędkości wysyłania
        upload_speed = round(test.upload() / 10**6, 2)  # konwersja na Mbps

        # Testowanie ping
        server = test.get_best_server()
        ping = round(server['latency'], 2)

        # Wyświetlanie wyników
        print(f"Download speed: {download_speed} Mbps")
        print(f"Upload speed: {upload_speed} Mbps")
        print(f"Ping: {ping} ms")

    except Exception as e:
        print(f"Error during speed test: {e}")

# Uruchamianie funkcji testu
speed_test()

