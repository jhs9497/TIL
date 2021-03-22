#### Django Auth -> 기술면접 단골 질문임!!

---

**Session**

- 서버는 수백, 수천, 수만 개의 클라이언트와 동시에 통신을 해야 한다.
- HTTP 프로토콜은 기본적으로 연결되어 있지 않고(Conectionless), 서로를 인식할 수 있는 상태 정보도 없다(Stateless).
- 서버와 클라이언트는 상태 정보를 기억하여 서로를 식별하게끔 만들 수 있다. (=> 세션을 유지하도록 만든다.)

**Cookie**

- **세션을 유지하는 방식** 중 가장 널리 사용되는 방식
- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각 (MDN)

- 브라우저는 데이터 조각들을 저장해 두었다가, 동일한 서버의 다른 페이지에 요청할 때마다 데이터 조각을 함께 보낸다.
- 쿠키의 종류 (=>'파기시점의 유무')
  - Session Cookie: 브라우저를 닫으면 삭제되는 쿠키
  - Permanent(Persistent) Cookie: 브라우저를 닫거나 컴퓨터를 재시작해도 남아있는 쿠키





Session

- Create : login
- Delete : logout

User

- Create : signup
- Update : update
- Delete : delete