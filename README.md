# Tech Spec

TECH SPEC [FED App](https://south-sunshine-1a6.notion.site/FED-7e9dbb96be18422ab8becf127a5fa367?pvs=4)


### Poetry 

- 하나의 가상환경
- `poetry env use 3.11` 명령어를 통해 FED 프로젝트 python 버전인 3.11 버전으로 세팅해준다.
- `poetry install` 명령어를 통해 기존에 설정해둔 패키지를 설치한다.
- `poetry add` 명령어를 통해 패키지를 추가할 수 있다.

- 인터프리터 변경을 통해 3.11 버전을 꼭 확인하여 작업을 진행하도록 한다.

### add package to using mysql  
- `poetry add SQLAlchemy mysqlclient PyMySQL 'databases[mysql]'`