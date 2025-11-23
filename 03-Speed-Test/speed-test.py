import speedtest
print("Testing speed...")
st = speedtest.Speedtest()
print(f"Download: {st.download()/1024/1024:.2f} Mbps")
print(f"Upload: {st.upload()/1024/1024:.2f} Mbps")
print(f"Ping: {st.results.ping:.2f} ms")