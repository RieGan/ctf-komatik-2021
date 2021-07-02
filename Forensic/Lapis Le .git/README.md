## Lapis Le .git
Dari judulnya sih lapis le .git

## Hint

## Deployment

Peserta diberi lapislegit.zip

## Flag

KOMATIKCTF{G1t_R3s3t_l0op}

## How to solve
- cek zip
- ada .git
- bisa pake tool git atau manual checkout checkout ke commit sebelumnya
- ternyata flag terpisah setiap karakter pada satu commit
- scripting :
  ```text
  loop sampe habis:
    rollback ke commit sebelumnya
        -> command: git reset --hard HEAD~1
    read file flag.txt terserah pake apa
    gabungin read tadi
    reverse text
    dapet flag
    ```
- solver:
  `lapislegit_solver.py`