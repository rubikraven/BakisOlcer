import cv2
import winsound
import pyttsx3
import yagmail

# mail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "gönderenin email adresi"
SMTP_PASSWORD = "gönderenin mail şifresi"

# Gönderilecek mail adresi
MAIL_TO = "gönderilen email adresi"

yag = yagmail.SMTP(SMTP_USERNAME, SMTP_PASSWORD)

# ses ve konuşma
engine = pyttsx3.init()
engine.setProperty('voice', 'Turkish')
engine.setProperty('rate', 195)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

webcam = cv2.VideoCapture(0)

start_time = 0

while True:

    success, frame = webcam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:

        elapsed_time = cv2.getTickCount() - start_time

        remaining_time = 10 - elapsed_time / cv2.getTickFrequency()

        cv2.putText(frame, f"Bakis suresi: {remaining_time:.2f} saniye", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 255), 2)

        if elapsed_time / cv2.getTickFrequency() > 10:
            winsound.Beep(2000, 500)
            cv2.putText(frame, "Supheli davranis!", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            engine.say("kapıyı izleyen biri var!")
            engine.runAndWait()

            # Save the image to a file
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