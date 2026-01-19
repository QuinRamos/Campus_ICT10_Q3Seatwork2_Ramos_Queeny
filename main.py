from pyscript import document

def display_club_info(event=None):
    #Get radio buttons
    online = document.querySelector("input[name='registered']:checked")
    clearance = document.querySelector("input[name='medical']:checked")

    #Dropdown access
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value

    output = document.getElementById("registrationInfo")

    #Validation
    if online is None or clearance is None or grade == "" or section == "":
        output.innerHTML = "<p class='text-danger'>Please answer all questions.</p>"
        return

    # egistration
    if online.value == "Yes" and clearance.value == "Yes":
        output.innerHTML = (
            "<p class='text-success'><strong>Congratulations!</strong><br>"
            "You are now registered.<br>"
            f"Grade {grade} - {section}</p>"
        )
    else:
        output.innerHTML = (
            "<p class='text-dark'>Registration failed.<br>"
            "Please complete online registration and medical clearance.</p>"
        )
