from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 : {self.name}'


class Patient(models.Model):
    name = models.TextField()
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    # 원래는 역참조로 patient_set을 사용해야하는데 <-- 이름을 patients로 바꿔버린 것
    # doctor1.patient_set.add(patient2) -> doctor1.patients.add(patient2)로 이용가능
    # patient입장에선 doctors라고 변수잡혀 있으므로 patient1.doctors.add(doctor1)

    # 중개에 필드 추가하고 사용해야할 때
    # doctors = models.ManyToManyField(Doctor, through=Reservaiton)

    def __str__(self):
        return f'{self.pk}번 환자 : {self.name}'


# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.doctor_id}번 의사 : {self.patient_id}번 환자'
    


    
    