import pyautogui
import time
import webbrowser
import sys


spam_msg = input("Enter the text you want to spam!\n")
num_of_times = int(input("Enter the number of times you want to send this message\n"))
ph_no = int(input("Enter the phone number you want to spam (Including country code without '+')\n"))


def design():
    """
    Simple animation to show user the status of program
    """
    text = "Opening Whatsapp"
    animation = "|/-\\"

    for i in range(10):
        time.sleep(0.25)
        sys.stdout.write("\r" + 3 * animation[i % len(animation)] + text + 3 * animation[i % len(animation)])
        sys.stdout.flush()


def main():
    """
    Main function to open whatsapp web and send message automatically
    """
    try:
        design()
        webbrowser.open(f"https://web.whatsapp.com/send?phone={ph_no}")
        # Open url of inbox of phone number provided
        time.sleep(25)  # Sleep till webpage loads

        for _ in range(num_of_times):
            pyautogui.typewrite(spam_msg)  # Write the spam message to be sent
            time.sleep(0.1)
            pyautogui.press('enter')  # Send the typed message

    except Exception as e:
        print("Error -", e)  # Exception error
        retry = bool(int(input("Enter 1 to retry, 0 for exit\n")))  # Input for retry or exit
        if retry:
            main()  # Running main function again
        else:
            exit(1)

    time.sleep(5)  # Sleep till message is sent
    pyautogui.hotkey('alt', 'f4')  # Close the current opened window


def log():
    """
    Function to log the actions of the user
    """
    current_date_time = time.asctime(time.localtime())  # Get current time
    with open("database.txt", "a") as f:  # Open file to log the user's data
        f.write(
            f"{current_date_time} "
            f"\n\nTO: +{ph_no} \nMESSAGE: {spam_msg} \n"
            f"NUMBER OF TIMES: {num_of_times}\n------------------------------\n"
        )


if __name__ == '__main__':
    main()
    log()
