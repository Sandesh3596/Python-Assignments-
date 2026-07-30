import sys
import psutil
import os
import time
import smtplib
from email.message import EmailMessage

def ProcessScan():

    ProcessList = []

    try:
        for proc in psutil.process_iter(["pid", "name", "username"]):
            try:
                info = {
                    "pid": proc.info["pid"],
                    "name": proc.info["name"] or "N/A",
                    "username": proc.info["username"] or "N/A"
                }
                ProcessList.append(info)

            except (psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess):
                pass

    except Exception:
        return []

    return ProcessList


def CreateLog(DirectoryName, Data):

    if not os.path.exists(DirectoryName):
        os.mkdir(DirectoryName)

    FileName = os.path.join(
        DirectoryName,
        "ProcessLog_" + time.strftime("%Y%m%d_%H%M%S") + ".txt"
    )

    with open(FileName, "w") as fobj:

        Border = "-" * 50

        fobj.write(Border + "\n")
        fobj.write("Running Process Information\n")
        fobj.write("Log Created At : " + time.ctime() + "\n")
        fobj.write(Border + "\n\n")

        for info in Data:
            fobj.write("PID       : %s\n" % info["pid"])
            fobj.write("Name      : %s\n" % info["name"])
            fobj.write("Username  : %s\n" % info["username"])
            fobj.write(Border + "\n")

    return FileName


def SendMail(FileName, ReceiverMail):

    SenderMail = "youremail@gmail.com"
    Password = "your_app_password"

    try:

        msg = EmailMessage()

        msg["Subject"] = "Process Log"
        msg["From"] = SenderMail
        msg["To"] = ReceiverMail

        msg.set_content("Attached is the process log file.")

        with open(FileName, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="octet-stream",
                filename=os.path.basename(FileName)
            )

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SenderMail, Password)
        server.send_message(msg)
        server.quit()

    except Exception as e:
        print(e)


def main():

    DirectoryName = sys.argv[1]
    MailID = sys.argv[2]

    Data = ProcessScan()

    FileName = CreateLog(DirectoryName, Data)

    SendMail(FileName, MailID)
    print("Mail Sent Sucessfully", MailID)


if __name__ == "__main__":
    main()