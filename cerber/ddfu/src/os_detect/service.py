import select
import socket
import struct

from print_color import print

from cerber.utils import Logger


class OSDetector:
    def __init__(self):
        self.os_ttl_map = {
            32: "Windows 95/98/ME",
            64: "Linux/Unix",
            128: "Windows NT/2000/XP/7/8/10",
            255: "Solaris/AIX",
        }

    def _send_icmp_ping(self, target_ip: str):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            sock.settimeout(2)

            packet_id = 12345
            packet_seq = 1
            packet_checksum = 0
            packet = struct.pack(
                "!BBHHH", 8, 0, packet_checksum, packet_id, packet_seq
            )

            packet_checksum = self._checksum(packet)
            packet = struct.pack(
                "!BBHHH", 8, 0, packet_checksum, packet_id, packet_seq
            )

            sock.sendto(packet, (target_ip, 1))

            ready = select.select([sock], [], [], 2)
            if ready[0]:
                response_packet, _ = sock.recvfrom(1024)
                ttl = response_packet[8]
                return ttl
            else:
                return None
        except OSError as e:
            Logger.error(f"for OS detected requires root privileges")
            exit(-1)
        except Exception as e:
            return None
        finally:
            try:
                sock.close()
            except:
                pass

    def _checksum(self, packet):
        sum = 0
        count_to = (len(packet) // 2) * 2
        for count in range(0, count_to, 2):
            sum += (packet[count] << 8) + packet[count + 1]

        if count_to < len(packet):
            sum += packet[count_to] << 8

        sum = (sum >> 16) + (sum & 0xFFFF)
        sum += sum >> 16
        return ~sum & 0xFFFF


    def detect_os(self, target_ip):
        ttl = self._send_icmp_ping(target_ip)
        if ttl is None:
            return [None, -1]

        for ttl_value, os_type in self.os_ttl_map.items():
            if ttl <= ttl_value:
                return [os_type, ttl]

        return [None, -1]

    def run(self, target_ip):
        os, ttl = self.detect_os(target_ip)
        if os:
            print(f"{target_ip} -> {os}", color='c', tag="success", tag_color='g')
        else:
            print(f"{target_ip} not detect os", color='c', tag="fail", tag_color='r')