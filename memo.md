### 로그 관련
- logging.conf
    - 로거, 핸들러, 포매터 등의 설정을 정의
- logs 폴더
    - 로그 파일 저장되는 곳
- logging_config.py
    - 로깅 모듈
    - 로깅 설정 로드하고 초기화하는 코드 작성

### 테스트 관련
- tests 폴더
    - 모든 테스트 파일 저장하는 곳
    - test_users.py 처럼 추가하면 됨
    - conftest.py: 공통 테스트 파일의 설정
    - data 폴더
        - 테스트에 사용될 샘플 데이터 파일 저장
    - integration 폴더
        - 모듈별로 통합 테스트 수행
- coveragerc: 테스트 커버리지 측정과 관련된 설정 지정