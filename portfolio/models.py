from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to= 'images/')#이미지를 받아주는 방식 
    description = models.CharField(max_length=500)

#이미지 패키지를 사용하려면 마이그레이션할 때 패키지하나를 설치해야된다
#pip install pillow 이미지를 효율적으로 사용해주는 설치해주는 라이브러리
    def __str__(self):
        return self.title