import streamlit as st
import datetime
import time

def countdown_timer():
    target_date = datetime.datetime(2026, 2, 1, 0, 0)  # Set the target date and time
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

    current_date = datetime.datetime.now()
    time_difference = target_date - current_date
    total_days = time_difference.days
    total_seconds = time_difference.total_seconds()
    total_hours, remainder = divmod(total_seconds, 3600)

    return months, days, hours, minutes, seconds, milliseconds, total_days, total_hours

def main():
    st.markdown(
        "<h1 style='font-weight: bold; font-size: 70px; text-align: center;'>Countdown Timer</h1>",
        unsafe_allow_html=True
    )


    timer_placeholder = st.empty()

    while True:
        months, days, hours, minutes, seconds, milliseconds,total_days, total_hours = countdown_timer()
        timer_placeholder.write(f"<h2 style='font-weight: bold; font-size: 40px; text-align: center;'>Time Remaining: </h2></br></br>"
                                f"<h2 style='font-weight: bold; font-size: 60px; text-align: center;'>{months} months {days} days</h2>"
                               f"<h3 style='font-weight: bold; font-size: 50px; text-align: center;'>{hours} hours, {minutes} minutes, {seconds} seconds, {milliseconds} milliseconds</h3>"
                                f"<h3 style='font-weight: bold; font-size: 60px; text-align: center;'>{total_days} Days</h3>"
                               f"<h3 style='font-weight: bold; font-size: 60px; text-align: center;'>{total_hours} Hours</h3>", unsafe_allow_html=True)
        time.sleep(0.01)  # Wait for 10 millisecond before updating the timer

if __name__ == "__main__":
    main()
