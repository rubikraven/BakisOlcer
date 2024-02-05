# Yüz Tanıma ve E-posta Bildirimi

Bu proje, OpenCV ve yagmail kütüphanelerini kullanarak bir web kamerası aracılığıyla yüz tanıma işlemi yapar ve belirli bir süre boyunca yüz algılandığında belirtilen bir e-posta adresine bildirim gönderir.

## Kullanılan Araçlar ve Teknolojiler

- Python 3.10
- OpenCV (cv2)
- winsound
- pyttsx3
- yagmail

Yüz tanıma işlemi için OpenCV'nin "haarcascade_frontalface_default.xml" ve haarcascade_eye.xml dosyası kullanılmıştır. Bu dosyanın çalıştırılabilir dosyanın bulunduğu dizinde bulunması gerekmektedir.

## Kurulum ve Kullanım

Projeyi kullanmak için aşağıdaki Python kütüphanelerini kurmanız gerekmektedir:

pip install opencv-python
pip install pyttsx3
pip install yagmail


## Lisans

Bu proje, MIT lisansı altında yayınlanmıştır. Daha fazla bilgi için [LICENSE](./LICENSE) dosyasına bakınız.
