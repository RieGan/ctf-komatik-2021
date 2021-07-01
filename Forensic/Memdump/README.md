## Memory Dump
No comment

## Hint
needed python2.7 module:
- pycrypto==2.6.1
- construct==2.5.5
- distorm3==3.5.2



## Deployment

Peserta diberi memdump.7z \
link: https://bit.ly/3dRZEIL or https://mega.nz/file/uywjiI5L#839wVGl0kdAHOPgWuaUGpEF20zU1AW4Q4ZQJ5lEvZAY

## Flag

KOMATIKCTF{M3mory_DuMp_FoR3nsic}

## How to solve
- pakai volatility
- imageinfo => profile Win7SP1x86
- analisis, terserah intinya ketemu clue di notepad
- flag ada di password
- pake plugin mimikatz
- command:  
  `python volatility/vol.py --plugin=./volatility/plugin/ -f memdump.vmem --profile=Win7SP1x86 mimikatz`
