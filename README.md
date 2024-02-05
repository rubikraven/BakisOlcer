Bakış Algılayıcı

Bu Python projesi, bir evin kapısına veya penceresine keşif amaçlı olarak yaklaşık 10 saniye süreyle bakan kişileri algılayan bir sistemdir. Eğer bir kişi belirlenen süre boyunca bakışını devam ettirirse, sistem bu durumu algılar, sesli bir uyarı verir ve bu kişinin fotoğrafını çeker. Ayrıca, fotoğrafı bir e-posta olarak belirlenen alıcıya gönderebilir.
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
pip install winsound


## Lisans

Bu proje, MIT lisansı altında yayınlanmıştır. Daha fazla bilgi için [LICENSE](./LICENSE) dosyasına bakınız.
