## Encrypted ZIP
Sepertinya ZIP yang diberikan berpassword. Mari kita cari tau cara membukanya.

## Hint<sup>*</sup>
- USB Keyboard
- Exif

<sup>*</sup> Kalau kepepet banget

## Deployment

Peserta diberi encrypted.zip & usb_log.pcap

## Flag

KOMATIKCTF{USB_Keyboard_NOICE}

## How to solve

- cek zip -> password needed 
- buka usb_log.pcap -> usb keyboard
- buat script HID Keyboard parser, bisa cari di internet banyak
- dapet deh passwordnya
- unzip
- masih belum dapet flag
- check exif dari gambar
- voila  

solver USB Parser:
  ```shell
  tshark -r <file-pcap> -Y 'usbhid.data' -T fields -e usbhid.data | sed 's/../&:/g; s/ $//' > usbhid.txt
  python usbkeyboard_solver.py usbhid.txt
  ```