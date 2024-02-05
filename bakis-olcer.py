import cv2
import winsound
import pyttsx3
import yagmail

# mail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "gönderenin email adresi"
SMTP_PASSWORD = "gönderenin mail şifresi"

# gönderilecek mail adresi
MAIL_TO = "Göndericek mail adresi"

yag = yagmail.SMTP(SMTP_USERNAME, SMTP_PASSWORD)

# ses ve konuşma
engine = pyttsx3.init()
engine.setProperty('voice', 'Turkish')
engine.setProperty('rate', 195)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

webcam = cv2.VideoCapture(0)

start_time = 0

while True:

    success, frame = webcam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
           

    if len(faces) > 0:

        elapsed_time = cv2.getTickCount() - start_time

        remaining_time = 10 - elapsed_time / cv2.getTickFrequency()

        cv2.putText(frame, f"Bakis suresi: {remaining_time:.2f} saniye", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 255), 2)

        if elapsed_time / cv2.getTickFrequency() > 10:
            winsound.Beep(2000, 500)
            cv2.putText(frame, "Supheli davranis!", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            engine.say("kapıyı izleyen biri var!")
            print("kapıyı izleyen biri var")
            engine.runAndWait()

            # İmajı kaydet
            cv2.imwrite("webcam.jpg", frame)

            yag.send(to=MAIL_TO, subject="Izlenme Uyarısı", contents=["webcam.jpg"])
    else:
        start_time = cv2.getTickCount()
        print("kapıyı izleyen biri yok")

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()
