# python-http-header

Python example for read &amp; send http header

## Usage

Simple http request

```bash
$ python3 send-http-request.py https://www.ziemers.de/fhtw/web/ms/ms1header1.html
```

Return:

```bash
Target Site: https://www.ziemers.de/fhtw/web/ms/ms1header1.html
##############################
#    http request content    #
##############################

+--------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| http header                    | value                                                                                                                    |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| User-Agent                     | python-requests/2.18.4                                                                                                   |
| Accept-Encoding                | gzip, deflate                                                                                                            |
| Accept                         | */*                                                                                                                      |
| Connection                     | keep-alive                                                                                                               |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------+

##############################
#    http headers content    #
##############################

+--------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| http header                    | value                                                                                                                    |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Date                           | Wed, 01 Nov 2017 17:59:27 GMT                                                                                            |
| Content-Type                   | text/html                                                                                                                |
| Transfer-Encoding              | chunked                                                                                                                  |
| Connection                     | keep-alive                                                                                                               |
| X-XSS-Protection               | 1; mode=block                                                                                                            |
| X-Frame-Options                | sameorigin                                                                                                               |
| Content-Security-Policy        | report-uri https://www.ziemers.de/rest/api/csp/report                                                                    |
| Strict-Transport-Security      | max-age=15552000                                                                                                         |
| SecretHeader                   | MySecretHttpHeader                                                                                                       |
| Server                         | NanomeCMS/4.3.1.454                                                                                                      |
| Set-Cookie                     | IDHTTPSESSIONID=hMePoBLJtfjytnP; path=/, NANOMESESSIONID=3F34D8BB-8E07-47C8-9FE0-3859D4B4EC95; path=/                    |
| Content-Encoding               | gzip                                                                                                                     |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------+
```

Simple http request with custom request heaers

```bash
$ https://www.ziemers.de/fhtw/web/ms/ms1header2.html SecretHeader MySecretHttpHeader
```

Return: 

```bash
Target Site: https://www.ziemers.de/fhtw/web/ms/ms1header2.html
##############################
#    http request content    #
##############################

+--------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| http header                    | value                                                                                                                    |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| User-Agent                     | python-requests/2.18.4                                                                                                   |
| Accept-Encoding                | gzip, deflate                                                                                                            |
| Accept                         | */*                                                                                                                      |
| Connection                     | keep-alive                                                                                                               |
| SecretHeader                   | MySecretHttpHeader                                                                                                       |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------+

##############################
#    http headers content    #
##############################

+--------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| http header                    | value                                                                                                                    |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Date                           | Wed, 01 Nov 2017 18:01:38 GMT                                                                                            |
| Content-Type                   | text/html                                                                                                                |
| Transfer-Encoding              | chunked                                                                                                                  |
| Connection                     | keep-alive                                                                                                               |
| X-XSS-Protection               | 1; mode=block                                                                                                            |
| X-Frame-Options                | sameorigin                                                                                                               |
| Content-Security-Policy        | report-uri https://www.ziemers.de/rest/api/csp/report                                                                    |
| Strict-Transport-Security      | max-age=15552000                                                                                                         |
| SecretPassword                 | CongratulationsYouDidIt                                                                                                  |
| Server                         | NanomeCMS/4.3.1.454                                                                                                      |
| Set-Cookie                     | IDHTTPSESSIONID=St11XhbXvfl5vuv; path=/, NANOMESESSIONID=8F9ECB15-983A-45B5-A9A4-C053DD381D52; path=/                    |
| Content-Encoding               | gzip                                                                                                                     |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------+
```