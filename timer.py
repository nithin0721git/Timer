import streamlit as st
import datetime
import time

def countdown_timer(target_date):
    current_date = datetime.datetime.now()
    time_difference = target_date - current_date

    seconds = time_difference.total_seconds()
    milliseconds = int((seconds - int(seconds)) * 1000)
    seconds = int(seconds)

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    months = days // 30
    days = days % 30

    return months, days, hours, minutes, seconds, milliseconds

def main():
    st.markdown(
        "<h1 style='font-weight: bold; font-size: 70px; text-align: center;'>Countdown Timer</h1>",
        unsafe_allow_html=True
    )
    target_date = datetime.datetime(2024, 9, 18, 0, 0)  # Set the target date and time

    timer_placeholder = st.empty()

    while True:
        months, days, hours, minutes, seconds, milliseconds = countdown_timer(target_date)
        timer_placeholder.write(f"<h2 style='font-weight: bold; font-size: 40px; text-align: center;'>Time Remaining: </h2></br></br>"
                                f"<h2 style='font-weight: bold; font-size: 60px; text-align: center;'>{months} months {days} days</h2>"
                               f"<h3 style='font-weight: bold; font-size: 50px; text-align: center;'>{hours} hours, {minutes} minutes, {seconds} seconds, {milliseconds} milliseconds</h3>", unsafe_allow_html=True)
        time.sleep(0.001)  # Wait for 1 millisecond before updating the timer

if __name__ == "__main__":
    main()
