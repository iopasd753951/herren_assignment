# Herren_assignment


### API Spec

| http Method | Path | Header | Args | Body | Description |
| :---: | :---: | :---: | :---: | :---: | :---: | 
| GET | api/v1/account/signup | | | | 유저 계정 보기 |
| POST | api/v1/account/signup | | |  {email: email type, name: char type, password: char type} | 유저 생성 |
| UPDATE | api/v1/account/signup/{pk: int} | {Authorization: Token examtokenstring} | | {email: email type, name: char type, password: char type} | 유저 정보 변경 |
| DELETE | api/v1/account/signup/{pk: int} | {Authorization: Token examtokenstring} | | | 유저 계정 삭제 |
| GET | api/v1/account/mail-list | {Authorization: Token examtokenstring} | | | 유저 메일링 리스트 보기 |
| POST | api/v1/account/mail-list | {Authorization: Token examtokenstring} | | {added_email: email type} | 유저 메일링 리스트 추가 |
| DELETE | api/v1/account/mail-list/{pk: int} | {Authorization: Token examtokenstring} | | | 유저 메일링 리스트의 선택된 메일 삭제 |
| GET | api/v1/mail/mail-system | | ?email=str | | 수신함 확인 |
| POST | api/v1/mail/mail-system | | | {mailto: email type, subject: char type, content: char type} | 메일 발신 |

