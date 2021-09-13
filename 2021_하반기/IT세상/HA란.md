## HA란 ? High Aailability(고가용성)

- 서버와 네트워크, 프로그램 등의 정보 시스템이 오랜 기간 동안 지속적으로 정상 운영이 가능한 성질 
  - -> 시스템에서 이슈 발생 시, 얼마나 빠른 시간 내에 복구가 가능한지에 대한 척도



- Active
  - Client로부터 request를 받아서 처리하는 역할
  - 실제 구동중인 서버
- Standby
  - 예측한 이벤트 (장애 등)가 발생했을 때, Active 대신 request를 처리하는 역할
  - Active를 감시하며 Active가 처리하기 힘들다고 판단됐을 때 Stanby 서버가 on 됨

🚩Active와 Stanby 서버는 기능이 거의 비슷하고 서로 미러링을 하고 있다. 



- Master
  - 하나의 역할을 수행 한느데 있어 동작의 주체가 되는 역할을 수행
  - 현재 Active 상태
- Slave
  - '주로' 마스터의 지시에 따라, 종속적인 역할을 수행
  - Slave는 확장이 가능하다
  - 현재 Active 상태
- Backup
  - 특정 서버의 역할을 대체하기 위해, 준비된 서버
  - Stanby와 같은 기능





## 예시

#### Cache server의 이중화 구성

- 캐시서버란 ..  ?

- Cache server의 다운 발생 시, 대체할 수 있는 미러링 서버를 구성



#### MySQL에서 Replication 구성

- Master와 Slave는 dedicated storage 사용하여 async 방식으로 데이터 복제
- Master에서 CRUD의 CUD를 담당하고, Slave에서 R을 담당
- Slave 서버는 Scale-out이 쉽게 가능 (1:N)



## High Availability 방식

- 클러스팅
  - 각기 다른 서버들을 하나로 묶어서 하나의 시스템같이 동작하게 함으로써, 고가용성의 서비스를 제공
- 로드밸런싱
- RAID (Redundant Array of independent Disks)