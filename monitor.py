from selenium import webdriver
import time
import yagmail

EMAIL = "test@gmail.com"
PASSWORD = "******** "
DESTINATION = "test@gmail.com"

driver = webdriver.Firefox()
driver.get("https://www.youtube.com/")

print("Page opened! Starting monitoring.")

start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
start_timestamp = time.time()

input("Press Enter to stop monitoring...")

end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
end_timestamp = time.time()

driver.quit()
elapsed_time = round((end_timestamp - start_timestamp) / 60, 2)

message =(f"Time elapsed: {elapsed_time} minutes"
      f"\nStart time: {start_time}"
      f"\nEnd time: {end_time}"
      f"\nActive time: {elapsed_time}")

try:
    yag = yagmail.SMTP(EMAIL, PASSWORD)
    yag.send(to=DESTINATION,
              subject="Monitoring Finished",
                contents=message)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")