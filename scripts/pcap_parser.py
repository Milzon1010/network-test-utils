import os  # ✅ Tambahkan ini
import pyshark
import pandas as pd

def parse_pcap(file_path):
    cap = pyshark.FileCapture(file_path, display_filter="udp")

    parsed_data = []
    for pkt in cap:
        try:
            parsed_data.append({
                'timestamp': pkt.sniff_time,
                'src_ip': pkt.ip.src,
                'dst_ip': pkt.ip.dst,
                'src_port': pkt[pkt.transport_layer].srcport,
                'dst_port': pkt[pkt.transport_layer].dstport,
                'protocol': pkt.transport_layer
            })
        except AttributeError:
            continue

    # Convert to DataFrame
    df = pd.DataFrame(parsed_data)

    # ✅ Buat folder output kalau belum ada
    os.makedirs("output", exist_ok=True)

    # ✅ Save hasil ke CSV
    df.to_csv('output/parsed_udp_packets.csv', index=False)
    print(f"✅ Parsed {len(parsed_data)} packets. Saved to output/parsed_udp_packets.csv")

# Tambahkan pemanggilan fungsi
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("❌ Usage: python pcap_parser.py <path_to_pcap>")
    else:
        parse_pcap(sys.argv[1])
