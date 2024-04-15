# Kubook Backend

## Overview
**Kubook**은 고려대학교 중앙 컴퓨터 동아리 KUCC의 컴퓨터 서적 200여 권을 관리하고, 동아리 부원들에게 도서관 서비스를 제공하는 시스템입니다. 이 리포지토리는 쿠책책의 백엔드 코드를 담고 있습니다.

목적:
- **도서 관리자**: 도서 구매, 알림, 공지사항 관리
- **일반 부원**: 도서 대출, 예약, 리뷰 작성

## Features
- **사용자 인증 및 회원가입**
- **도서 검색 및 상세 정보 조회**
- **대출, 반납 및 예약**
- **리뷰 작성 및 조회**
- **구매 요청 및 관리자 알림**
- **도서 및 사용자 관리 (관리자 전용)**

## Technologies Used
| Category        | Technology                                    |
|-----------------|-----------------------------------------------|
| Framework       | [FastAPI](https://fastapi.tiangolo.com/)      |
| Language        | Python 3.10                                   |
| Database/ORM    | MySQL, SQLAlchemy                             |
| Cloud           | Kakao Cloud - MySQL                           |
| Tools           | ngrok, Swagger, Channel Talk, MySQL Workbench |
| Authentication  | Firebase Authentication                       |
| Design          | [ERDCloud (ERD)](https://www.erdcloud.com/d/nSaQY4NjMcnwcQ3CM) |

## Installation and Setup
1. **클론**:
   ```bash
   git clone https://github.com/kucc/kubook-backend
   ```
2. **가상 환경 설정**:
   ```bash
   cd src
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```
3. **의존성 설치**:
   ```bash
   pip install -r requirements/prod.txt
   ```
4. **데이터베이스 설정**:
   - `database.py` 파일에서 연결 정보 업데이트
5. **Firebase 설정**:
   - Firebase 프로젝트 생성 후 인증 정보 확보
   - `firebase_admin` 초기화
6. **서버 실행**:
   ```bash
   uvicorn main:app --reload
   ```

## Usage
- 애플리케이션 실행 후 `http://localhost:8000/docs`에 접속하여 API 문서를 확인할 수 있습니다.

## Screenshots
- 추가 예정

## Team
<table>
  <tr>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/75142329?v=4" width="200px;" alt=""/><br /><sub><b>권

민재</b></sub><br /><a href="https://github.com/mjkweon17">Auth, Search, Users CI/CD</a></td>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/76930385?v=4" width="200px;" alt=""/><br /><sub><b>한수빈</b></sub><br /><a href="https://github.com/smreosms13">ORM, Admins, Schemas</a></td>
  </tr>
</table>

## Contact
- **프로젝트 문의**: [mjkweon17@korea.ac.kr](mailto:mjkweon17@korea.ac.kr)
- **피드백**: [mjkweon17@korea.ac.kr](mailto:mjkweon17@korea.ac.kr)

## Acknowledgements
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Firebase Authentication](https://firebase.google.com/docs/auth)
- [JWT](https://jwt.io/)
- 그 외 도움을 준 모든 오픈소스 프로젝트 및 개인에게 감사합니다.